from fastapi import Depends, Request, HTTPException

from backend.database import with_db
from backend.models.tenant import Tenant


def get_tenant(req: Request) -> Tenant:
    tenant_header = (req.headers.get("x-tenant") or "").strip()
    tenant_path = (req.path_params.get("tenant") or "").strip()
    host = (req.headers.get("host") or "").split(":", 1)[0].lower()
    tenant_key = tenant_header or tenant_path

    # Conecta ao schema shared para acessar a tabela tenants
    with with_db("shared") as db:
        if tenant_key:
            tenant = db.query(Tenant).filter(
                (Tenant.schema == tenant_key)
                | (Tenant.name == tenant_key)
                | (Tenant.host == tenant_key)
            ).one_or_none()
        else:
            if not host:
                raise HTTPException(status_code=400, detail="Missing tenant identifier")
            tenant = db.query(Tenant).filter(Tenant.host == host).one_or_none()

    if tenant is None:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant


def get_db(tenant: Tenant = Depends(get_tenant)):
    with with_db(tenant.schema) as db:
        yield db
