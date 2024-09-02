FROM python:3.8-slim
WORKDIR /myapp
COPY app.py ./
COPY requirements.txt ./
RUN apt update
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
