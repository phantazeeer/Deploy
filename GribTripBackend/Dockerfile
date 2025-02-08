FROM python:3.12-alpine AS build
WORKDIR /application
COPY requirements_prod.txt .
RUN python -m venv .venv \
&& source .venv/bin/activate \
&& pip install -r requirements_prod.txt
COPY . .

FROM python:3.12-alpine AS runner
COPY --from=build /application ./application
WORKDIR /application
# CMD .venv/bin/python Toor.py
CMD source .venv/bin/activate \
&& export PYTHONPATH=$(pwd) \
&& mkdir alembic/versions -p \
&& alembic revision --autogenerate \
python Toor.py
# && alembic upgrade head \
# && python server.py