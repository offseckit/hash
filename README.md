# >_ osk hash

**Identify unknown hash types and generate hashes from your terminal.**

Part of [OffSecKit](https://offseckit.com) | [Browser version](https://offseckit.com/tools/hash) | [Unified CLI](https://github.com/offseckit/osk)

## Install

This tool is part of the OffSecKit CLI toolkit:

```bash
pip install offseckit
```

## Usage

```bash
# Identify a hash
osk hash id 5d41402abc4b2a76b9719d911017c592

# Generate hashes
osk hash generate -a sha256 "password"
osk hash generate -a md5 -a ntlm "test"

# List supported algorithms
osk hash list
```

## Related

- [OffSecKit CLI](https://github.com/offseckit/osk) — full toolkit (`pip install offseckit`)
- [Browser version](https://offseckit.com/tools/hash) — use in your browser
- [Hash Identifier Guide](https://offseckit.com/blog/hash-identifier-guide) — practical guide

## License

MIT
