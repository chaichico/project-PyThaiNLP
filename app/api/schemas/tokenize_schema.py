"""
tokenize_schema.py - Pydantic Models สำหรับ Request และ Response

ไฟล์นี้ทำหน้าที่:
1. กำหนดโครงสร้างข้อมูล (schema) ของ request และ response
2. ทำ data validation อัตโนมัติผ่าน Pydantic
3. สร้าง API documentation ที่มีตัวอย่างข้อมูลชัดเจน

หลักการ: ใช้ Pydantic เพื่อความปลอดภัยและความถูกต้องของข้อมูล
"""

from pydantic import BaseModel, Field


class TokenizeRequest(BaseModel):
    """
    Schema สำหรับ Request ของ /tokenize endpoint
    
    Attributes:
        text (str): ข้อความที่ต้องการแยกคำ
            - ต้องมีความยาวอย่างน้อย 1 ตัวอักษร (min_length=1)
            - รองรับภาษาไทยล้วนหรือผสมภาษาไทย-อังกฤษ
            - ... หมายถึง field นี้เป็น required (ต้องส่งมาเสมอ)
    
    Example:
        {"text": "วันนี้คือวันจันทร์"}
    """
    text: str = Field(
        ...,  # Required field (ต้องส่งมาเสมอ)
        min_length=1,  # ความยาวขั้นต่ำ 1 ตัวอักษร
        example="วันนี้คือวันจันทร์"  # ตัวอย่างที่แสดงใน API docs
    )


class TokenizeResponse(BaseModel):
    """
    Schema สำหรับ Response ของ /tokenize endpoint
    
    Attributes:
        texttoken (str): ข้อความที่แยกคำแล้ว
            - คำแต่ละคำจะคั่นด้วยช่องว่าง (space)
            - รูปแบบ: "คำ1 คำ2 คำ3 ..."
    
    Example:
        {"texttoken": "วัน นี้ คือ วัน จันทร์"}
    """
    texttoken: str = Field(
        ...,  # Required field (จะส่งกลับเสมอ)
        example="วัน นี้ คือ วัน จันทร์"  # ตัวอย่างที่แสดงใน API docs
    )