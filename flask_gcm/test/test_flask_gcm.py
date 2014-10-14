#!/usr/bin/env python

"""Tests for Flask-GCM package"""

from flask.ext.gcm import GCM
from gcm.gcm import GCM_URL


class TestFlaskGCM:
    def test_create_new_gcm(self, app):
        gcm = GCM(app)

        # If not specified, should use defalult URL from python-gcm
        assert gcm.url == GCM_URL

        # Passing app to constructor should link GCM and app object
        assert gcm.app == app
        assert app.extensions['gcm'] == gcm

    def test_create_new_gcm_copies_settings(self, app, config):
        app.config.from_object(config)
        gcm = GCM(app)

        assert gcm.api_key == app.config['GCM_KEY']
        assert gcm.url == app.config['GCM_URL']
        assert gcm.proxy == app.config['GCM_PROXY']

    def test_create_gcm_with_app_factory(self, app):
        gcm = GCM()

        # http://flask.pocoo.org/docs/0.10/extensiondev/#the-extension-code
        # If app object is not passed to constructor, the extension should
        # not store it.
        assert gcm.app is None

        gcm.init_app(app)

        assert app.extensions['gcm'] == gcm

    def test_create_gcm_with_app_factory_copies_settings(self, app, config):
        app.config.from_object(config)
        gcm = GCM()
        gcm.init_app(app)

        assert gcm.api_key == app.config['GCM_KEY']
        assert gcm.url == app.config['GCM_URL']
        assert gcm.proxy == app.config['GCM_PROXY']
