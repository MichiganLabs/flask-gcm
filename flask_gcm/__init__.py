#!/usr/bin/env python

"""Flask-GCM wrapper for python-gcm."""

from gcm.gcm import (
    GCM as _GCM,
    GCM_URL,
)

# Import exception classes into the flask_gcm package
from gcm.gcm import (  # NOQA
    GCMException,
    GCMMalformedJsonException,
    GCMConnectionException,
    GCMAuthenticationException,
    GCMTooManyRegIdsException,
    GCMInvalidTtlException,
    GCMMissingRegistrationException,
    GCMMismatchSenderIdException,
    GCMNotRegisteredException,
    GCMMessageTooBigException,
    GCMInvalidRegistrationException,
    GCMUnavailableException,
)

# import other functions into flask_gcm package
from gcm.gcm import group_response, urlencode_utf8  # NOQA


# Version info
__project__ = 'Flask-GCM'
__MAJOR__ = 0
__MINOR__ = 0
__PATCH__ = 1
__version__ = '{0}.{1}.{2}'.format(__MAJOR__, __MINOR__, __PATCH__)
VERSION = __project__ + '-' + __version__


# Define what gets imported when using `from flask_gcm import *`
__all__ = ('GCM',
           'GCMException',
           'GCMMalformedJsonException',
           'GCMConnectionException',
           'GCMAuthenticationException',
           'GCMTooManyRegIdsException',
           'GCMInvalidTtlException',
           'GCMMissingRegistrationException',
           'GCMMismatchSenderIdException',
           'GCMNotRegisteredException',
           'GCMMessageTooBigException',
           'GCMInvalidRegistrationException',
           'GCMUnavailableException',)


class GCM(_GCM):

    """Convenience wrapper class for GCM library."""

    def __init__(self, app=None, api_key=None, url=GCM_URL):
        """Initialize the GCM object with flask app settings."""
        self.app = app
        if self.app:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the GCM object with flask app settings."""
        # Configure default GCM settings
        app.config.setdefault('GCM_URL', GCM_URL)
        app.config.setdefault('GCM_KEY', None)
        app.config.setdefault('GCM_PROXY', None)
        # The following is a limit hard coded into the python-gcm library:
        app.config.setdefault('GCM_MAX_DEVICES_PER_REQUEST', 1000)

        # Configure GCM from app settings
        self.url = app.config.get('GCM_URL')
        self.api_key = app.config.get('GCM_KEY')
        self.proxy = app.config.get('GCM_PROXY')

        # Register GCM on app extensions
        if not hasattr(app, 'extensions'):  # pragma: no cover
            # For older versions of Flask before 0.7
            app.extensions = {}
        app.extensions['gcm'] = self

        # init python-gcm object
        super(self.__class__, self).__init__(self.api_key, url=self.url,
                                             proxy=self.proxy)
