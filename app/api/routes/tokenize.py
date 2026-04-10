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
    """
    POST /tokenize - แยกคำภาษาไทยและคืนค่าเป็นข้อความที่แยกคำด้วยช่องว่าง
    
    Endpoint นี้รับข้อความภาษาไทย (หรือผสมภาษาไทย-อังกฤษ) แล้วแยกคำออกมา
    โดยใช้ PyThaiNLP library ซึ่งมีความแม่นยำสูงในการแยกคำภาษาไทย
    
    Args:
        request (TokenizeRequest): ข้อมูล request ที่มี field:
            - text (str): ข้อความที่ต้องการแยกคำ (ต้องมีความยาวอย่างน้อย 1 ตัวอักษร)
    
    Returns:
        TokenizeResponse: ข้อมูล response ที่มี field:
            - texttoken (str): ข้อความที่แยกคำแล้ว โดยคำแต่ละคำคั่นด้วยช่องว่าง
    
    Example:
        Request:  {"text": "วันนี้คือวันจันทร์"}
        Response: {"texttoken": "วัน นี้ คือ วัน จันทร์"}
    
    HTTP Status Codes:
        - 200: แยกคำสำเร็จ
        - 422: ข้อมูล request ไม่ถูกต้อง (validation error)
    """
    # เรียกใช้ service เพื่อทำการแยกคำ
    result = tokenize_service.tokenize(request.text)
    
    # สร้าง response object และส่งกลับไปยัง client
    return TokenizeResponse(texttoken=result)