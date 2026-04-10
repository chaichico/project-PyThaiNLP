"""
tokenize.py - API Routes สำหรับการแยกคำภาษาไทย

ไฟล์นี้ทำหน้าที่:
1. กำหนด API endpoints ที่เกี่ยวข้องกับการแยกคำ (tokenization)
2. รับ request จาก client และส่งต่อไปยัง service layer
3. จัดการ response ให้อยู่ในรูปแบบที่ถูกต้องตาม schema

หลักการ: แยก routing logic ออกจาก business logic (separation of concerns)
"""

from fastapi import APIRouter
from app.api.schemas.tokenize_schema import TokenizeRequest, TokenizeResponse
from app.api.services.tokenize_service import TokenizeService

# สร้าง APIRouter instance สำหรับจัดการ endpoints ในกลุ่มนี้
router = APIRouter()

# สร้าง instance ของ TokenizeService เพื่อใช้งาน business logic
# Service นี้จะทำงานจริงๆ ในการแยกคำ
tokenize_service = TokenizeService()


@router.post("/tokenize", response_model=TokenizeResponse, tags=["Tokenizer"])
async def tokenize(request: TokenizeRequest) -> TokenizeResponse:
    
    # เรียกใช้ service เพื่อทำการแยกคำ
    result = tokenize_service.tokenize(request.text)
    
    # สร้าง response object และส่งกลับไปยัง client
    return TokenizeResponse(texttoken=result)