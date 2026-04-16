"""
main.py - จุดเริ่มต้นของ FastAPI Application

ไฟล์นี้เป็นหัวใจหลักของ API ทำหน้าที่:
1. สร้าง FastAPI application instance
2. กำหนดข้อมูล metadata ของ API (title, description, version)
3. รวม routers จากโมดูลต่างๆ เข้ามา
4. สร้าง health check endpoint เพื่อตรวจสอบสถานะ API
"""

from fastapi import FastAPI
from app.api.routes import tokenize

# สร้าง FastAPI application instance พร้อมกำหนดข้อมูลพื้นฐาน
# ข้อมูลเหล่านี้จะแสดงใน API documentation (/swagger และ /redoc)
app = FastAPI(
    title="Thai Tokenizer API",  # ชื่อ API ที่แสดงใน docs
    description="API สำหรับแยกคำภาษาไทย (Thai Word Tokenization) โดยใช้ PyThaiNLP library",  # คำอธิบาย API
    version="1.0.0",  # เวอร์ชันของ API
    docs_url="/",  # เปลี่ยน Swagger UI path จาก /docs เป็น /
    redoc_url="/redoc",  # ReDoc path (เก็บไว้เหมือนเดิม)
)

# รวม router จากโมดูล tokenize เข้ามาใน application
# router นี้จะจัดการ endpoints ทั้งหมดที่เกี่ยวกับการแยกคำ
app.include_router(tokenize.router)


@app.get("/health", tags=["Health"])
async def root():
    """
    Health Check Endpoint
    
    ใช้สำหรับตรวจสอบว่า API ทำงานปกติหรือไม่
    เหมาะสำหรับ monitoring tools หรือ load balancers
    
    Returns:
        dict: สถานะการทำงานของ API
            - status: "ok" หมายถึง API ทำงานปกติ
            - message: ข้อความแจ้งสถานะ
    """
    return {"status": "ok", "message": "Thai Tokenizer API is running"}