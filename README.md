[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkkent030315%2Fntstatus.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fkkent030315%2Fntstatus?ref=badge_shield)
![crates.io](https://img.shields.io/crates/v/ntstatus.svg?label=crates.io:ntstatus)

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fkkent030315%2Fntstatus.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fkkent030315%2Fntstatus?ref=badge_large)

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
