#!/usr/bin/env python

"""Test fixtures for Flask-GCM tests."""

import pytest
from flask import Flask


@pytest.fixture(scope='function')
def app():
    """Create an instance of a Flask app."""
    app = Flask(__name__)
    return app


@pytest.fixture
def config():
    """Create a configuration class which can be loaded by a Flask app."""
    class Config:
        GCM_KEY = 'super secret'
        GCM_URL = 'gcm url'
        GCM_PROXY = 'gcm proxy'
    return Config
