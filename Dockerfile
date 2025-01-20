FROM python:3.12
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
RUN python manage.py shell < scripts/populate_books.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
