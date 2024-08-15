FROM python:3.11

WORKDIR /app

COPY ./src /app/src/
COPY ./requirements /app/requirements/

RUN pip install --no-cache-dir -U -r requirements/private.txt \ 
    && pip install --no-cache-dir -U -r requirements/public.txt

CMD ["fastapi", "run", "src/main.py", "--port", "8000"]