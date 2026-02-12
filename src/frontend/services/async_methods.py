import asyncio


class AsyncMethods:

    @staticmethod
    def async_reg_account(window):
        try:
            asyncio.run(window.register_account())
        except Exception as e:
            print(f"Erro ao cadastrar registro: {e}")

    @staticmethod
    def async_login_account(window):
        try:
            asyncio.run(window.login_token())
        except Exception as e:
            print(f"Erro ao fazer login: {e}")

    @staticmethod
    def async_get_materials(window):
        try:
            asyncio.run(window.get_materials())
        except Exception as e:
            print(f"Erro ao listar materiais: {e}")

    @staticmethod
    def async_post_materials(window):
        try:
            asyncio.run(window.post_material())
            AsyncMethods.async_get_materials(window)
        except Exception as e:
            print(f"Erro ao cadastrar material: {e}")

    @staticmethod
    def async_refresh_quant(window):
        try:
            asyncio.run(window.refresh_quant())
        except Exception as e:
            print(e)
