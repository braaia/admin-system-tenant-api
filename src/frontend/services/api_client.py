from typing import Optional

import httpx
from decouple import config


class ApiClient:
    HTTP_SCHEME = config("API_SCHEME", default="https")
    BASE_DOMAIN = config("API_BASE_DOMAIN", default="admin-system-tenant-2vscxmjdf-wesleys-projects-abf53e5c.vercel.app")
    BASE_PORT = config("API_PORT", default="5001")
    TENANT_MODE = config("API_TENANT_MODE", default="header")
    _token: Optional[str] = None
    _role: Optional[str] = None
    _tenant: Optional[str] = None
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
    def _resolve_tenant(cls, tenant: Optional[str]) -> Optional[str]:
        return tenant or cls._tenant

    @classmethod
    def _get_headers(cls, tenant: Optional[str]) -> dict:
        """Retorna headers com autenticacao se token estiver configurado"""
        headers = {}
        if cls._token:
            headers["Authorization"] = f"Bearer {cls._token}"
        tenant_value = cls._resolve_tenant(tenant)
        if tenant_value and cls.TENANT_MODE == "header":
            headers["X-Tenant"] = tenant_value
        return headers

    @classmethod
    def _build_base_url(cls, tenant: Optional[str]) -> str:
        host = cls.BASE_DOMAIN
        tenant_value = cls._resolve_tenant(tenant)
        if cls.TENANT_MODE == "subdomain" and tenant_value:
            host = f"{tenant_value}.{cls.BASE_DOMAIN}"
        return f"{cls.HTTP_SCHEME}://{host}"

    @classmethod
    def _build_url(cls, tenant: Optional[str], endpoint: str) -> str:
        tenant_value = cls._resolve_tenant(tenant)
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"
        base_url = cls._build_base_url(tenant_value)
        if cls.TENANT_MODE == "path" and tenant_value:
            return f"{base_url}/t/{tenant_value}{endpoint}"
        return f"{base_url}{endpoint}"

    @staticmethod
    async def get(tenant: Optional[str], endpoint: str, headers: dict = None):
        """GET request"""
        async with httpx.AsyncClient(timeout=ApiClient._timeout) as client:
            merged_headers = ApiClient._get_headers(tenant)
            if headers:
                merged_headers.update(headers)

            response = await client.get(
                ApiClient._build_url(tenant, endpoint),
                headers=merged_headers
            )
            response.raise_for_status()
            return response.json() if response.content else None

    @staticmethod
    async def post(tenant: Optional[str], endpoint: str, data: dict, headers: dict = None):
        """POST request"""
        async with httpx.AsyncClient(timeout=ApiClient._timeout) as client:
            merged_headers = ApiClient._get_headers(tenant)
            if headers:
                merged_headers.update(headers)

            response = await client.post(
                ApiClient._build_url(tenant, endpoint),
                json=data,
                headers=merged_headers
            )
            response.raise_for_status()
            return response.json() if response.content else None

    @staticmethod
    async def put(tenant: Optional[str], endpoint: str, data: dict, headers: dict = None):
        """PUT request"""
        async with httpx.AsyncClient(timeout=ApiClient._timeout) as client:
            merged_headers = ApiClient._get_headers(tenant)
            if headers:
                merged_headers.update(headers)

            response = await client.put(
                ApiClient._build_url(tenant, endpoint),
                json=data,
                headers=merged_headers
            )
            response.raise_for_status()
            return response.json() if response.content else None

    @staticmethod
    async def patch(tenant: Optional[str], endpoint: str, data: dict = None, headers: dict = None):
        """PATCH request"""
        async with httpx.AsyncClient(timeout=ApiClient._timeout) as client:
            merged_headers = ApiClient._get_headers(tenant)
            if headers:
                merged_headers.update(headers)

            response = await client.patch(
                ApiClient._build_url(tenant, endpoint),
                json=data,
                headers=merged_headers
            )
            response.raise_for_status()
            return response.json() if response.content else None

    @staticmethod
    async def delete(tenant: Optional[str], endpoint: str, headers: dict = None):
        """DELETE request"""
        async with httpx.AsyncClient(timeout=ApiClient._timeout) as client:
            merged_headers = ApiClient._get_headers(tenant)
            if headers:
                merged_headers.update(headers)

            response = await client.delete(
                ApiClient._build_url(tenant, endpoint),
                headers=merged_headers
            )
            response.raise_for_status()
            return response.json() if response.content else None
