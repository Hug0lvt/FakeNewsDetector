FROM django

EXPOSE 8000
WORKDIR /app

COPY . /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]