"""The library of functions used by authors."""


from pathlib import Path

from jinja2 import (
    Environment,
    PackageLoader
)

from yaml import (
    load,
    YAMLError
)


CONFIGURATION_FILE = ".authors.yml"


def get_configuration_path(file):
    """Return path to configuration file (.authors.yml)."""

    path = Path()
    directory = path.cwd()
    configuration_path = path.joinpath(directory, file)

    return configuration_path


def get_parsed_configuration_settings(path):
    """Return parsed configuration settings."""

    try:
        with path.open() as reader:
            parsed = reader.read()
            parsed = load(parsed)
    except (FileNotFoundError, IOError, YAMLError):
        parsed = dict()

    return parsed


def get_validated_configuration_settings(settings):
    """Return validated configuration settings, providing
       default values where necessary."""

    fformats = [
        "html",
        "md",
        "rst"
    ]

    try:
        name = settings.get("file").get("name")
        assert isinstance(name, str)
    except AssertionError:
        name = "AUTHORS"

    # We use fformat, because format is the name of a
    # built-in function.

    try:
        fformat = settings.get("file").get("format").lower()
        assert isinstance(fformat, str)
        assert fformat in fformats
    except AssertionError:
        fformat = "md"

    try:
        heading = settings.get("contents").get("heading")
        assert isinstance(heading, str)
    except AssertionError:
        heading = "Authors"

    try:
        opening = settings.get("contents").get("opening")
        assert isinstance(opening, str)
    except AssertionError:
        opening = "Thank you to all of our contributors."

    try:
        closing = settings.get("contents").get("closing")
        assert isinstance(closing, str)
    except AssertionError:
        closing = "This project would not be possible without you."

    validated = dict(
        name=name,
        fformat=fformat,
        heading=heading,
        opening=opening,
        closing=closing
    )

    return validated


def get_authors(source):
    """Return unique, sorted authors from either
       arguments or standard input."""

    skip = [
        "",
        " ",
        "\n"
    ]

    authors = set(source)
    authors = list(author.strip() for author in authors if author not in skip)
    authors.sort(key=str.lower)

    return authors


def get_contents_of_authors_file(authors, **kwargs):
    """Return contents of AUTHORS file."""

    # We use fformat, because format is the name of a
    # built-in function.

    fformat = kwargs.get("fformat")
    file = "template.{}".format(fformat)

    loader = PackageLoader("authors", "templates")
    environment = Environment(
        loader=loader,
        lstrip_blocks=True,
        trim_blocks=True
    )

    template = environment.get_template(file)
    contents = template.render(authors=authors, **kwargs)

    return contents


def write_authors_file(contents, **kwargs):
    """Write AUTHORS file."""

    name = kwargs.get("name")

    with open(name, "w") as writer:
        writer.write(contents)
