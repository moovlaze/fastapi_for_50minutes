FROM python:3.12-silm

COPY . .

RUN pip instal -r requiirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]