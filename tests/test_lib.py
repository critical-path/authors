from pathlib import Path

from pytest import mark

from yaml import safe_load

from authors.lib import (
    get_configuration_path,
    get_parsed_configuration_settings,
    get_validated_configuration_settings,
    get_authors,
    get_contents_of_authors_file,
    write_authors_file
)

from constants import (
    CONFIGURATION_FILE,
    INVALID_YAML,
    YAML_MD_FORMAT,
    YAML_HTML_FORMAT,
    YAML_RST_FORMAT,
    YAML_NO_NAME,
    YAML_NO_FORMAT,
    YAML_NO_HEADING,
    YAML_NO_OPENING,
    YAML_NO_CLOSING,
    YAML_NAME_NOT_STR,
    YAML_FORMAT_NOT_STR,
    YAML_HEADING_NOT_STR,
    YAML_OPENING_NOT_STR,
    YAML_CLOSING_NOT_STR,
    YAML_FORMAT_NOT_IN_LIST,
    SETTINGS,
    SETTINGS_DEFAULT_NAME,
    SETTINGS_DEFAULT_FORMAT,
    SETTINGS_DEFAULT_HEADING,
    SETTINGS_DEFAULT_OPENING,
    SETTINGS_DEFAULT_CLOSING,
    CONTENTS_MD,
    CONTENTS_HTML,
    CONTENTS_RST,
    SOURCE
)


def test_get_configuration_path():
    path = get_configuration_path(CONFIGURATION_FILE)
    assert path.is_absolute()
    assert CONFIGURATION_FILE in path.parts


@mark.parametrize("configuration", [YAML_MD_FORMAT], indirect=True)
def test_get_parsed_configuration_settings(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    assert parsed == safe_load(YAML_MD_FORMAT)


def test_get_parsed_configuration_settings_error_no_file():
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    assert parsed == {}


@mark.parametrize("configuration", [INVALID_YAML], indirect=True)
def test_get_parsed_configuration_settings_error_invalid_yaml(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    assert parsed == {}


@mark.parametrize("configuration", [YAML_MD_FORMAT], indirect=True)
def test_get_validated_configuration_settings(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS


@mark.parametrize("configuration", [YAML_NO_NAME], indirect=True)
def test_get_validated_configuration_settings_no_name(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_NAME


@mark.parametrize("configuration", [YAML_NAME_NOT_STR], indirect=True)
def test_get_validated_configuration_settings_name_not_str(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_NAME


@mark.parametrize("configuration", [YAML_NO_FORMAT], indirect=True)
def test_get_validated_configuration_settings_no_format(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_FORMAT


@mark.parametrize("configuration", [YAML_FORMAT_NOT_STR], indirect=True)
def test_get_validated_configuration_settings_format_not_str(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_FORMAT


@mark.parametrize("configuration", [YAML_FORMAT_NOT_IN_LIST], indirect=True)
def test_get_validated_configuration_settings_format_not_in_list(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_FORMAT


@mark.parametrize("configuration", [YAML_NO_HEADING], indirect=True)
def test_get_validated_configuration_settings_no_heading(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_HEADING


@mark.parametrize("configuration", [YAML_HEADING_NOT_STR], indirect=True)
def test_get_validated_configuration_settings_heading_not_str(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_HEADING


@mark.parametrize("configuration", [YAML_NO_OPENING], indirect=True)
def test_get_validated_configuration_settings_no_opening(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_OPENING


@mark.parametrize("configuration", [YAML_OPENING_NOT_STR], indirect=True)
def test_get_validated_configuration_settings_opening_not_str(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_OPENING


@mark.parametrize("configuration", [YAML_NO_CLOSING], indirect=True)
def test_get_validated_configuration_settings_no_closing(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_CLOSING


@mark.parametrize("configuration", [YAML_CLOSING_NOT_STR], indirect=True)
def test_get_validated_configuration_settings_closing_not_str(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_CLOSING


def test_get_authors():
    authors = get_authors(SOURCE)
    assert authors == ["author-a", "Author-B", "author-c"]


@mark.parametrize("configuration", [YAML_MD_FORMAT], indirect=True)
def test_get_contents_of_authors_file_md(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    authors = get_authors(SOURCE)

    contents = get_contents_of_authors_file(authors, **validated)
    assert contents == CONTENTS_MD


@mark.parametrize("configuration", [YAML_HTML_FORMAT], indirect=True)
def test_get_contents_of_authors_file_html(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    authors = get_authors(SOURCE)

    contents = get_contents_of_authors_file(authors, **validated)
    assert contents == CONTENTS_HTML


@mark.parametrize("configuration", [YAML_RST_FORMAT], indirect=True)
def test_get_contents_of_authors_file_rst(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    authors = get_authors(SOURCE)

    contents = get_contents_of_authors_file(authors, **validated)
    assert contents == CONTENTS_RST


@mark.parametrize("configuration", [YAML_MD_FORMAT], indirect=True)
def test_write_authors_file(configuration):
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    authors = get_authors(SOURCE)
    contents = get_contents_of_authors_file(authors, **validated)

    write_authors_file(contents, **validated)
    assert Path("TEST-AUTHORS").exists()

    Path("TEST-AUTHORS").unlink()
