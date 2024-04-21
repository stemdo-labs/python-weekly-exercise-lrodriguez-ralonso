FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt
 
COPY ./app /app

RUN echo $(ls -1 /tmp/dir)

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
