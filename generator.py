def main() -> None:
  with open(file='./ntstatus.txt', mode='r', encoding='utf-8') as input_file:
    with open(file='./src/ntstatus.rs', mode='w+', encoding='utf-8') as output_file:
      with open(file='./src/test.rs', mode='w+', encoding='utf-8') as test_file:
        output_file.write("""use num_enum::TryFromPrimitive;\n
#[derive(Debug, TryFromPrimitive)]
#[repr(u32)]
#[allow(non_camel_case_types)]
pub enum NtStatus {""")
        lines = input_file.readlines()
        for line in lines:
          line = line.replace('\n', '')
          (symbol, value) = line.split(':')
          if symbol.startswith('//'):
            continue
          output_file.write(f'\n    {symbol} = {value},')
        output_file.write('\n}')
        output_file.write("""\n\nimpl NtStatus {
    pub fn from_u32(value: u32) -> Option<&'static str> {
        match NtStatus::try_from(value) {""")
        for line in lines:
          line = line.replace('\n', '')
          (symbol, value) = line.split(':')
          if symbol.startswith('//'):
            continue
          output_file.write(f'\n            Ok(NtStatus::{symbol}) => Some("{symbol}"),')
        output_file.write("""\n            Err(_) => None,
        }
    }
}
""")
        test_file.write("""#![cfg(test)]\n
use crate::ntstatus::NtStatus;\n
#[test]
fn test_from_u32() {""")
        for line in lines:
          line = line.replace('\n', '')
          (symbol, value) = line.split(':')
          if symbol.startswith('//'):
            continue
          test_file.write(f'\n    assert_eq!(NtStatus::from_u32({value}), Some("{symbol}"));')
        test_file.write('}\n')


if __name__ == '__main__':
  main()
