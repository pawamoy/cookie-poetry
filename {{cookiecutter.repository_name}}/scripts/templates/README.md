<!--
IMPORTANT:
  This file is generated from the template at 'scripts/templates/README.md'.
  Please update the template instead of this file.
-->

# {{ cookiecutter.project_name }}
[![pipeline status](https://{{ cookiecutter.repository_provider }}/{{ cookiecutter.repository_namespace }}/{{ cookiecutter.repository_name }}/badges/master/pipeline.svg)](https://{{ cookiecutter.repository_provider }}/{{ cookiecutter.repository_namespace }}/{{ cookiecutter.repository_name }}/commits/master)
[![coverage report](https://{{ cookiecutter.repository_provider }}/{{ cookiecutter.repository_namespace }}/{{ cookiecutter.repository_name }}/badges/master/coverage.svg)](https://{{ cookiecutter.repository_provider }}/{{ cookiecutter.repository_namespace }}/{{ cookiecutter.repository_name }}/commits/master)
[![documentation](https://img.shields.io/readthedocs/{{ cookiecutter.repository_name }}.svg?style=flat)](https://{{ cookiecutter.repository_name }}.readthedocs.io/en/latest/index.html)
[![pypi version](https://img.shields.io/pypi/v/{{ cookiecutter.repository_name }}.svg)](https://pypi.org/project/{{ cookiecutter.repository_name }}/)

{{ cookiecutter.project_description }}

## Requirements
{{ cookiecutter.project_name }} requires Python 3.6 or above.

<details>
<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.6
pyenv install 3.6.8

# make it available globally
pyenv global system 3.6.8
```
</details>

## Installation
With `pip`:
```bash
python3.6 -m pip install {{ cookiecutter.python_package_distribution_name }}
```

With [`pipx`](https://github.com/cs01/pipx):
```bash
# install pipx with the recommended method
curl https://raw.githubusercontent.com/cs01/pipx/master/get-pipx.py | python3

pipx install --python python3.6 {{ cookiecutter.python_package_distribution_name }}
```

## Usage (as a library)
TODO

## Usage (command-line)
```
{{ command_line_help }}
```

Commands:
{% for command in commands %}
- [`{{ command.name }}`](#{{ command.name }}){% endfor %}

{% for command in commands %}
### `{{ command.name }}`
```
{{ command.help }}
```

{% include "command_" + command.name.replace("-", "_") + "_extra.md" ignore missing %}
{% endfor %}
