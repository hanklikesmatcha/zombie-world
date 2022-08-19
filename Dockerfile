FROM python:3.9
WORKDIR /ailo/src
COPY ./requirements.txt /ailo/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /ailo/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/ailo/src"
COPY ./src .
CMD uvicorn app:app --reload --host=0.0.0.0 --port=3000