FROM python:3.11.4

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app", "--log-level", "debug"]