FROM python:3.9-slim

WORKDIR /pad_2025_1_2
COPY setup.py .

COPY src/ src/

RUN mkdir -p static/static/csv

RUN pip install --upgrade pip \
    && pip install -e . \
    && rm -rf /root/.cache/pip

ENV PYTHONPATH="${PYTHONPATH}:/pad_2025_1_2/src"

ENTRYPOINT ["python", "-m", "edu_pad.main"]