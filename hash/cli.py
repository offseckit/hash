"""CLI interface for hash."""

import sys

import click

from . import __version__
from .hashes import HASH_TYPES, generate_hash, identify_hash, list_algorithms

BANNER = f"""\
\033[36m>_\033[0m \033[1mhash\033[0m \033[90mv{__version__}\033[0m
\033[90m   offseckit.com/tools/hash\033[0m
"""


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """Identify hash types and generate hashes in MD5, SHA1, SHA256, SHA512, NTLM, and more.

    \b
    Examples:
      hash id 5d41402abc4b2a76b9719d911017c592
      hash generate -a sha256 "hello"
      hash generate -a md5 -a ntlm "password"
      echo "admin" | hash generate -a sha512
      hash list

    \b
    Part of OffSecKit — https://offseckit.com/tools/hash
    """
    if ctx.invoked_subcommand is None:
        click.echo(BANNER)
        click.echo(ctx.get_help())


@main.command("id")
@click.argument("hash_string", nargs=-1)
@click.option("-i", "--input", "input_text", default=None, help="Hash string (reads stdin if omitted)")
def identify(hash_string, input_text):
    """Identify the type of a hash string.

    \b
    Examples:
      hash id 5d41402abc4b2a76b9719d911017c592
      hash id aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
      echo "hash_value" | hash id
    """
    click.echo(BANNER)

    # Resolve input
    if input_text is not None:
        data = input_text
    elif hash_string:
        data = " ".join(hash_string)
    elif not sys.stdin.isatty():
        data = sys.stdin.read().strip()
    else:
        raise click.ClickException("No hash provided. Pass a hash as an argument, use -i, or pipe via stdin.")

    matches = identify_hash(data)

    if not matches:
        click.secho("No matching hash types found.", fg="yellow")
        click.echo("Verify the input is a valid hash string.")
        return

    click.secho(f"# Input: {data[:80]}", fg="bright_black")
    click.secho(f"# Length: {len(data.strip())} characters\n", fg="bright_black")

    for match in matches:
        confidence = match["confidence"]
        color = {"high": "green", "medium": "yellow", "low": "red"}.get(confidence, "white")
        click.secho(f"  {match['type']['name']}", fg="cyan", nl=False)
        click.secho(f"  [{confidence}]", fg=color, nl=False)
        click.secho(f"  {match['reason']}", fg="bright_black")

    click.echo()


@main.command("generate")
@click.option("-a", "--algo", multiple=True,
              help="Algorithm(s) to use (e.g., -a md5 -a sha256). Default: md5,sha1,sha256,ntlm")
@click.option("-i", "--input", "input_text", default=None, help="Text to hash (reads stdin if omitted)")
@click.argument("text", nargs=-1)
def generate(algo, input_text, text):
    """Generate hash(es) of the given text.

    \b
    Examples:
      hash generate "hello"
      hash generate -a sha256 "password"
      hash generate -a md5 -a sha1 -a ntlm "test"
      echo "secret" | hash generate -a sha512
    """
    click.echo(BANNER)

    # Resolve input
    if input_text is not None:
        data = input_text
    elif text:
        data = " ".join(text)
    elif not sys.stdin.isatty():
        data = sys.stdin.read().rstrip("\n")
    else:
        raise click.ClickException("No input provided. Pass text as an argument, use -i, or pipe via stdin.")

    # Default algorithms
    algorithms = list(algo) if algo else ["md5", "sha1", "sha256", "ntlm"]

    # Validate
    valid_ids = {h["id"] for h in HASH_TYPES}
    for a in algorithms:
        if a not in valid_ids:
            raise click.ClickException(
                f"Unknown algorithm: {a}. Use 'hash list' to see available algorithms."
            )

    click.secho(f"# Input: {data[:80]}", fg="bright_black")
    click.secho(f"# Bytes: {len(data.encode('utf-8'))}\n", fg="bright_black")

    for a in algorithms:
        try:
            result = generate_hash(a, data)
            algo_name = next(h["name"] for h in HASH_TYPES if h["id"] == a)
            click.secho(f"  {algo_name}", fg="cyan")
            click.echo(f"  {result}")
            click.echo()
        except Exception as e:
            click.secho(f"  {a}: error — {e}", fg="red")


@main.command("list")
def list_cmd():
    """List all supported hash algorithms."""
    algorithms = list_algorithms()

    click.secho("# Supported Algorithms\n", fg="bright_magenta")
    click.secho(f"  {'Algorithm':<12} {'Bits':<8} {'Hex Length'}", fg="bright_black")
    click.secho(f"  {'─' * 12} {'─' * 8} {'─' * 10}", fg="bright_black")

    for algo in algorithms:
        click.secho(f"  {algo['name']:<12}", fg="cyan", nl=False)
        click.echo(f" {algo['bits']:<8} {algo['bits'] // 4}")


if __name__ == "__main__":
    main()
