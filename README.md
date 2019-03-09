# Cookie Poetry

<!-- badge list -->
Cookiecutter for Poetry projects.

This cookiecutter is mainly for my own usage,
but feel free to try it out, or fork it!

<!-- logo -->

- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Features](#features)
- [License: ISC License](LICENSE)
- [Requirements](#requirements)
- [Usage](#usage)
- [Credits](#credits)

## Features
- [Poetry](https://github.com/sdispater/poetry) setup, with pre-defined `pyproject.toml`
- Documentation built with Sphinx, in Markdown and/or reStructuredText
- Pre-configured tools: black, isort, bandit, safety
- Tests run with pytest (and plugins), with coverage
- Gitlab CI configuration (no Travis CI)
- Python 3.6 or above
- Auto-generated CREDITS.md from Python dependencies
- All licenses from [choosealicense.com](https://choosealicense.com/appendix/)
- Convenience Makefile

## Requirements
- [git](https://git-scm.com/downloads)
- [python](https://www.python.org/downloads/)
- [cookiecutter](https://github.com/audreyr/cookiecutter)

## Usage
```
cookiecutter gh:pawamoy/cookie-poetry
```

## Credits
This cookiecutter was created with [cookiecutter-cookiecutter](https://github.com/pawamoy/cookiecutter-cookiecutter).
