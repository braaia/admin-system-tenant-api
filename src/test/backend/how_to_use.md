Atualizei o backend para suportar roles leves (cargo em token) e adicionei a dependência de autorização. O que foi mudado (arquivos editados):

* [authHandler.py](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — inclui [cargo](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) no payload do JWT.
* [schemas.py](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — [UsuariosWithToken](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) agora contém [cargo](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html).
* [userService.py](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — gera token com [cargo](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) e retorna [cargo](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) no login.
* [protectedRoute.py](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — nova factory [require_roles(*roles)](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) para usar como dependency.
* [userRepo.py](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — normalizei o [cargo](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) default para [&#34;user&#34;](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html).

Como usar (exemplos rápidos)

* Proteger rota no FastAPI:
  * Dependência direta:
    * from backend.security.util.protectedRoute import require_roles
    * @router.get("/admin")
      def admin_panel(current_user: UsuariosOut = Depends(require_roles("admin"))):
      ...
  * Ou via [dependencies](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) no decorator:
    * @router.get("/manage", dependencies=[Depends(require_roles("manager","admin"))])
* Login / frontend (Flet)
  * O endpoint de login retorna [token](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) e [cargo](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html). No Flet, guarde o token (ex: local file/secure storage) e use o campo [cargo](vscode-file://vscode-app/c:/Users/Braia/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html) para condicionar UI:
    * if user['cargo'] == "admin": mostrar painel admin
    * else: esconder ações administrativas
