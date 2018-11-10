CONFIGURATION_FILE = ".test.authors.yml"

YAML_MD_FORMAT = "file:\n" +\
                 "  name: TEST-AUTHORS\n" +\
                 "  format: md\n" +\
                 "contents:\n" +\
                 "  heading: Test-Heading\n" +\
                 "  opening: Test-Opening\n" +\
                 "  closing: Test-Closing\n"

YAML_HTML_FORMAT = "file:\n" +\
                   "  name: TEST-AUTHORS\n" +\
                   "  format: html\n" +\
                   "contents:\n" +\
                   "  heading: Test-Heading\n" +\
                   "  opening: Test-Opening\n" +\
                   "  closing: Test-Closing\n"

YAML_RST_FORMAT = "file:\n" +\
                  "  name: TEST-AUTHORS\n" +\
                  "  format: rst\n" +\
                  "contents:\n" +\
                  "  heading: Test-Heading\n" +\
                  "  opening: Test-Opening\n" +\
                  "  closing: Test-Closing\n"

YAML_NO_NAME = "file:\n" +\
               "  format: md\n" +\
               "contents:\n" +\
               "  heading: Test-Heading\n" +\
               "  opening: Test-Opening\n" +\
               "  closing: Test-Closing\n"

YAML_NAME_NOT_STR = "file:\n" +\
                    "  name:\n" +\
                    "    - TEST-AUTHORS\n" +\
                    "  format: md\n" +\
                    "contents:\n" +\
                    "  heading: Test-Heading\n" +\
                    "  opening: Test-Opening\n" +\
                    "  closing: Test-Closing\n"

YAML_NO_FORMAT = "file:\n" +\
                 "  name: TEST-AUTHORS\n" +\
                 "contents:\n" +\
                 "  heading: Test-Heading\n" +\
                 "  opening: Test-Opening\n" +\
                 "  closing: Test-Closing\n"

YAML_FORMAT_NOT_STR = "file:\n" +\
                      "  name: TEST-AUTHORS\n" +\
                      "  format:\n" +\
                      "    - md\n" +\
                      "contents:\n" +\
                      "  heading: Test-Heading\n" +\
                      "  opening: Test-Opening\n" +\
                      "  closing: Test-Closing\n"

YAML_FORMAT_NOT_IN_LIST = "file:\n" +\
                          "  name: TEST-AUTHORS\n" +\
                          "  format: xml\n" +\
                          "contents:\n" +\
                          "  heading: Test-Heading\n" +\
                          "  opening: Test-Opening\n" +\
                          "  closing: Test-Closing\n"

YAML_NO_HEADING = "file:\n" +\
                  "  name: TEST-AUTHORS\n" +\
                  "  format: md\n" +\
                  "contents:\n" +\
                  "  opening: Test-Opening\n" +\
                  "  closing: Test-Closing\n"

YAML_HEADING_NOT_STR = "file:\n" +\
                       "  name: TEST-AUTHORS\n" +\
                       "  format: md\n" +\
                       "contents:\n" +\
                       "  heading:\n" +\
                       "    - Test-Heading\n" +\
                       "  opening: Test-Opening\n" +\
                       "  closing: Test-Closing\n"

YAML_NO_OPENING = "file:\n" +\
                  "  name: TEST-AUTHORS\n" +\
                  "  format: md\n" +\
                  "contents:\n" +\
                  "  heading: Test-Heading\n" +\
                  "  closing: Test-Closing\n"

YAML_OPENING_NOT_STR = "file:\n" +\
                       "  name: TEST-AUTHORS\n" +\
                       "  format: md\n" +\
                       "contents:\n" +\
                       "  heading: Test-Heading\n" +\
                       "  opening:\n" +\
                       "    - Test-Opening\n" +\
                       "  closing: Test-Closing\n"

YAML_NO_CLOSING = "file:\n" +\
                  "  name: TEST-AUTHORS\n" +\
                  "  format: md\n" +\
                  "contents:\n" +\
                  "  heading: Test-Heading\n" +\
                  "  opening: Test-Opening\n"

YAML_CLOSING_NOT_STR = "file:\n" +\
                       "  name: TEST-AUTHORS\n" +\
                       "  format: md\n" +\
                       "contents:\n" +\
                       "  heading: Test-Heading\n" +\
                       "  opening: Test-Opening\n" +\
                       "  closing:\n" +\
                       "    - Test-Closing\n"

INVALID_YAML = "file:\n" +\
               "  name: TEST-AUTHORS\n" +\
               "  format: md\n" +\
               "contents:\n" +\
               "  heading: Test-Heading:\n" +\
               "  opening: Test-Opening:\n" +\
               "  closing: Test-Closing:\n"

SETTINGS = dict(
    name="TEST-AUTHORS",
    fformat="md",
    heading="Test-Heading",
    opening="Test-Opening",
    closing="Test-Closing"
)

SETTINGS_DEFAULT_NAME = dict(
    name="AUTHORS",
    fformat="md",
    heading="Test-Heading",
    opening="Test-Opening",
    closing="Test-Closing"
)

SETTINGS_DEFAULT_FORMAT = dict(
    name="TEST-AUTHORS",
    fformat="md",
    heading="Test-Heading",
    opening="Test-Opening",
    closing="Test-Closing"
)

SETTINGS_DEFAULT_HEADING = dict(
    name="TEST-AUTHORS",
    fformat="md",
    heading="Authors",
    opening="Test-Opening",
    closing="Test-Closing"
)

SETTINGS_DEFAULT_OPENING = dict(
    name="TEST-AUTHORS",
    fformat="md",
    heading="Test-Heading",
    opening="Thank you to all of our contributors.",
    closing="Test-Closing"
)

SETTINGS_DEFAULT_CLOSING = dict(
    name="TEST-AUTHORS",
    fformat="md",
    heading="Test-Heading",
    opening="Test-Opening",
    closing="This project would not be possible without you."
)

CONTENTS_MD = "# Test-Heading\n" +\
              "\n" +\
              "Test-Opening\n" +\
              "\n" +\
              "- author-a\n" +\
              "- Author-B\n" +\
              "- author-c\n" +\
              "\n" +\
              "Test-Closing\n"

CONTENTS_HTML = "<!doctype html>\n" +\
                "<html lang=\"en\">\n" +\
                "  <head>\n" +\
                "    <meta charset=\"utf-8\">\n" +\
                "    <title>Authors</title>\n" +\
                "  </head>\n" +\
                "  <body>\n" +\
                "    <h1>Test-Heading</h1>\n" +\
                "    <p>Test-Opening</p>\n" +\
                "    <ul>\n" +\
                "      <li>author-a</li>\n" +\
                "      <li>Author-B</li>\n" +\
                "      <li>author-c</li>\n" +\
                "    </ul>\n" +\
                "    <p>Test-Closing</p>\n" +\
                "  </body>\n" +\
                "</html>\n"

CONTENTS_RST = "Test-Heading\n" +\
               "==============================\n" +\
               "\n" +\
               "Test-Opening\n" +\
               "\n" +\
               "- author-a\n" +\
               "- Author-B\n" +\
               "- author-c\n" +\
               "\n" +\
               "Test-Closing\n"

SOURCE = (
    "",
    "\n",
    "author-c",
    "Author-B",
    "author-a",
    "",
    "\n",
    "author-c",
    "Author-B",
    "author-a"
)
