FROM ubuntu:alpine

RUN set -ex && \
    apt-get update && \
    apt-get install -y --no-install-recommends libomp-dev build-essential && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN set -ex && \
    # install/upgrade pip
    python3 -m pip install --upgrade pip && \
    # install/upgrade wheel
    python3 -m pip install --upgrade wheel && \
    # create working directory
    mkdir -p /app && \
    # make appuser and appgroup owner of /app
    chown -R appuser:appgroup /app && \
    chmod -R 755 /app

COPY requirements.txt /app/

RUN set -ex && \
    pip install -r requirements.txt && \
    rm -f requirements.txt

USER appuser

COPY runserver.sh /app/bin/
COPY config.py wsgi.py /app/
COPY src /app/src