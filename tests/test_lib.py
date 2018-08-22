from pathlib import Path

from yaml import load

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
    SOURCE,
    create_configuration_file,
    delete_configuration_file
)

def test_get_configuration_path():
    path = get_configuration_path(CONFIGURATION_FILE)
    assert path.is_absolute()
    assert CONFIGURATION_FILE in path.parts

def test_get_parsed_configuration_settings():
    create_configuration_file(YAML_MD_FORMAT)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    assert parsed == load(YAML_MD_FORMAT)

    delete_configuration_file()

def test_get_parsed_configuration_settings_error_no_file():
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    assert parsed == {}

def test_get_parsed_configuration_settings_error_invalid_yaml():
    create_configuration_file(INVALID_YAML)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    assert parsed == {}

    delete_configuration_file()

def test_get_validated_configuration_settings():
    create_configuration_file(YAML_MD_FORMAT)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS

    delete_configuration_file()

def test_get_validated_configuration_settings_no_name():
    create_configuration_file(YAML_NO_NAME)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_NAME

    delete_configuration_file()

def test_get_validated_configuration_settings_name_not_str():
    create_configuration_file(YAML_NAME_NOT_STR)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_NAME

    delete_configuration_file()

def test_get_validated_configuration_settings_no_format():
    create_configuration_file(YAML_NO_FORMAT)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_FORMAT

    delete_configuration_file()

def test_get_validated_configuration_settings_format_not_str():
    create_configuration_file(YAML_FORMAT_NOT_STR)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_FORMAT

    delete_configuration_file()

def test_get_validated_configuration_settings_format_not_in_list():
    create_configuration_file(YAML_FORMAT_NOT_IN_LIST)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_FORMAT

    delete_configuration_file()

def test_get_validated_configuration_settings_no_heading():
    create_configuration_file(YAML_NO_HEADING)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_HEADING

    delete_configuration_file()

def test_get_validated_configuration_settings_heading_not_str():
    create_configuration_file(YAML_HEADING_NOT_STR)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_HEADING

    delete_configuration_file()

def test_get_validated_configuration_settings_no_opening():
    create_configuration_file(YAML_NO_OPENING)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_OPENING

    delete_configuration_file()

def test_get_validated_configuration_settings_opening_not_str():
    create_configuration_file(YAML_OPENING_NOT_STR)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_OPENING

    delete_configuration_file()

def test_get_validated_configuration_settings_no_closing():
    create_configuration_file(YAML_NO_CLOSING)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_CLOSING

    delete_configuration_file()

def test_get_validated_configuration_settings_closing_not_str():
    create_configuration_file(YAML_CLOSING_NOT_STR)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    assert validated == SETTINGS_DEFAULT_CLOSING

    delete_configuration_file()

def test_get_authors():
    authors = get_authors(SOURCE)
    assert authors == ["author-a", "Author-B", "author-c"]

def test_get_contents_of_authors_file_md():
    create_configuration_file(YAML_MD_FORMAT)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    authors = get_authors(SOURCE)

    contents = get_contents_of_authors_file(authors, **validated)
    assert contents == CONTENTS_MD

    delete_configuration_file()

def test_get_contents_of_authors_file_html():
    create_configuration_file(YAML_HTML_FORMAT)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    authors = get_authors(SOURCE)

    contents = get_contents_of_authors_file(authors, **validated)
    assert contents == CONTENTS_HTML

    delete_configuration_file()

def test_get_contents_of_authors_file_rst():
    create_configuration_file(YAML_RST_FORMAT)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    authors = get_authors(SOURCE)

    contents = get_contents_of_authors_file(authors, **validated)
    assert contents == CONTENTS_RST

    delete_configuration_file()

def test_write_authors_file():
    create_configuration_file(YAML_MD_FORMAT)

    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    authors = get_authors(SOURCE)
    contents = get_contents_of_authors_file(authors, **validated)

    write_authors_file(contents, **validated)
    assert Path("TEST-AUTHORS").exists()

    Path("TEST-AUTHORS").unlink()
    delete_configuration_file()
