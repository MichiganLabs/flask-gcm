#!/usr/bin/env python

"""Tests for Flask-GCM package"""

from flask.ext.gcm import GCM, GCM_URL


class TestFlaskGCM:
    def test_create_new_gcm(self, app):
        app.config['GCM_URL'] = None
        gcm = GCM(app)

        # If not specified, should use defalult URL from python-gcm
        assert gcm.url == GCM_URL

        # Passing app to constructor should link GCM and app object
        assert gcm.app == app
        assert app.extensions['gcm'] == gcm

    def test_create_new_gcm_copies_settings(self, app):
        gcm = GCM(app)

        assert gcm.api_key == app.config['GCM_KEY']
        assert gcm.url == app.config['GCM_URL']

    def test_create_gcm_with_app_factory(self, app):
        gcm = GCM()

        # http://flask.pocoo.org/docs/0.10/extensiondev/#the-extension-code
        # If app object is not passed to constructor, the extension should
        # not store it.
        assert gcm.app is None
        gcm.init_app(app)
        assert gcm.app is None

        assert app.extensions['gcm'] == gcm

    def test_create_gcm_with_app_factory_copies_settings(self, app):
        gcm = GCM()
        gcm.init_app(app)

        assert gcm.api_key == app.config['GCM_KEY']
        assert gcm.url == app.config['GCM_URL']

    def test_gcm_registers_on_extensions(self, app):
        gcm = GCM(app)
        assert app.extensions['gcm'] == gcm

    def test_gcm_registers_on_extensions_with_init_app(self, app):
        gcm = GCM()
        gcm.init_app(app)
        assert app.extensions['gcm'] == gcm
