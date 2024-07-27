from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session, declarative_base

# создадим или подключимся к базе данных
SQLALCHEMY_BASE_URL = "sqlite:///social_media.db"
# создаем движок
engine = create_engine(SQLALCHEMY_BASE_URL)
# переменная, которая будет генерировать сессии
SessionLocal = sessionmaker(bind=engine)
# создадим шаблон декларативной базы данных для классов (Model...)
Base = declarative_base()

# функция-генератор сессий и отката бд
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()