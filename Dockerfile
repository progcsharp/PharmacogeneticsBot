FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app

RUN ls /code
RUN ls /code/app

EXPOSE 5050
CMD ["python", "app/main.py"]