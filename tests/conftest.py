import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.database import Base
from app.models import *  # Импортируйте все ваши модели здесь

# Укажите URL вашей тестовой базы данных MySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost/marketplace_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    # Создание всех таблиц перед тестами
    Base.metadata.create_all(bind=engine)

    # Создание новой сессии для тестирования
    session = TestingSessionLocal()

    # Добавление начальных данных, если это необходимо
    category = Category(name="Test Category")
    session.add(category)
    session.commit()

    yield session

    # Очистка базы данных после завершения тестов
    Base.metadata.drop_all(bind=engine)
    session.close()

@pytest.fixture(scope="module")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c

