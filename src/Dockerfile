### FOR LOCAL DEVELOPMENT ONLY ###
### see infrastructure repo for staging and production ready deployment ###

FROM debian:buster-slim
RUN apt update && apt upgrade -y --no-install-recommends --fix-missing
RUN apt install -y --no-install-recommends \
    vim \
    libpq-dev gcc \
    python3 python3-pip python3-setuptools python3-wheel python3-venv python3-dev uwsgi-plugin-python3

WORKDIR /srv

# create directories
RUN mkdir src

# FIXME(@JonasCir) https://github.com/unbit/uwsgi/issues/1126
#  switch back to Debian version once landed

# [cache] install python packages we want to fetch via pip
COPY requirements.txt src/python/
RUN python3 -m venv src/python/venv && \
    pip3 install -r src/python/requirements.txt

# copy everything
COPY . src/

CMD [ "/srv/src/config/setup_and_run.sh" ]
