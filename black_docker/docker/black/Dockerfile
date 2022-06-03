FROM python:3.10.4-alpine

WORKDIR /

RUN pip install black[d]

EXPOSE 45484
CMD ["blackd", "--bind-host", "0.0.0.0", "--bind-port", "45484"]