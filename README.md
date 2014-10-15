# Flask-GCM

[![Build Status][travis-badge]][travis-status]
[![Coverage Status][coveralls-badge]][coverage-status]
[![PyPI Version][pypi-version-badge]][pypi-page]
[![PyPI Downloads][pypi-downloads-badge]][pypi-page]

Flask-GCM is a simple wrapper for the [`gcm-client`][gcm-client] library to be used with [Flask][flask] applications.

## Getting Started

### Requirements

* Python 2.6+ or Python 3.3+

### Installation

Flask-GCM can be installed with pip:

```
$ pip install flask-gcm
```

or directly from the source code:

```
$ git clone https://github.com/MichiganLabs/flask-gcm.git
$ cd flask-gcm
$ python setup.py install
```

### Basic Usage

```python
from flask import Flask
from flask.ext.gcm import GCM

app = Flask(__name__)
gcm = GCM(app)
```

Flask-GCM also supports the Flask ["app factory"][app-factories] paradigm using `init_app`:

```python
from flask import Flask
from flask.ext.gcm import GCM

gcm = GCM()

def create_app():
    app = Flask(__name__)
    gcm.init_app(app)
    return app
```

The `gcm` object can then be used as described in the [`gcm-client` docs][gcm-client-docs]

## For Contributors

### Requirements

* GNU Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation

### Installation

Create a virtualenv:

```
$ make env
```

Run the tests:

```
$ make test
```

Build the documentation:

```
$ make doc
```

Run static analysis:

```
$ make flake8
$ make pep257
$ make check  # includes all checks
```

### Pull Request Guidelines

Contributions are always welcome! Please keep the following in mind when creating a pull request:

* Include (passing) tests for all new features and bugfixes
* Contributed code should pass `flake8` checks
* Include documentation which passes `pep257` guidelines

[travis-badge]: http://img.shields.io/travis/MichiganLabs/flask-gcm/master.svg
[travis-status]: https://travis-ci.org/MichiganLabs/flask-gcm
[coveralls-badge]: http://img.shields.io/coveralls/MichiganLabs/flask-gcm/master.svg
[coverage-status]: https://coveralls.io/r/MichiganLabs/flask-gcm
[pypi-version-badge]: http://img.shields.io/pypi/v/flask-gcm.svg
[pypi-downloads-badge]: http://img.shields.io/pypi/dm/flask-gcm.svg
[pypi-page]: https://pypi.python.org/pypi/flask-gcm
[app-factories]: http://flask.pocoo.org/docs/0.10/patterns/appfactories/
[gcm-client]: https://pypi.python.org/pypi/gcm-client/
[flask]: http://flask.pocoo.org/
[gcm-client-docs]: http://gcm-client.readthedocs.org/en/latest/index.html
