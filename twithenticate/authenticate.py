#-------------------------------------------------------------------------------
# Name:        authenticate.py
#
# Purpose:     A Python implementation of Twitter's Application-only
#              authentication.
#
#              The Requests module(http://docs.python-requests.org/en/latest/)
#              is required for this implementation to work
#
# Author:      Ken Tong, @kenwtong
#
# Created:     27/11/2014
#-------------------------------------------------------------------------------
import base64
import requests

def encode_credentials(consumer_key, consumer_secret):
    """
        Generate an encoded bearer token to access the Twitter REST API.

        Input:

        consumer_key: consumer key provided by your Twitter application created
            at http://apps.twitter.com.

        consumer_secret: consumer secret provided by your Twitter application
            created at http://apps.twitter.com.
    """
    return base64.b64encode(':'.join([consumer_key, consumer_secret]))


def get_access_token(encoded_credentials):
    """
        Get the bearer token payload (JSON) from the Twitter Application only
        authentication URL.

        Function should not be called directly. It is used internally by the
        get_access_token function.

        Input:

        encoded_credentials: base64 encoded token.
    """
    APP_ONLY_AUTHENTICATION_URL = 'https://api.twitter.com/oauth2/token'
    headers = {
        'content-type' : 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization' : 'Basic {0}'.format(encoded_credentials)
    }
    data = 'grant_type=client_credentials'

    return requests.post(APP_ONLY_AUTHENTICATION_URL,
                         headers=headers,
                         data=data).json()['access_token']