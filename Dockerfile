FROM python:3.8-slim-buster AS builder
LABEL "maintainer"="Shashwat Kare <skare@cisco.com>"
LABEL "version"=1.1

ENV PYTHONPATH "${PYTHONPATH}:/usr/app:/usr/app/src"
ENV PYTHON_BIN_PATH "/usr/bin/python3"
ENV PYTHON_INCLUDE_PATH /usr/include/python3.8m/
ENV PYTHON_LIB_PATH /usr/lib/python3.8/site-packages

#RUN apt-get -y update --fix-missing && \
#    apt-get -y upgrade && \
#    apt-get install -y gcc libev-dev curl


RUN pip install -U pip

RUN mkdir -m 0700 -p /usr/app && \
    chmod -R 777 /usr/app && \
    groupadd -r aira_group && \
    useradd -r -g aira_group aira
WORKDIR /usr/app
COPY . .
EXPOSE 8000

RUN pip install -r requirements.txt --no-cache-dir && apt-get clean

USER aira
CMD streamlit run --server.port=8000 --server.address=0.0.0.0 --server.baseUrlPath /home src/app.py
