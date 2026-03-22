# >_ hash

**Hash identifier & generator CLI — identify unknown hash types and generate hashes from your terminal.**

Part of [OffSecKit](https://offseckit.com) | [Browser version](https://offseckit.com/tools/hash)

## Install

```bash
pip install offseckit-hash
```

Or clone and install locally:

```bash
git clone https://github.com/offseckit/hash.git
cd hash
pip install .
```

## Quick Start

```bash
# Identify a hash
hash id 5d41402abc4b2a76b9719d911017c592

# Output:
# >_ hash v0.1.0
#    offseckit.com/tools/hash
#
# # Input: 5d41402abc4b2a76b9719d911017c592
# # Length: 32 characters
#
#   MD5    [medium]  32 hex characters — could be MD5 or NTLM
#   NTLM   [medium]  32 hex characters — could be MD5 or NTLM

# Generate hashes
hash generate "hello"

# Output:
# >_ hash v0.1.0
#    offseckit.com/tools/hash
#
# # Input: hello
# # Bytes: 5
#
#   MD5
#   5d41402abc4b2a76b9719d911017c592
#
#   SHA-1
#   aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
#
#   SHA-256
#   2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
#
#   NTLM
#   066ddfd4ef0e9cd7c256fe77191ef43c
```

## Usage

```
hash [COMMAND]
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `--help` | Show help | — |

### Commands

| Command | Description |
|---------|-------------|
| `id` | Identify the type of a hash string |
| `generate` | Generate hash(es) of the given text |
| `list` | List all supported hash algorithms |

### `hash id` Options

| Flag | Description | Default |
|------|-------------|---------|
| `-i, --input` | Hash string | (reads stdin if omitted) |

### `hash generate` Options

| Flag | Description | Default |
|------|-------------|---------|
| `-a, --algo` | Algorithm(s) to use (repeatable) | `md5,sha1,sha256,ntlm` |
| `-i, --input` | Text to hash | (reads stdin if omitted) |

## Examples

```bash
# Identify an MD5 hash
hash id 5d41402abc4b2a76b9719d911017c592

# Identify a SHA-256 hash
hash id 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Identify a hash from a file or pipe
echo "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d" | hash id

# Generate SHA-256 hash only
hash generate -a sha256 "password"

# Generate multiple specific algorithms
hash generate -a md5 -a ntlm -a sha512 "admin"

# Generate NTLM hash for Windows credential testing
hash generate -a ntlm "P@ssw0rd"

# Hash from stdin (useful in pipelines)
echo -n "secret" | hash generate -a sha256

# Generate all supported algorithms
hash generate -a md5 -a sha1 -a sha256 -a sha384 -a sha512 -a ntlm -a sha3-256 -a sha3-512 "test"

# List all supported algorithms
hash list
```

## Supported Algorithms

| Algorithm | Bits | Hex Length | Notes |
|-----------|------|------------|-------|
| **MD5** | 128 | 32 | Widely used, cryptographically broken |
| **SHA-1** | 160 | 40 | Deprecated for security use |
| **SHA-256** | 256 | 64 | SHA-2 family, standard for most uses |
| **SHA-384** | 384 | 96 | SHA-2 family, truncated SHA-512 |
| **SHA-512** | 512 | 128 | SHA-2 family, maximum security |
| **NTLM** | 128 | 32 | Windows password hashes (MD4 of UTF-16LE) |
| **SHA3-256** | 256 | 64 | SHA-3 (Keccak) family |
| **SHA3-512** | 512 | 128 | SHA-3 (Keccak) family |

## Requirements

- Python 3.8+
- No external dependencies beyond `click`

## Related

- [OffSecKit](https://offseckit.com) — Free browser-based security toolkit
- [Browser version](https://offseckit.com/tools/hash) — Use hash identifier & generator in your browser
- [Hash Identification Guide](https://offseckit.com/blog/hash-identifier-guide) — Full guide with examples

## License

MIT
