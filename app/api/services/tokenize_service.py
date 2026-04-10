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
        """
        แยกคำภาษาไทยโดยใช้ PyThaiNLP
        
        Method นี้จะ:
        1. รับข้อความภาษาไทย (หรือผสมภาษาไทย-อังกฤษ)
        2. ใช้ algorithm 'newmm' (Maximum Matching + Thai Character Cluster)
        3. แยกคำออกมาเป็น list
        4. นำคำทั้งหมดมาต่อกันด้วยช่องว่าง
        
        Args:
            text (str): ข้อความที่ต้องการแยกคำ
        
        Returns:
            str: ข้อความที่แยกคำแล้ว โดยคำแต่ละคำคั่นด้วยช่องว่าง
        
        Example:
            Input:  "วันนี้คือวันจันทร์"
            Output: "วัน นี้ คือ วัน จันทร์"
        
        Technical Details:
            - engine="newmm": ใช้ algorithm newmm ซึ่งเหมาะกับข้อความผสมภาษาไทย-อังกฤษ
            - keep_whitespace=False: ไม่เก็บช่องว่างเดิมที่มีอยู่ในข้อความ
        """
        # เรียกใช้ word_tokenize จาก PyThaiNLP เพื่อแยกคำ
        # ได้ผลลัพธ์เป็น list ของคำ เช่น ["วัน", "นี้", "คือ", "วัน", "จันทร์"]
        tokens = word_tokenize(
            text,
            engine="newmm",  # Algorithm ที่ใช้ (newmm = Maximum Matching + Thai Character Cluster)
            keep_whitespace=False  # ไม่เก็บช่องว่างเดิม
        )
        
        # นำคำทั้งหมดมาต่อกันด้วยช่องว่าง แล้ว return กลับไป
        return " ".join(tokens)