from sqlalchemy import engine_from_config, pool

from alembic import context
from txhttputil.util.LoggingUtil import setupLogging

global config
config = context.config

setupLogging()

from peek_server.storage.DeclarativeBase import metadata
target_metadata = metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def exclude_tables_from_config(config_):
    tables_ = config_.get("tables", None)
    if tables_ is not None:
        tables = tables_.split(",")
    return tables

exclude_tables = exclude_tables_from_config(config.get_section('alembic:exclude'))


def include_object(object, name, type_, reflected, compare_to):
    # If it's not in this schema, don't include it
    if hasattr(object, 'schema') and object.schema != target_metadata.schema:
        return False

    if type_ == "table" and name in 'spatial_ref_sys':
        return False
    else:
        return True

def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)


    with connectable.connect() as connection:
        # Ensure the schema exists
        connection.execute('CREATE SCHEMA IF NOT EXISTS "%s" ' % target_metadata.schema)

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
            include_schemas=True,
            version_table_schema=target_metadata.schema
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    raise NotImplementedError("Peek doesn't allow offline migrations")
else:
    run_migrations_online()