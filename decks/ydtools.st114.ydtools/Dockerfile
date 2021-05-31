FROM ubuntu:18.04

# .@@set=block.init block.manager.kind=deps.docker.conf-v4.yml
# .@@set=block.content={{ shell "task deps:gen-blocks" }}
RUN apt-get update\
    && apt-get install -y \
    bash \
    curl \
    wget \
    git 
# .@@set=block.over
RUN curl --help

COPY decks/_install_scripts /decks/_install_scripts
RUN  cd /tmp/ \
     && curl --location https://taskfile.dev/install.sh \
     | sh && chmod +x ./bin/task \
     && mv ./bin/task /usr/local/bin/task
RUN  ls /usr/local/bin/task
# task -t /decks/_install_scripts/install.yq.exe.yml

RUN uname -r
