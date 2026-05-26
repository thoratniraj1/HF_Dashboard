from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database credentials
username = "root"
password = "godseye"
host = "127.0.0.1"
port = "3306"
database = "godseye"

DATABASE_URL = (
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# Create engine
engine = create_engine(
    DATABASE_URL,
    echo=True    # optional: prints SQL queries
)

# Session
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# Base class
Base = declarative_base()