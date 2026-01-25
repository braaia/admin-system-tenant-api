from typing import Optional

import httpx
from decouple import config


class ApiClient:
    HTTP_SCHEME = config("API_SCHEME", default="http")
    BASE_DOMAIN = config("API_BASE_DOMAIN", default="localhost")
    BASE_PORT = config("API_PORT", default="8000")
    _token: Optional[str] = None
    _role: Optional[str] = None
    _tenant: Optional[str] = "usuarios"
    _timeout = config("API_TIMEOUT", default=10.0, cast=float)

    @classmethod
    def set_tenant(cls, tenant: str) -> None:
        """Define o tenant para as requisicoes"""
        cls._tenant = tenant

    @classmethod
    def set_token(cls, token: dict) -> None:
        """Define o token JWT para autenticacao"""
        cls._token = token["token"]
        cls._role = token["cargo"]
        cls._tenant = token["tenant_schema"]

    @classmethod
    def get_token(cls) -> Optional[str]:
        return cls._token

    @classmethod
    def get_role(cls) -> Optional[str]:
        return cls._role

    @classmethod
    def get_tenant(cls) -> Optional[str]:
        return cls._tenant

    @classmethod
    def clear_token(cls) -> None:
        """Remove o token JWT"""
        cls._token = None

    @classmethod
    def _get_headers(cls) -> dict:
        """Retorna headers com autenticacao se token estiver configurado"""
        headers = {}
        if cls._token:
            headers["Authorization"] = f"Bearer {cls._token}"
        return headers

    @classmethod
    def _build_base_url(cls, tenant: Optional[str]) -> str:
        host = cls.BASE_DOMAIN
        if tenant:
            host = f"{tenant}.{cls.BASE_DOMAIN}"
        return f"{cls.HTTP_SCHEME}://{host}:{cls.BASE_PORT}"

    @staticmethod
    async def get(tenant: str, endpoint: str, headers: dict = None):
        """GET request"""
        async with httpx.AsyncClient(timeout=ApiClient._timeout) as client:
            merged_headers = ApiClient._get_headers()
            if headers:
                merged_headers.update(headers)

            base_url = ApiClient._build_base_url(tenant)
            response = await client.get(
                f"{base_url}{endpoint}",
                headers=merged_headers
            )
            response.raise_for_status()
            return response.json() if response.content else None

    @staticmethod
    async def post(tenant: str, endpoint: str, data: dict, headers: dict = None):
        """POST request"""
        async with httpx.AsyncClient(timeout=ApiClient._timeout) as client:
            merged_headers = ApiClient._get_headers()
            if headers:
                merged_headers.update(headers)

            base_url = ApiClient._build_base_url(tenant)
            response = await client.post(
                f"{base_url}{endpoint}",
                json=data,
                headers=merged_headers
            )
            response.raise_for_status()
            return response.json() if response.content else None

    @staticmethod
    async def put(tenant: str, endpoint: str, data: dict, headers: dict = None):
        """PUT request"""
        async with httpx.AsyncClient(timeout=ApiClient._timeout) as client:
            merged_headers = ApiClient._get_headers()
            if headers:
                merged_headers.update(headers)

            base_url = ApiClient._build_base_url(tenant)
            response = await client.put(
                f"{base_url}{endpoint}",
                json=data,
                headers=merged_headers
            )
            response.raise_for_status()
            return response.json() if response.content else None

    @staticmethod
    async def patch(tenant: str, endpoint: str, data: dict = None, headers: dict = None):
        """PATCH request"""
        async with httpx.AsyncClient(timeout=ApiClient._timeout) as client:
            merged_headers = ApiClient._get_headers()
            if headers:
                merged_headers.update(headers)

            base_url = ApiClient._build_base_url(tenant)
            response = await client.patch(
                f"{base_url}{endpoint}",
                json=data,
                headers=merged_headers
            )
            response.raise_for_status()
            return response.json() if response.content else None

    @staticmethod
    async def delete(tenant: str, endpoint: str, headers: dict = None):
        """DELETE request"""
        async with httpx.AsyncClient(timeout=ApiClient._timeout) as client:
            merged_headers = ApiClient._get_headers()
            if headers:
                merged_headers.update(headers)

            base_url = ApiClient._build_base_url(tenant)
            response = await client.delete(
                f"{base_url}{endpoint}",
                headers=merged_headers
            )
            response.raise_for_status()
            return response.json() if response.content else None
