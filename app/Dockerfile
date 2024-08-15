FROM python:3.11

WORKDIR /app

COPY src /app/
COPY requirements /app/requirements

RUN pip install -r requirements/private.txt \
    && pip install -r requirements/public.txt

CMD ["/bin/bash"]