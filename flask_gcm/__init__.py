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
__PATCH__ = 0
__version__ = '{}.{}.{}'.format(__MAJOR__, __MINOR__, __PATCH__)
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
