"""
tokenize_service.py - Business Logic สำหรับการแยกคำภาษาไทย

ไฟล์นี้ทำหน้าที่:
1. ประมวลผล business logic จริงๆ ของการแยกคำ
2. เรียกใช้ PyThaiNLP library เพื่อทำ tokenization
3. จัดรูปแบบผลลัพธ์ให้พร้อมส่งกลับ

หลักการ: แยก business logic ออกจาก routing เพื่อให้ code สะอาดและทดสอบง่าย
"""

from pythainlp.tokenize import word_tokenize


class TokenizeService:
    """
    Service Class สำหรับจัดการการแยกคำภาษาไทย
    
    ใช้ PyThaiNLP library ซึ่งเป็น standard library สำหรับ NLP ภาษาไทย
    มีความแม่นยำสูงและรองรับข้อความผสมภาษาไทย-อังกฤษได้ดี
    """
    
    def tokenize(self, text: str) -> str:
        # เรียกใช้ word_tokenize จาก PyThaiNLP เพื่อแยกคำ
        # ได้ผลลัพธ์เป็น list ของคำ เช่น ["วัน", "นี้", "คือ", "วัน", "จันทร์"]
        tokens = word_tokenize(
            text,
            engine="newmm",  # Algorithm ที่ใช้ (newmm = Maximum Matching + Thai Character Cluster)
            # engine="mm",
            # engine="newmm-safe" ,
            keep_whitespace=False  # ไม่เก็บช่องว่างเดิม
        )
        
        # นำคำทั้งหมดมาต่อกันด้วยช่องว่าง แล้ว return กลับไป
        return " ".join(tokens)