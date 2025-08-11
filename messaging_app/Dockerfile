FROM python:3.10
COPY . .
EXPOSE 8000
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]