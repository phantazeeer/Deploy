# GribTripBackend
```bash
python -m venv .venv
```

```bash
source .venv/Scripts/activate
```

```bash
pip install -r requirements.txt
```

```bash
mkdir alembic/versions -p
```

```bash
alembic revision --autogenerate
```

```bash
alembic upgrade head
```

проблема с импортами:
```bash
export PYTHONPATH=$(pwd)
```
отладка:
```bash
cd app
```
```bash
python -c "import sys; print(sys.path)"
```
Запуск приложения:
собирается приложение, происходит alembic revision,
Повторный запуск приложения:
просто запускается приложение
Добавление новых изменений:
alembic revision

проблемы:
куда вынести алембик ревизион
Когда происходит сборка нового образа тянутся данные окружения из енв грибтрипбекенд
