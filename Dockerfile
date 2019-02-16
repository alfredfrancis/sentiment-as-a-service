FROM python:3-onbuild
ENTRYPOINT gunicorn app:app --bind 0.0.0.0:8001