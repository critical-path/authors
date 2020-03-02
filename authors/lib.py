"""
This module contains functions used by authors.
"""


import pathlib
import sys
import jinja2
import yaml


CONFIGURATION_FILE = ".authors.yml"

DEFAULT_CONFIGURATION = {
    "name": "AUTHORS",
    "kind": "md",
    "heading": "Authors",
    "opening": "Thank you to all of our contributors.",
    "closing": "This project would not be possible without you."
}

VALID_KINDS = [
    "html",
    "md",
    "rst",
    "txt"
]


def read_configuration_file(file=CONFIGURATION_FILE):
    """
    Reads a configuration file, usually `.authors.yml`.

    Parameters
    ----------
    file : str
        The name of a file with user-defined
        configuration settings.

        The default value is `.authors.yml`.

    Returns
    -------
    str
        The contents of a configuration file or an
        empty str.
    """

    path = pathlib.Path(file)

    if path.exists():
        return path.read_text()
    else:
        return str()


def parse_yaml_to_dict(contents):
    """
    Parses YAML to a dict.

    Parameters
    ----------
    contents : str
        The contents of a file with user-defined
        configuration settings.

    Returns
    -------
    dict
       Configuration settings (one key-value
       pair per setting) or an empty dict.
    """

    if contents:
        return yaml.safe_load(contents)
    else:
        return dict()


def validate_configuration(configuration):
    """
    Validates configuration settings.

    Parameters
    ----------
    configuration : dict
        The unvalidated configuration settings.

    Returns
    -------
    configuration : dict
        The validated configuration settings,
        using default values in the case of
        missing or invalid values.
    """

    # Iterate over each key in DEFAULT_CONFIGURATION.
    #
    # If the user-defined configuration settings do not
    # contain this key, then add it and set its value
    # to that found in DEFAULT_CONFIGURATION.

    for key in DEFAULT_CONFIGURATION:
        if key not in configuration:
            configuration[key] = DEFAULT_CONFIGURATION[key]

    # Make sure that the value of the `kind` key
    # is `html`, `md`, `rst`, or `txt`.

    if configuration["kind"] not in VALID_KINDS:
        configuration["kind"] = DEFAULT_CONFIGURATION["kind"]

    return configuration


def read_standard_input():
    """
    Reads from standard input.

    Returns
    -------
    authors : list
        A unique, sorted list of authors.
    """

    authors = sys.stdin.read().splitlines()
    authors = set(authors)
    return sorted(authors, key=str.lower)


def render_template(authors, configuration):
    """
    Renders a template in `html`, `md`, `rst`,
    or `txt` format.

    Parameters
    ----------
    authors : list
        The authors to include in the rendered
        template.

    configuration : dict
        Configuration settings relevant to the
        rendered template (`heading`, `opening`,
        and `closing`).

    Returns
    -------
    str
        The rendered template.
    """

    loader = jinja2.PackageLoader("authors", "templates")

    environment = jinja2.Environment(
        loader=loader,
        lstrip_blocks=True,
        trim_blocks=True
    )

    source_file = "template.{}".format(configuration["kind"])
    template = environment.get_template(source_file)
    return template.render(authors=authors, **configuration)


def write_authors_file(contents, configuration):
    """
    Writes the rendered template to a file,
    usually `AUTHORS`.

    Parameters
    ----------
    contents : str
        The rendered template.

    configuration : dict
        Configuration settings relevant to the
        AUTHORS file (`name`).
    """

    destination_file = configuration["name"]

    with open(destination_file, "w") as writer:
        writer.write(contents)


def main(file=CONFIGURATION_FILE):
    """
    Generates an AUTHORS file.

    Parameters
    ----------
    file : str
        The name of a file with user-defined
        configuration settings.

        The default value is `.authors.yml`.
    """

    configuration = read_configuration_file(file=file)
    parsed = parse_yaml_to_dict(configuration)
    validated = validate_configuration(parsed)
    authors = read_standard_input()
    rendered = render_template(authors, validated)
    write_authors_file(rendered, validated)
