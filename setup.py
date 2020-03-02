import setuptools


setuptools.setup(
    name="authors",
    version="0.3.1",
    description="Thank the people who contribute to your Git/GitHub project by creating an AUTHORS file.",
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
    keywords="thank authors contributors git github",
    packages=setuptools.find_packages(),
    package_data={
        "authors": [
            "templates/template.html",
            "templates/template.md",
            "templates/template.rst",
            "templates/template.txt"
        ]
    },
    install_requires=[
        "Jinja2",
        "PyYAML"
    ],
    extras_require={
        "test": [
            "coveralls",
            "flake8",
            "pytest",
            "pytest-cov"
        ]
    },
    entry_points={
        "console_scripts": [
            "authors=authors:main"
        ]
    }
)
