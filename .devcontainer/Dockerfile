FROM python:3.11-slim

WORKDIR /app

# Install Java
RUN apt update && \
    apt install -y sudo && \
    sudo apt install default-jdk -y

# Add non-root user
ARG USERNAME=nonroot
RUN groupadd --gid 1000 $USERNAME && \
    useradd --uid 1000 --gid 1000 -m $USERNAME
## Make sure to reflect new user in PATH
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
USER $USERNAME

## Pip dependencies
# Upgrade pip
RUN pip install --upgrade pip
# Install production dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt
# Install development dependencies
COPY requirements-dev.txt /tmp/requirements-dev.txt
RUN pip install -r /tmp/requirements-dev.txt && \
    rm /tmp/requirements-dev.txt

