FROM django

EXPOSE 8000
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]