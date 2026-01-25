from logging.config import fileConfig

from sqlalchemy import engine_from_config, MetaData
from sqlalchemy import pool, text

from alembic import context
from decouple import config as env_config

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
configuration = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if configuration.config_file_name is not None:
    fileConfig(configuration.config_file_name)

database_url = env_config("DATABASE_URL")
configuration.set_main_option("sqlalchemy.url", database_url)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel


# noinspection PyUnresolvedReferences
from backend.models.models import Usuarios, Material, EntradaMaterial, SaidaMaterial

# target_metadata = mymodel.Base.metadata
from backend.database import Base, naming_convention

target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = configuration.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    translated = MetaData(naming_convention=naming_convention)

    def translate_schema(table, to_schema, constraint, referred_schema):
        # pylint: disable=unused-argument
        return to_schema

    for table in Base.metadata.tables.values():
        table.tometadata(
            translated,
            schema="tenant_default" if table.schema == "tenant" else table.schema,
            referred_schema_fn=translate_schema,
        )

    connectable = engine_from_config(
        configuration.get_section(configuration.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS tenant_default"))

        context.configure(
            connection=connection,
            target_metadata=translated,
            compare_type=True,
            transaction_per_migration=True,
            include_schemas=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
