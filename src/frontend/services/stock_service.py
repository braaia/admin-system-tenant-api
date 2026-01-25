from .api_client import ApiClient


class EstoqueService:
    admin_prefix = "/admin"
    auth_prefix = "/auth-usuarios-adm"
    material_prefix = "/estoque-materiais"

    # region ALL TENANTS
    @staticmethod
    async def register_account(data):
        return await ApiClient.post("usuarios", f"{EstoqueService.auth_prefix}/sign-up", data)

    @staticmethod
    async def login_account(data):
        return await ApiClient.post("usuarios", f"{EstoqueService.auth_prefix}/login", data)

    @staticmethod
    async def listar_materiais(tenant):
        return await ApiClient.get(tenant, f"{EstoqueService.material_prefix}/listar-materiais")

    @staticmethod
    async def cadastrar_material(tenant, data):
        return await ApiClient.post(tenant, f"{EstoqueService.material_prefix}/cadastrar-material", data)
    # endregion


    # region Cícero Gomes - Cliente 0
    @staticmethod
    async def listar_entradas(tenant):
        return await ApiClient.get(tenant, f"{EstoqueService.material_prefix}/listar-entrada")
    @staticmethod
    async def listar_saidas(tenant):
        return await ApiClient.get(tenant, f"{EstoqueService.material_prefix}/listar-saida")
    # endregion