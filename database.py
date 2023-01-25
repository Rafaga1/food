from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from sqlalchemy.pool import NullPool


DB_DSN = URL.create(
    drivername='postgresql+asyncpg',
    username='web',
    password='web',
    # host='0.0.0.0',
    host='postgres',
    port=5432,
    database='postgres'
)

ALEMBIC_DB_DSN = URL(
    drivername='postgresql',
    username='web',
    password='web',
    host='0.0.0.0',
    port=5432,
    database='postgres',
)

metadata = MetaData()
engine = create_async_engine(DB_DSN, echo=True, poolclass=NullPool)
session = sessionmaker(bind=engine, class_=AsyncSession)


