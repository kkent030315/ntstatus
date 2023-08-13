[![GitGuardian scan](https://github.com/kkent030315/ntstatus/actions/workflows/gitguardian.yml/badge.svg)](https://github.com/kkent030315/ntstatus/actions/workflows/gitguardian.yml)
![crates.io](https://img.shields.io/crates/v/ntstatus.svg?label=crates.io:ntstatus)

# ntstatus

NTSTATUS bindings for Rust

# NTSTATUS to string conversion

```rust
fn main() {
    assert_eq!(NtStatus::from_u32(0x00000000), Some("STATUS_SUCCESS"));
}
```

# License

[LICENSE - Apache 2.0](./LICENSE)
