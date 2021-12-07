FROM python:3-alpine 
WORKDIR /src
COPY ./ .
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev
RUN pip3 install numpy
CMD python /src/solution.py