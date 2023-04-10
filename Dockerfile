FROM python:3.8-alpine as base

FROM base as builder

RUN mkdir /install
RUN apk update && apk add python3-dev
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
COPY . /code
RUN pip install -r /code/requirements.txt
RUN apk --no-cache add ffmpeg
RUN apk add --no-cache bash
WORKDIR /code
