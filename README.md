[![Build Status](https://travis-ci.com/critical-path/authors.svg?branch=master)](https://travis-ci.com/critical-path/authors) [![Coverage Status](https://coveralls.io/repos/github/critical-path/authors/badge.svg)](https://coveralls.io/github/critical-path/authors)

## authors v0.1.0

Create an `AUTHORS` file to thank the people who contribute to your Git/GitHub project.


## Dependencies

authors requires Python 3.x and the pip package.  It also requires the following packages for usage and testing.

__Usage__:
- click
- Jinja2
- PyYAML

__Testing__:
- coveralls
- pytest
- pytest-cov
- radon


## Installing authors with test cases and testing dependencies

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command and the `--editable` option.

```
sudo pip install --editable .[test]
```


## Installing authors without test cases or testing dependencies

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command.

```
sudo pip install .
```


## Using authors with arguments

From any directory, run `authors` with one or more arguments, where each argument is the name of someone who has contributed to your project.  The result will be an `AUTHORS` file containing the names that you provide.

```
authors first-author second-author third-author nth-author
```


## Using authors with standard input (preferred method)

From your project's working directory (the directory in which the `.git` sub-directory resides), run `git` with the `log` command and the `--format` option, redirecting the standard output to `authors`.  The result will be an `AUTHORS` file that contains the names found in your commit log.

```
git log --format=%an | authors
```

## Configuring authors with .authors.yml

To configure authors, place a file named `.authors.yml` in your project's working directory.  A sample is below:

```
file:
  name: AUTHORS
  format: md
contents:
  heading: Authors
  opening: Thank you to all of our contributors.
  closing: This project would not be possible without you.
```

`name` - The name of the file created by authors (default: `AUTHORS`).

`format` - The format of the file created by authors, where `html`, `md`, and `rst` are valid values (default: `md`).

`heading` - The heading string (default: `Authors`).

`opening` - The opening string (default: `Thank you to all of our contributors.`).

`closing` - The closing string (default: `This project would not be possible without you.`).

authors does not require `.authors.yml`.  If authors cannot find, open, or parse `.authors.yml`, or if authors detects any missing or invalid values, then it will use default values.


## Testing authors after installation

1. Run `radon` with the `mi` command and the `--show` option.

```
radon mi --show authors
```

2. Run `pytest` with the `-vv`, `--cov`, and `--cov-report` options.

```
pytest -vv --cov --cov-report=term-missing
```

If you modify any of the existing templates, be sure to make the corresponding changes to the test cases.  Otherwise, they will fail.

