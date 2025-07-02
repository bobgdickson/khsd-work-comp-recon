from logging.config import fileConfig
import os
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
# Add your app to the path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from app.db import DATABASE_URL, engine
from app.models import Base  # Import your models to ensure they are registered
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
target_metadata = Base.metadata

def include_object(object, name, type_, reflected, compare_to):
    """
    Determine if a database object should be included in migrations.

    Args:
        object: The SQLAlchemy object to inspect.
        name: Name of the database object.
        type_: Type of the object, e.g., 'table', 'column'.
        reflected: Flag indicating if the object was reflected.
        compare_to: The object being compared to.

    Returns:
        bool: True if the object is a table starting with 'WORK_COMP_', False otherwise.
    """
    return type_ == "table" and name.upper().startswith("WORK_COMP_")

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
        version_table='alembic_version_work_comp',
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            include_object=include_object,
            version_table='alembic_version_work_comp',
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
