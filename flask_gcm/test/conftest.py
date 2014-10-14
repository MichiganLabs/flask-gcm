#!/usr/bin/env python

"""Test fixtures for Flask-GCM tests."""

import pytest
from flask import Flask


@pytest.fixture
def config():
    """Create a configuration class which can be loaded by a Flask app."""
    class Config:
        GCM_KEY = 'super secret'
        GCM_URL = 'http://foobar.com'
    return Config


@pytest.fixture(scope='function')
def app(config):
    """Create an instance of a Flask app."""
    app = Flask(__name__)
    app.config.from_object(config)
    return app
