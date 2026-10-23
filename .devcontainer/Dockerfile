# EXPERIMENTAL (not built/tested here); official OpenFOAM Foundation v14 apt source:
# https://openfoam.org/download/14-ubuntu/
FROM ubuntu:24.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates wget software-properties-common python3 git build-essential \
    && rm -rf /var/lib/apt/lists/*
RUN wget -qO /etc/apt/trusted.gpg.d/openfoam.asc https://dl.openfoam.org/gpg.key \
    && add-apt-repository -y 'http://dl.openfoam.org/ubuntu main dev' \
    && apt-get update \
    && apt-get install -y --no-install-recommends openfoam14 \
    && rm -rf /var/lib/apt/lists/*
RUN test -f /opt/openfoam14/etc/bashrc
