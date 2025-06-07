FROM python:3.9-slim

WORKDIR /pad_2025_1_2
COPY pruebadocker.py /pad_2025_1_2/

CMD [ "python","pruebadocker.py" ]