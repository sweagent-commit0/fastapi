try:
    from fastapi_cli.cli import main as cli_main
except ImportError:
    cli_main = None