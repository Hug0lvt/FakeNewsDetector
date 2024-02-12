FROM python:3.8

EXPOSE 8000
WORKDIR /app
#ENV PYTHONUNBUFFERED=1

COPY . /app

RUN wget http://fr.archive.ubuntu.com/ubuntu/pool/universe/p/python-stdlib-extensions/python-tk_2.7.18-1_amd64.deb
RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
RUN pip install django sickit-learn pandas numpy pillow

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]