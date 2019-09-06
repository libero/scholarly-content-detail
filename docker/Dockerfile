FROM python:3.7.4-slim as base

WORKDIR /srv/app

COPY ./requirements/ requirements/
RUN pip install --no-cache-dir -r requirements/base.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0:8000"]


FROM base as dev
ENV PYTHONUNBUFFERED=true
ENV PYTHONDONTWRITEBYTECODE=true

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.5.0/wait /wait
RUN chmod +x /wait

RUN pip install --no-cache-dir -r requirements/dev.txt \
    && rm -rf /tmp/*
