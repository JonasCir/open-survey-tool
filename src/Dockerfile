FROM debian:buster-slim
RUN apt update && apt upgrade -y --no-install-recommends
RUN apt install -y \
    vim \
    python3 python3-pip python3-setuptools python3-wheel python3-venv python3-dev\
    uwsgi-plugin-python3 \
    python3-pandas python3-pdfkit

WORKDIR /srv

# create directories
RUN mkdir src

# FIXME(@JonasCir) https://github.com/unbit/uwsgi/issues/1126
#  switch back to Debian version once landed
# [cache] install python packages we want to fetch via pip
COPY requirements-prod.txt src/python/
RUN python3 -m venv src/python/venv && \
    pip3 install -r src/python/requirements-prod.txt

# copy everything
COPY . src/

CMD [ "/srv/src/config/setup_and_run.sh" ]
