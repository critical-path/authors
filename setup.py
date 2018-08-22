from setuptools import (
    find_packages,
    setup
)

setup(
    name="authors",
    version="0.1.0",
    description="Create an AUTHORS file to thank the people who contribute to your Git/GitHub project.",
    url="https://github.com/critical-path/authors",
    author="critical-path",
    author_email="n/a",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    keywords="authors thank contribute contributor contribution git github",
    packages=find_packages(),
    package_data={
        "authors": [
            "templates/template.html",
            "templates/template.md",
            "templates/template.rst"
        ]
    },
    install_requires=[
        "click",
        "Jinja2",
        "PyYAML"
    ],
    extras_require={
        "test": [
            "coveralls",
            "pytest",
            "pytest-cov"
        ]
    },
    entry_points={
        "console_scripts": [
            "authors=authors.cli:thank_authors"
        ]
    }
)
