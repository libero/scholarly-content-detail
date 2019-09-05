FROM python:3.7.4-slim

ENV PYTHONUNBUFFERED true
ENV PYTHONDONTWRITEBYTECODE true

WORKDIR /srv/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0:8000"]
