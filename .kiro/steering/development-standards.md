# มาตรฐานและกฎการพัฒนาทั่วไป

## 🛠 Technology Stack (Global Standards)

- **Framework:** FastAPI (เวอร์ชันล่าสุดที่เสถียร)
- **Python Version:** Python 3.11 หรือสูงกว่า
- **ASGI Server:** Uvicorn with standard extras
- **Data Validation:** Pydantic 2.x
- **Package Manager:** ใช้ `pip` และต้องมีไฟล์ `requirements.txt`
- **Library สำหรับ Thai NLP:** ใช้ **PyThaiNLP** สำหรับงานประมวลผลภาษาไทยทั้งหมด (tokenization, segmenting, etc.)

## 📁 Project Structure (Standard Layout)

โครงสร้างโฟลเดอร์มาตรฐานสำหรับทุก API:

```
.
├── app/
│   ├── __init__.py
│   └── api/
│       ├── routes/          # API endpoint definitions
│       │   └── [feature].py
│       ├── schemas/         # Pydantic models
│       │   └── [feature]_schema.py
│       ├── services/        # Business logic
│       │   └── [feature]_service.py
│       └── config/          # Configuration files (optional)
├── features/                # Feature specifications
│   └── [feature]-spec.md
├── main.py                  # FastAPI application entry point
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker compose configuration
└── README.md               # Project documentation
```

**หลักการ:**
- แยก business logic ออกจาก API routes ให้ชัดเจน (separation of concerns)
- ใช้ชื่อไฟล์ที่สื่อความหมายและสอดคล้องกับฟีเจอร์
- เก็บ Pydantic schemas แยกจาก routes และ services

## 🐳 Docker & Infrastructure Standards

### Base Configuration
- **Base Image:** `python:3.11-slim` (เพื่อลดขนาด image)
- **Default Port:** 9999 (container และ host) เว้นแต่จะระบุไว้เป็นอย่างอื่นในเอกสาร feature
- **Working Directory:** `/app`

### Dockerfile Template
```dockerfile
FROM python:3.11-slim
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download/initialize resources at build time (if needed)
# Example: RUN python -c "import library; library.init()"

COPY . .
EXPOSE 9999

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9999"]
```

### Docker Compose Template
```yaml
services:
  [project-name]-api:
    build: .
    container_name: [project-name]-api
    ports:
      - "9999:9999"
    restart: unless-stopped
```

**หลักการ:**
- ใช้ multi-stage builds หากจำเป็นเพื่อลดขนาด image
- ชื่อ container ควรตามรูปแบบ: `[project-name]-api`
- Pre-download resources ตอน build time แทน runtime เพื่อความเร็ว

## 📝 Coding Style & Patterns

### API Endpoints
- **Async First:** ใช้ `async def` สำหรับ FastAPI endpoints เสมอ
- **HTTP Methods:** ใช้ HTTP methods ที่เหมาะสม (GET, POST, PUT, DELETE, PATCH)
- **Naming:** ใช้ชื่อ endpoint ที่ชัดเจนและเป็น RESTful (เช่น `/tokenize`, `/analyze`, `/check`)

### Data Validation
- ใช้ **Pydantic BaseModel** สำหรับ request และ response schemas ทั้งหมด
- กำหนด validation rules ที่ชัดเจน (min_length, max_length, regex, etc.)
- ใช้ Field descriptions เพื่ออธิบาย schema ใน API docs

### Documentation
- API documentation ต้องเข้าถึงได้ผ่าน `/docs` (Swagger UI) และ `/redoc` (ReDoc)
- เขียน docstrings สำหรับ functions และ classes ที่สำคัญ
- ใส่ examples ใน Pydantic schemas เพื่อให้ API docs มีตัวอย่างที่ชัดเจน

## ⚠️ Error Handling Standards

### HTTP Status Codes
- **200 OK:** Request สำเร็จ
- **400 Bad Request:** Request ไม่ถูกต้อง (logic error)
- **422 Unprocessable Entity:** Validation error (Pydantic จัดการอัตโนมัติ)
- **500 Internal Server Error:** Server error

### Validation Error Format (Pydantic Standard)
Pydantic จะคืนค่า validation errors ในรูปแบบมาตรฐาน:

```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "field_name"],
      "msg": "String should have at least X characters",
      "input": "...",
      "ctx": {"min_length": X}
    }
  ]
}
```

### Error Handling Pattern
```python
from fastapi import HTTPException

try:
    # Business logic
    result = process_data(input)
    return result
except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))
except Exception as e:
    raise HTTPException(status_code=500, detail="Internal server error")
```

## 🧪 Testing & Development

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run with auto-reload
uvicorn main:app --host 0.0.0.0 --port 9999 --reload
```

### Docker Development
```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

## 📦 Dependencies Management

- ระบุเวอร์ชันที่ชัดเจนใน `requirements.txt` (เช่น `fastapi==0.111.0`)
- จัดกลุ่ม dependencies ตามหมวดหมู่ (web framework, NLP, utilities, etc.)
- อัพเดต dependencies เป็นประจำเพื่อความปลอดภัย

## 🔒 Security Best Practices

- **ห้ามใช้ Library ที่ไม่มีจริง:** ห้ามใช้ Python libraries ที่ไม่ชัดเจนหรือไม่มีอยู่จริง
- **Input Validation:** ใช้ Pydantic เพื่อ validate input ทั้งหมด
- **Error Messages:** ไม่เปิดเผยข้อมูลระบบใน error messages
- **Dependencies:** ใช้ libraries จากแหล่งที่เชื่อถือได้เท่านั้น
