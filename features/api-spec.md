# Thai Tokenizer API Specification

## Overview
API สำหรับแยกคำภาษาไทย (Thai Word Tokenization) โดยใช้ PyThaiNLP library รองรับข้อความภาษาไทยล้วน และข้อความผสมภาษาไทย-อังกฤษ

## Feature-Specific Dependencies
- **PyThaiNLP**: 5.0.4 (Thai NLP library สำหรับ tokenization)
- **FastAPI**: 0.111.0
- **Uvicorn**: 0.29.0
- **Pydantic**: 2.7.1

## API Endpoint

### POST /tokenize

แยกคำภาษาไทยและคืนค่าเป็นข้อความที่แยกคำด้วยช่องว่าง (space-separated tokens)

#### Request

**Content-Type**: `application/json`

**Request Body Schema**:
```json
{
  "text": "string (required, min_length=1)"
}
```

**ตัวอย่าง Request**:

1. ข้อความภาษาไทยล้วน:
```json
{
  "text": "วันนี้คือวันจันทร์"
}
```

2. ข้อความผสมภาษาไทย-อังกฤษ:
```json
{
  "text": "วันนี้คือmonday"
}
```

#### Response

**Content-Type**: `application/json`

**Response Body Schema**:
```json
{
  "texttoken": "string"
}
```

**ตัวอย่าง Response**:

1. สำหรับข้อความภาษาไทยล้วน:
```json
{
  "texttoken": "วัน นี้ คือ วัน จันทร์"
}
```

2. สำหรับข้อความผสมภาษาไทย-อังกฤษ:
```json
{
  "texttoken": "วัน นี้ คือ monday"
}
```

#### Status Codes

- **200 OK**: Tokenization สำเร็จ
- **422 Unprocessable Entity**: Request body ไม่ถูกต้อง (validation error)

#### Validation Rules

- `text` field เป็น required
- `text` ต้องมีความยาวอย่างน้อย 1 ตัวอักษร

## Tokenization Engine Configuration

### PyThaiNLP newmm Engine
- **Engine**: `newmm` (Maximum Matching algorithm + Thai Character Cluster)
- **Configuration**: `keep_whitespace=False`
- **Behavior**: 
  - แยกคำภาษาไทยตามพจนานุกรม
  - รองรับข้อความผสมภาษาอังกฤษ (คงภาษาอังกฤษไว้ตามเดิม)
  - ไม่เก็บ whitespace เดิม
  - คืนค่าเป็น list of tokens แล้วนำมา join ด้วย space

### Pre-loading Corpus (Docker Build Optimization)
เพื่อลด startup time ให้ download PyThaiNLP corpus ตอน build time:

```dockerfile
# ใน Dockerfile หลัง RUN pip install
RUN python -c "from pythainlp.tokenize import word_tokenize; word_tokenize('ทดสอบ', engine='newmm')"
```

## API Testing Examples

### Using cURL
```bash
curl -X POST "http://localhost:9999/tokenize" \
  -H "Content-Type: application/json" \
  -d '{"text":"วันนี้คือวันจันทร์"}'
```

### Using Python requests
```python
import requests

response = requests.post(
    "http://localhost:9999/tokenize",
    json={"text": "วันนี้คือวันจันทร์"}
)
print(response.json())
# Output: {"texttoken": "วัน นี้ คือ วัน จันทร์"}
```

### Using HTTPie
```bash
http POST localhost:9999/tokenize text="วันนี้คือmonday"
```

## Implementation Checklist

- [x] สร้าง Pydantic schemas ใน `app/api/schemas/tokenize_schema.py`
  - [x] TokenizeRequest model (text: str, min_length=1)
  - [x] TokenizeResponse model (texttoken: str)
- [x] สร้าง business logic ใน `app/api/services/tokenize_service.py`
  - [x] ใช้ PyThaiNLP `word_tokenize()` กับ engine='newmm'
  - [x] ตั้งค่า `keep_whitespace=False`
  - [x] Join tokens ด้วย space
- [x] สร้าง API endpoint ใน `app/api/routes/tokenize.py`
  - [x] POST /tokenize endpoint
  - [x] ใช้ async def
  - [x] เชื่อมต่อกับ tokenize_service
- [x] อัพเดท `main.py` ให้ include tokenize router
- [x] เพิ่ม PyThaiNLP ใน `requirements.txt`
- [x] อัพเดท Dockerfile ให้ pre-download corpus
- [ ] ทดสอบ API ผ่าน `/docs`
- [ ] ทดสอบกับข้อความภาษาไทยล้วนและผสมภาษาอังกฤษ

---

**Document Version**: 1.0.0  
**Last Updated**: 2026-04-09  
**API Version**: 1.0.0
