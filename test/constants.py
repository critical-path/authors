CONFIGURATION_FILE = ".test-authors.yml"

YAML = """
name: TEST-AUTHORS
kind: {}
heading: Test Heading
opening: Test Opening
closing: Test Closing
"""

YAML_WITH_MD_KIND = YAML.format("md")

YAML_WITH_ADOC_KIND = YAML.format("adoc")

YAML_WITH_HTML_KIND = YAML.format("html")

YAML_WITH_RST_KIND = YAML.format("rst")

YAML_WITH_TXT_KIND = YAML.format("txt")

YAML_WITH_INVALID_KIND = YAML.format("invalid")

AUTHORS_WITH_MD_KIND = """
# Test Heading

Test Opening

- Test Author A
- Test Author B
- Test Author C

Test Closing
""".strip()

AUTHORS_WITH_ADOC_KIND = """
= Test Heading

Test Opening

* Test Author A
* Test Author B
* Test Author C

Test Closing
""".strip()

AUTHORS_WITH_HTML_KIND = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Authors</title>
  </head>
  <body>
    <h1>Test Heading</h1>
    <p>Test Opening</p>
    <ul>
      <li>Test Author A</li>
      <li>Test Author B</li>
      <li>Test Author C</li>
    </ul>
    <p>Test Closing</p>
  </body>
</html>
""".strip()

AUTHORS_WITH_RST_KIND = """
Test Heading
=============

Test Opening

- Test Author A
- Test Author B
- Test Author C

Test Closing
""".strip()

AUTHORS_WITH_TXT_KIND = """
Test Heading

Test Opening

- Test Author A
- Test Author B
- Test Author C

Test Closing
""".strip()
