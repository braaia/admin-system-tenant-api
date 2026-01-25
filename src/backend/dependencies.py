from fastapi import Depends, Request, HTTPException

from backend.database import with_db
from backend.models.tenant import Tenant


def get_tenant(req: Request) -> Tenant:
    host = (req.headers.get("host") or "").split(":", 1)[0].lower()
    if not host:
        raise HTTPException(status_code=400, detail="Missing Host header")

    # Conecta ao schema shared para acessar a tabela tenants
    with with_db("shared") as db:
        tenant = db.query(Tenant).filter(Tenant.host == host).one_or_none()

    if tenant is None:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant


def get_db(tenant: Tenant = Depends(get_tenant)):
    with with_db(tenant.schema) as db:
        yield db
