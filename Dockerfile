
FROM python:3.9-slim


WORKDIR /app


COPY script.py .


RUN mkdir -p /home/data
COPY texts/ /home/data/


CMD ["python", "script.py"]