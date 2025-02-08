# Сборка проект GribTrip


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
cp .env.template .env
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