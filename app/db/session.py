# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv, find_dotenv, dotenv_values
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parents[2]
env_path = find_dotenv(usecwd=True) or str(PROJECT_ROOT / ".env")
load_dotenv(dotenv_path=env_path, override=True, encoding="utf-8")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL and Path(env_path).exists():
    cfg = dotenv_values(env_path, encoding="utf-8")
    DATABASE_URL = cfg.get("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(f"❌ DATABASE_URL missing. Checked: {env_path}")

engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass
