## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/marketplace-api.git
cd marketplace-api 
```

2. Создайте и активируйте виртуальное окружение:
```commandline
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости:

```commandline
pip install -r requirements.txt
```

4. Настройте базу данных в файле .env: <br>

    Внести данные о своей БД в файл .env 
<br>
<br>

5. Создайте директорию для Alembic:
```commandline
alembic init alembic
```
После настройки env.py, выполните следующую команду для создания первой миграции: <br>
```commandline
alembic revision --autogenerate -m "Initial migration"
```
Затем примените миграции:
```commandline
alembic upgrade head
```

6. Запустите сервер:
```commandline
uvicorn app.main:app --reload
```
<br>
Для запуска тестов, нужно выполнить команду:

```commandline
pytest
```

*В файле conftest тоже надо прописать путь к БД