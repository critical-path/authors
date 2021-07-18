import io
import pytest
import authors
import constants


# This represents the result of redirecting `git log --format=%an`
# to standard input.  Standard input is blocked by pytest,
# so we need a mock-up.

@pytest.fixture
def standard_input(monkeypatch):
    git_log = "Test Author C\nTest Author B\nTest Author A\n"
    return monkeypatch.setattr("sys.stdin", io.StringIO(git_log))


# This represents a configuration file for which the value of
# `kind` is `md`.

@pytest.fixture
def configuration_file(tmp_path):
    file = tmp_path.joinpath(constants.CONFIGURATION_FILE)
    file.write_text(constants.YAML_WITH_MD_KIND)
    yield file.as_posix()


# This represents a configuration file for which the value of
# `kind` is `adoc`.

@pytest.fixture
def configuration_file_with_adoc_kind(tmp_path):
    file = tmp_path.joinpath(constants.CONFIGURATION_FILE)
    file.write_text(constants.YAML_WITH_ADOC_KIND)
    yield file.as_posix()


# This represents a configuration file for which the value of
# `kind` is `html`.

@pytest.fixture
def configuration_file_with_html_kind(tmp_path):
    file = tmp_path.joinpath(constants.CONFIGURATION_FILE)
    file.write_text(constants.YAML_WITH_HTML_KIND)
    yield file.as_posix()


# This represents a configuration file for which the value of
# `kind` is `rst`.

@pytest.fixture
def configuration_file_with_rst_kind(tmp_path):
    file = tmp_path.joinpath(constants.CONFIGURATION_FILE)
    file.write_text(constants.YAML_WITH_RST_KIND)
    yield file.as_posix()


# This represents a configuration file for which the value of
# `kind` is `txt`.

@pytest.fixture
def configuration_file_with_txt_kind(tmp_path):
    file = tmp_path.joinpath(constants.CONFIGURATION_FILE)
    file.write_text(constants.YAML_WITH_TXT_KIND)
    yield file.as_posix()


# This represents a configuration file for which the value of
# `kind` is `invalid`.

@pytest.fixture
def configuration_file_with_invalid_kind(tmp_path):
    file = tmp_path.joinpath(constants.CONFIGURATION_FILE)
    file.write_text(constants.YAML_WITH_INVALID_KIND)
    yield file.as_posix()


# This represents valid configuration settings parsed from a
# file.  The value of `kind` is `md`, so it will produce
# an AUTHORS file in MD format.

@pytest.fixture
def configuration(configuration_file):
    yaml = authors.lib.read_configuration_file(file=configuration_file)
    return authors.lib.parse_yaml_to_dict(yaml)


# This represents valid configuration settings parsed from a
# file.  The value of `kind` is `adoc`, so it will produce
# an AUTHORS file in ADOC format.

@pytest.fixture
def configuration_with_adoc_kind(configuration_file_with_adoc_kind):
    yaml = authors.lib.read_configuration_file(file=configuration_file_with_adoc_kind)
    return authors.lib.parse_yaml_to_dict(yaml)


# This represents valid configuration settings parsed from a
# file.  The value of `kind` is `html`, so it will produce
# an AUTHORS file in HTML format.

@pytest.fixture
def configuration_with_html_kind(configuration_file_with_html_kind):
    yaml = authors.lib.read_configuration_file(file=configuration_file_with_html_kind)
    return authors.lib.parse_yaml_to_dict(yaml)


# This represents valid configuration settings parsed from a
# file.  The value of `kind` is `rst`, so it will produce
# an AUTHORS file in RST format.

@pytest.fixture
def configuration_with_rst_kind(configuration_file_with_rst_kind):
    yaml = authors.lib.read_configuration_file(file=configuration_file_with_rst_kind)
    return authors.lib.parse_yaml_to_dict(yaml)


# This represents valid configuration settings parsed from a
# file.  The value of `kind` is `txt`, so it will produce
# an AUTHORS file in text format.

@pytest.fixture
def configuration_with_txt_kind(configuration_file_with_txt_kind):
    yaml = authors.lib.read_configuration_file(file=configuration_file_with_txt_kind)
    return authors.lib.parse_yaml_to_dict(yaml)


# This represents invalid configuration settings parsed from a
# file.  The value of `kind` is `invalid`, so it will produce
# an AUTHORS file in the default format (MD).

@pytest.fixture
def configuration_with_invalid_kind(configuration_file_with_invalid_kind):
    yaml = authors.lib.read_configuration_file(file=configuration_file_with_invalid_kind)
    return authors.lib.parse_yaml_to_dict(yaml)


# This represents a list of authors, the result of calling
# `authors.lib.read_standard_input`.

@pytest.fixture
def authors_list():
    return ["Test Author A", "Test Author B", "Test Author C"]


# This represents a rendered template.

@pytest.fixture
def rendered_template(authors_list, configuration):
    return authors.lib.render_template(authors_list, configuration)
