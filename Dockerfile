FROM python:3.10-slim

WORKDIR /kauma

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x kauma
RUN chmod +x test_json_outputs.py

CMD ["./test_json_outputs.py"]