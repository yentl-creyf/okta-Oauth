import logging

import requests


logger = logging.getLogger(__name__)

class OktaOAth:
    def __init__(
        self,
        issuer: str,
        redirect_url: str,
        client_id: str,
        state: str,
        nonce: str,
        secret: str,
        scope: str
    ) -> None:
        self.issuer = issuer
        self.redirect_url = redirect_url
        self.client_id = client_id
        self.state = state
        self.nonce = nonce
        self.secret = secret
        self.scope = scope

    def authenticate_user(self) -> str:
        """
        create the url to start the authentication process
        :return: a url
        """
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_url,
            "scope": self.scope,
            "state": self.state,
            "nonce": self.nonce,
            "response_type": "code",
            "response_mode": "query",
        }
        url = self.issuer + "/v1/authorize"
        logger.debug({"url": url})
        request_url = requests.Request("GET", url, params=params).prepare().url
        return request_url

    def token_request(self, code: str) -> dict:
        """
        request token from okta
        :return: the token from okta
        """
        params = {
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_url,
            "client_id": self.client_id,
            "client_secret": self.secret,
        }
        url = self.issuer + "/v1/token"
        logger.debug({"url": url})
        response = requests.post(url, data=params)

        if not response.ok:
            logger.error("Error occurred while requesting token")
        return response.json()

    def user_info_request(self, access_token: str) -> dict:
        """
        request user info from okta
        :param access_token: the access token to access the user info
        :return: user info from okta
        """
        url = self.issuer + "/v1/userinfo"
        headers = {"Authorization": f"Bearer {access_token}"}
        logger.debug({"url": url})
        response = requests.get(url, headers=headers)

        if not response.ok:
            logger.error("Error occured while requesting user info")
        return response.json()
