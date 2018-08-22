from authors.lib import (
    CONFIGURATION_FILE,
    get_authors,
    get_configuration_path,
    get_contents_of_authors_file,
    get_parsed_configuration_settings,
    get_validated_configuration_settings,
    write_authors_file
)

from click import (
    argument,
    command,
    get_text_stream
)

@command()
@argument("authors", nargs=-1)
def thank_authors(authors):
    """Create an AUTHORS file to thank the people 
       who contribute to your Git/GitHub project."""

    # source = arguments | standard input

    source = authors if authors else get_text_stream("stdin")
    authors = get_authors(source)
    path = get_configuration_path(CONFIGURATION_FILE)
    parsed = get_parsed_configuration_settings(path)
    validated = get_validated_configuration_settings(parsed)
    contents = get_contents_of_authors_file(authors, **validated)
    write_authors_file(contents, **validated)

if __name__ == "__main__":
    thank_authors()
