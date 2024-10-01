FROM python:3.9-slim
RUN pip install requests
COPY app.py /app.py
WORKDIR /
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]
