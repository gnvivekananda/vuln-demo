FROM python:3.14.2
# ❌ Outdated Python version with known CVEs

WORKDIR /app

# ❌ Install vulnerable packages
RUN pip install flask==0.10 requests==2.19.0

COPY app.py .

# ❌ Run as root user (bad practice)
USER root

CMD ["python", "app.py"]
