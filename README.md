# Сборка проекта GribTrip


```commandline
copy GribTripBackend\.env.template .env
```


```commandline
docker-compose up -d db
```

```commandline
cd GribTripBackend
```

```commandline
python -m venv .venv
```

```
.venv\Scripts\activate.bat
```

```commandline
pip install -r requirements.txt
```

```commandline
copy .env.template .env
```

```commandline
mkdir alembic\versions
```

```commandline
alembic revision --autogenerate
```

```commandline
alembic upgrade head
```


```commandline
docker-compose up -d
```