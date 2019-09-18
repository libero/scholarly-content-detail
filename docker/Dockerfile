FROM python:3.7.4-slim as base

WORKDIR /srv/app

COPY ./requirements/ requirements/
RUN pip install -U pip \
    && set -ex \
    && apt-get update -yq \
    && apt-get install -yq --no-install-recommends \
        git \
    && pip install --no-cache-dir -r requirements/base.txt \
    && rm -rf ~/.cache/* \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*


FROM base as dev
ENV FLASK_APP scholarly_content_detail:create_app(\"dev.py\")
ENV FLASK_ENV development
ENV PYTHONDONTWRITEBYTECODE true
ENV PYTHONUNBUFFERED true

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.5.0/wait /wait
RUN chmod +x /wait

RUN pip install --no-cache-dir -r requirements/dev.txt \
    && rm -rf /tmp/*

COPY . .

HEALTHCHECK --interval=5s \
    CMD bash -c "echo > /dev/tcp/localhost/5000"

EXPOSE 5000
CMD bash -c "/wait && flask run --host=0.0.0.0"


FROM base as prod
ENV FLASK_APP scholarly_content_detail:create_app(\"prod.py\")
ENV FLASK_ENV production

COPY ./scholarly_content_detail/ scholarly_content_detail/
