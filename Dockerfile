FROM ubuntu:latest
LABEL authors="rival"

ENTRYPOINT ["top", "-b"]