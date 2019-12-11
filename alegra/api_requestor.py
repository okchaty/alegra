import alegra
import base64

from requests import request


class APIRequestor(object):
    def __init__(self, user=None, token=None, api_base=None, api_version=None):
        self.user = user or alegra.user
        self.token = token or alegra.token
        self.api_base = api_base or alegra.api_base
        self.api_version = api_version or alegra.api_version
        self.api_url = "{}/{}".format(self.api_base, self.api_version)

    def authorization_header(self):
        """Returns authorization header."""
        user_token = "{}:{}".format(self.user, self.token).encode()
        authorization_code = base64.b64encode(user_token).decode("utf-8")
        return "Basic {}".format(authorization_code)
    
    def request(self, method, url, **kwargs):
        """Injects auth headers."""
        headers = {
            "Authorization": self.authorization_header(),
            "content-type": "application/json",
        }
        headers.update(kwargs.pop("headers", {}))  # Updates headers.
        # More info:
        # https://requests.readthedocs.io/en/master/api/#requests.request
        return request(
            method,
            url="{}/{}".format(self.api_url, url),
            headers=headers,
            **kwargs
        )
