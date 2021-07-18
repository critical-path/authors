import pathlib
import authors
import constants


def test_read_configuration_file(configuration_file):
    results = authors.lib.read_configuration_file(file=configuration_file)
    assert results == constants.YAML_WITH_MD_KIND


def test_read_configuration_file_when_file_does_not_exist():
    file = ".this-file-does-not-exist.yml"
    results = authors.lib.read_configuration_file(file=file)
    assert results == str()


def test_parse_yaml_to_dict():
    results = authors.lib.parse_yaml_to_dict(constants.YAML_WITH_MD_KIND)
    assert isinstance(results, dict)
    assert results["name"] == "TEST-AUTHORS"
    assert results["kind"] == "md"
    assert results["heading"] == "Test Heading"
    assert results["opening"] == "Test Opening"
    assert results["closing"] == "Test Closing"


def test_parse_yaml_to_dict_when_yaml_is_empty_str():
    yaml = str()
    results = authors.lib.parse_yaml_to_dict(yaml)
    assert results == dict()


def test_validate_configuration(configuration):
    results = authors.lib.validate_configuration(configuration)
    assert results == configuration


def test_validate_configuration_when_configuration_is_invalid(configuration_with_invalid_kind):
    results = authors.lib.validate_configuration(configuration_with_invalid_kind)
    assert results["name"] == "TEST-AUTHORS"
    assert results["kind"] == "md"
    assert results["heading"] == "Test Heading"
    assert results["opening"] == "Test Opening"
    assert results["closing"] == "Test Closing"


def test_validate_configuration_when_configuration_is_empty_dict():
    configuration = dict()
    results = authors.lib.validate_configuration(configuration)
    assert results == authors.lib.DEFAULT_CONFIGURATION


def test_read_standard_input(standard_input):
    results = authors.lib.read_standard_input()
    assert results == ["Test Author A", "Test Author B", "Test Author C"]


def test_render_template(authors_list, configuration):
    results = authors.lib.render_template(authors_list, configuration)
    assert results == constants.AUTHORS_WITH_MD_KIND


def test_render_template_with_adoc_kind(authors_list, configuration_with_adoc_kind):
    results = authors.lib.render_template(authors_list, configuration_with_adoc_kind)
    assert results == constants.AUTHORS_WITH_ADOC_KIND


def test_render_template_with_html_kind(authors_list, configuration_with_html_kind):
    results = authors.lib.render_template(authors_list, configuration_with_html_kind)
    assert results == constants.AUTHORS_WITH_HTML_KIND


def test_render_template_with_rst_kind(authors_list, configuration_with_rst_kind):
    results = authors.lib.render_template(authors_list, configuration_with_rst_kind)
    assert results == constants.AUTHORS_WITH_RST_KIND


def test_render_template_with_txt_kind(authors_list, configuration_with_txt_kind):
    results = authors.lib.render_template(authors_list, configuration_with_txt_kind)
    assert results == constants.AUTHORS_WITH_TXT_KIND


def test_write_authors_file(rendered_template, configuration):
    authors.lib.write_authors_file(rendered_template, configuration)
    destination_file = pathlib.Path(configuration["name"])
    assert destination_file.exists()
    destination_file.unlink()


def test_main(standard_input, configuration_file, configuration):
    authors.lib.main(file=configuration_file)
    destination_file = pathlib.Path(configuration["name"])
    assert destination_file.exists()
    destination_file.unlink()
