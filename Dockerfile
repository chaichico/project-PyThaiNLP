FROM python:3.11-slim
 
WORKDIR /app
 
# Install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
# Download PyThaiNLP corpus at build time (not runtime)
RUN python -c "from pythainlp.tokenize import word_tokenize; word_tokenize('ทดสอบ', engine='newmm')"

COPY . .
EXPOSE 9999

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9999"]