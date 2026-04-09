from fastapi import APIRouter
from app.api.schemas.tokenize_schema import TokenizeRequest, TokenizeResponse
from app.api.services.tokenize_service import TokenizeService

router = APIRouter()
tokenize_service = TokenizeService()

@router.post("/tokenize", response_model=TokenizeResponse, tags=["Tokenizer"])
async def tokenize(request: TokenizeRequest) -> TokenizeResponse:
    """
    แยกคำภาษาไทยและคืนค่าเป็นข้อความที่แยกคำด้วยช่องว่าง
    
    รองรับข้อความภาษาไทยล้วนและข้อความผสมภาษาไทย-อังกฤษ
    """
    result = tokenize_service.tokenize(request.text)
    return TokenizeResponse(texttoken=result)