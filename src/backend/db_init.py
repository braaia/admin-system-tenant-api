from sqlalchemy import MetaData
from sqlalchemy.schema import CreateSchema

from backend.models import models as tenant_models
from backend.database import engine, Base, with_db
from backend.models.tenant import Tenant


def get_shared_metadata():
    meta = MetaData(schema="shared")
    for table in Base.metadata.tables.values():
        if table.schema == "shared":
            table.tometadata(meta)
    return meta


def get_tenant_specific_metadata():
    meta = MetaData(schema="tenant")
    for table in Base.metadata.tables.values():
        if table.schema == "tenant":
            table.tometadata(meta)
    return meta


def init_database():
    # Cria schema shared + tabelas shared
    with engine.begin() as conn:
        conn.execute(CreateSchema("shared", if_not_exists=True))
        get_shared_metadata().create_all(bind=conn)


def create_tenant(name: str, schema: str, host: str) -> None:
    # Verifica migrations no schema do tenant (comentado pois schemas já existem)
    # with with_db(schema) as db:
    #     context = MigrationContext.configure(db.connection())
    #     alembic_ini_path = os.path.join(os.path.dirname(__file__), "..", "alembic.ini")
    #     alembic_config = AlembicConfig(alembic_ini_path)
    #     script = alembic.script.ScriptDirectory.from_config(alembic_config)
    #     if context.get_current_revision() != script.get_current_head():
    #         raise RuntimeError(
    #             "Database is not up-to-date. Execute migrations before adding new tenants."
    #         )

    # Adiciona o tenant no schema shared
    with with_db("shared") as db_shared:
        tenant = db_shared.query(Tenant).filter(
            (Tenant.schema == schema) | (Tenant.host == host)
        ).one_or_none()
        if tenant is None:
            tenant = Tenant(
                name=name,
                host=host,
                schema=schema,
            )
            db_shared.add(tenant)
            db_shared.commit()

        # Cria schema se não existir
        from sqlalchemy import text
        result = db_shared.execute(
            text("SELECT schema_name FROM information_schema.schemata WHERE schema_name = :schema"), {"schema": schema})
        if not result.fetchone():
            db_shared.execute(CreateSchema(schema, if_not_exists=True))
            db_shared.commit()

        # Cria tabelas no schema do tenant (idempotente)
        connectable = engine.execution_options(schema_translate_map={"tenant": schema})
        with connectable.begin() as conn:
            get_tenant_specific_metadata().create_all(bind=conn)

        db_shared.commit()
