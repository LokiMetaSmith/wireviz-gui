import logging
import os
from pathlib import Path

import click

from wireviz_gui.app import Application


@click.command()
@click.argument("file", required=False, type=click.Path(exists=True, dir_okay=False))
@click.option(
    "--graphviz-path",
    "-p",
    default=None,
    type=click.Path(file_okay=False),
    help="The directory path on which GraphViz binary may be found.",
)
@click.option(
    "--loglevel",
    "-l",
    default="INFO",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=False),
    help="Logging level.",
)
def main(file=None, graphviz_path=None, loglevel="INFO"):
    if graphviz_path is not None:
        _graphviz_path = Path(graphviz_path).resolve()
        if os.environ.get("PATH", "").endswith(os.pathsep):
            os.environ["PATH"] += str(_graphviz_path)
        else:
            os.environ["PATH"] = os.environ.get("PATH", "") + os.pathsep + str(_graphviz_path)

    numeric_level = getattr(logging, loglevel.upper(), logging.INFO)
    logging.basicConfig(level=numeric_level)
    Application(initial_file=file, loglevel=numeric_level)


if __name__ == "__main__":
    main()
