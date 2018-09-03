from pathlib import Path

from subprocess import (
    PIPE,
    Popen
)

from click.testing import CliRunner

from authors.cli import thank_authors


def test_options():
    path = Path("AUTHORS")

    runner = CliRunner()
    result = runner.invoke(
        thank_authors,
        ["author-c", "Author-B", "author-a"]
    )

    assert result.exit_code == 0
    assert path.stat()

    path.unlink()


def test_standard_input():
    path = Path("AUTHORS")

    runner = CliRunner()
    result = runner.invoke(
        thank_authors,
        ["\n", "author-c", "Author-B", "author-a"]
    )

    assert result.exit_code == 0
    assert path.stat()

    path.unlink()


def test_standard_input_redirection():
    path = Path("AUTHORS")

    echo = Popen(
        ["echo", "-e", "author-c\nAuthor-B\nauthor-a"],
        stdout=PIPE
    )

    thank_authors = Popen(
        ["authors"],
        stdin=echo.stdout
    )

    standard_output, standard_error = thank_authors.communicate()

    assert path.stat()

    path.unlink()
