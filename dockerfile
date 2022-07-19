FROM python:3.10.5-slim-bullseye

WORKDIR /app

COPY . /app/

RUN apt-get update -y
RUN python3 -m venv /app/venv

# Enable venv
ENV PATH="/app/venv/bin:$PATH"

EXPOSE 80

RUN python3 -m pip install -r requirements.txt

ENV FLASK_APP="app"

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]

