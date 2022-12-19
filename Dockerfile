# docker build -t samgabrail/currencyconverter .
# docker push samgabrail/currencyconverter
FROM python:3.9-slim
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
COPY main.py .
RUN pip install -r requirements.txt
CMD ["python", "-m", "main"]