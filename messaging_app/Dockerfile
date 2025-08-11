FROM python:3.10
COPY . .
EXPOSE 8000
# docker run -p 8000:8000 containerizedapp
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]