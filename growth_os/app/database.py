from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ===================================================
# DATABASE URL
# ===================================================

# for local development (easy start)
DATABASE_URL = "sqlite:///./growth_os.db"

# If later moving to Postgres:
# DATABASE_URL = "postgresql://user:pass@localhost/dbname"


# ===================================================
# ENGINE
# ===================================================

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed for sqlite
)


# ===================================================
# SESSION
# ===================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ===================================================
# BASE MODEL
# ===================================================

Base = declarative_base()


# ===================================================
# DEPENDENCY (FastAPI)
# ===================================================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
