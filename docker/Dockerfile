FROM python:3.7.4-slim as base

WORKDIR /srv/app

COPY ./requirements/ requirements/
RUN pip install --no-cache-dir -r requirements/base.txt


FROM base as dev
ENV PYTHONUNBUFFERED=true
ENV PYTHONDONTWRITEBYTECODE=true

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.5.0/wait /wait
RUN chmod +x /wait

RUN pip install --no-cache-dir -r requirements/dev.txt \
    && rm -rf /tmp/*

COPY . .

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]


FROM base as prod

COPY ./scholarly_content_detail/ scholarly_content_detail/
