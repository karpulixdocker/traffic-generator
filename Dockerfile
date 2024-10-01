FROM python:3.9-slim
RUN pip install requests
COPY app.py /app.py
WORKDIR /
CMD ["python", "app.py"]
