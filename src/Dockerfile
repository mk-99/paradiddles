FROM python:3.10-slim

WORKDIR /opt/paradiddles

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup --system service_group \
    && adduser --system service_user --ingroup service_group \
    && apt-get update \
    && pip install --upgrade pip

COPY requirements.txt /opt/paradiddles/requirements.txt

RUN  pip install -r requirements.txt --no-cache-dir

COPY . .

COPY entrypoint.sh /opt/paradiddles/entrypoint.sh

RUN chown -R service_user:service_group .
USER service_user

ENTRYPOINT ["bash", "/opt/paradiddles/entrypoint.sh"]
