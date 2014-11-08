#!/usr/bin/env python

"""Flask-GCM wrapper for python-gcm."""

from gcmclient import (
    GCM as _GCM,
    GCMAuthenticationError,
    JSONMessage,
    PlainTextMessage,
    Result,
)
from gcmclient.gcm import GCM_URL


# Version info
__project__ = 'Flask-GCM'
__MAJOR__ = 0
__MINOR__ = 2
__PATCH__ = 0
__version__ = '{0}.{1}.{2}'.format(__MAJOR__, __MINOR__, __PATCH__)
VERSION = __project__ + '-' + __version__


# Define what gets imported when using `from flask_gcm import *`
__all__ = ('GCMAuthenticationError',
           'JSONMessage',
           'PlainTextMessage',
           'GCM',
           'Result')


class GCM(_GCM):

    """Convenience wrapper class for GCM library."""

    def __init__(self, app=None, **kwargs):
        """Initialize the GCM object with flask app settings."""
        self.app = app
        if self.app:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        """Initialize the GCM object with flask app settings."""
        # Configure default GCM settings
        app.config.setdefault('GCM_URL', GCM_URL)
        app.config.setdefault('GCM_KEY', None)

        # Hard limit in GCM API:
        # http://developer.android.com/training/cloudsync/gcm.html
        app.config.setdefault('GCM_MAX_DEVICES_PER_REQUEST', 1000)

        # Configure GCM from app settings
        self.url = app.config.get('GCM_URL') or GCM_URL
        self.api_key = app.config.get('GCM_KEY')

        # Register GCM on app extensions
        if not hasattr(app, 'extensions'):  # pragma: no cover
            # For older versions of Flask before 0.7
            app.extensions = {}
        app.extensions['gcm'] = self

        # init python-gcm object
        super(self.__class__, self).__init__(self.api_key, url=self.url,
                                             **kwargs)
