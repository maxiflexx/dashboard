import json
from typing import Any, Dict, Optional, Union

import requests

from src.core.settings.config import settings


class ApiClient:
    def __init__(
        self,
        *,
        base_url: str,
        headers: Dict[str, str] = {},
        timeout: int = 30 * 1000,
        max_body_length: int = 2 * 1024 * 1024,
    ):
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout
        self.max_body_length = max_body_length

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Union[str, bytes]] = None,
    ):
        url: str = f"{self.base_url}{path}"

        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                params=params,
                json=data,
                timeout=self.timeout / 1000,  # Convert milliseconds to seconds
            )

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            error = e.response.json()
            raise BaseException(error)

    def get_json(
        self,
        path: str,
        query: Optional[Dict[str, Any]] = None,
    ):
        return self._request("GET", path, params=query)

    def delete_json(
        self,
        path: str,
        query: Optional[Dict[str, Any]] = None,
    ):
        return self._request("DELETE", path, params=query)

    def post_json(
        self,
        path: str,
        body: Optional[Dict[str, Any]] = None,
    ):
        return self._request("POST", path, data=body)

    def put_json(
        self,
        path: str,
        body: Optional[Dict[str, Any]] = None,
    ):
        return self._request("PUT", path, data=body)


data_io_client = ApiClient(base_url=f"{settings.data_io_schema}://{settings.data_io_host}:{settings.data_io_port}")
