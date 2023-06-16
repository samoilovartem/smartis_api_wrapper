from http import HTTPStatus
from typing import Any

import requests

from core.config import config


class SmartisAPI:
    """
    The Smartis API base class for making requests to the Smartis API.
    """

    def __init__(self, api_key: str, base_url: str = config.base_url):
        """
        Initiate the SmartisAPI class.

        Parameters:
        api_key (str): API key for authentication (required).
        base_url (str): Base URL for the API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def make_request(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
    ) -> dict[str, Any] | None:
        """
        Make a request to the API.

        Parameters:
        endpoint (str): The endpoint of the API to make the request to.
        params (dict): Parameters to pass to the endpoint (Optional).
        data (dict): Data to pass to the endpoint (Optional).

        Returns:
        dict: The response from the API as a dictionary.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        url = f'{self.base_url}{endpoint}'
        response = requests.post(url, params=params, json=data, headers=headers)

        self.handle_http_errors(response)

        if response.text:
            return response.json()
        else:
            return None

    @staticmethod
    def handle_http_errors(response: requests.Response) -> None:
        """
        Handle HTTP errors.

        Parameters:
        response: The response object to check for errors.

        Raises:
        Exception: If the response contains a HTTP error status code.
        """
        status_code_to_message = {
            HTTPStatus.BAD_REQUEST: 'Bad Request. Please check your request data.',
            HTTPStatus.UNAUTHORIZED: 'Unauthorized. Please check your API key.',
            HTTPStatus.FORBIDDEN: 'Forbidden. You do not have the necessary permissions.',
            HTTPStatus.UNPROCESSABLE_ENTITY: 'Unprocessable Entity. The server was unable to process the contained '
            'instructions.',
            HTTPStatus.INTERNAL_SERVER_ERROR: 'Internal Server Error. The server encountered an error.',
        }
        if HTTPStatus(response.status_code) in status_code_to_message:
            raise Exception(
                f'Error {response.status_code}: {status_code_to_message[HTTPStatus(response.status_code)]}'
            )
