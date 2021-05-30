FROM ubuntu:18.04

# .@@set=block.init block.manager=deps.docker.conf-v4.yml
# .@@set=block.content={{ shell "task -t deps.docker.conf-v4.yml deps:gen-blocks" }}
RUN apt-get update && items=' \
curl \
wget \
git \
' apt-get install -y ${items}
# .@@set=block.over


RUN uname -r
