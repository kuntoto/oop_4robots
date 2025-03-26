# การอธิบายแนวคิดของ Object-Oriented Programming (OOP)
#
# Object-Oriented Programming (OOP) คือแนวคิดในการพัฒนาโปรแกรมที่เน้นการจัดระเบียบข้อมูลและฟังก์ชัน
# โดยการใช้ "คลาส" (Class) และ "อ็อบเจกต์" (Object) คลาสเป็นแม่แบบที่กำหนดลักษณะของข้อมูลและพฤติกรรมต่างๆ
# ในขณะที่อ็อบเจกต์เป็นการสร้างอินสแตนซ์ของคลาสนั้น ๆ ซึ่งจะสามารถเก็บข้อมูลและดำเนินการตามฟังก์ชันที่กำหนดไว้
#
# OOP มีคุณสมบัติหลักๆ ที่สำคัญคือ:
# 1. **Encapsulation (การห่อหุ้ม)** - ข้อมูลและฟังก์ชันที่เกี่ยวข้องจะถูกจัดกลุ่มไว้ในคลาสเดียวกัน เพื่อให้การเข้าถึงข้อมูลภายในสามารถควบคุมได้อย่างปลอดภัย
# 2. **Abstraction (การซ่อนรายละเอียด)** - การซ่อนรายละเอียดที่ไม่จำเป็นและแสดงแค่สิ่งที่สำคัญในการทำงานของโปรแกรม
# 3. **Inheritance (การสืบทอด)** - คลาสสามารถสืบทอดคุณสมบัติและพฤติกรรมจากคลาสอื่น ๆ ได้ ทำให้สามารถสร้างโปรแกรมที่ยืดหยุ่นและขยายได้ง่าย
# 4. **Polymorphism (การแสดงออกหลายรูปแบบ)** - อ็อบเจกต์สามารถแสดงพฤติกรรมที่แตกต่างกันได้ตามประเภทของมัน

# 1. **Class (คลาส)**
# คลาสคือแม่แบบในการสร้างอ็อบเจกต์ ซึ่งจะกำหนดข้อมูลและพฤติกรรมของอ็อบเจกต์
# คลาสประกอบด้วยสองส่วนหลักคือ **Attributes (คุณสมบัติ)** และ **Methods (วิธีการ)**
#   - **Attributes** คือคุณสมบัติหรือข้อมูลที่เก็บไว้ในอ็อบเจกต์
#   - **Methods** คือฟังก์ชันหรือพฤติกรรมที่อ็อบเจกต์สามารถทำได้
#
# 2. **Object (อ็อบเจกต์)**
# อ็อบเจกต์คือลูกของคลาสที่ถูกสร้างขึ้นมาเพื่อใช้งานจริง โดยจะมีคุณสมบัติและพฤติกรรมตามที่คลาสกำหนดไว้
# การสร้างอ็อบเจกต์จะใช้คำสั่งสร้างอินสแตนซ์จากคลาส เช่น `robot = Robot()` 
#
# ตัวอย่าง: การสร้างหุ่นยนต์เพื่อการศึกษา

# กำหนดคลาสหุ่นยนต์ (Robot)
class Robot:
    # เมธอด __init__ จะทำงานเมื่อสร้างอ็อบเจกต์ใหม่จากคลาสนี้
    def __init__(self, name, color):
        # self คือการอ้างอิงถึงอ็อบเจกต์ที่ถูกสร้างขึ้นจากคลาสนี้
        self.name = name  # ชื่อของหุ่นยนต์
        self.color = color  # สีของหุ่นยนต์
        self.is_moving = False  # สถานะการเคลื่อนที่ของหุ่นยนต์ (เริ่มต้นคือหยุด)

    # เมธอดให้หุ่นยนต์เคลื่อนที่ไปข้างหน้า
    def move_forward(self):
        print(f"{self.name} is moving forward.")  # แสดงข้อความว่าหุ่นยนต์กำลังเคลื่อนที่
        self.is_moving = True  # เปลี่ยนสถานะเป็นกำลังเคลื่อนที่

    # เมธอดให้หุ่นยนต์หยุดการเคลื่อนที่
    def stop(self):
        print(f"{self.name} has stopped.")  # แสดงข้อความว่าหุ่นยนต์หยุดแล้ว
        self.is_moving = False  # เปลี่ยนสถานะเป็นหยุด

    # เมธอดแสดงข้อมูลของหุ่นยนต์
    def get_info(self):
        # แสดงข้อมูลของหุ่นยนต์ในรูปแบบข้อความ
        print(f"Robot Name: {self.name}")
        print(f"Robot Color: {self.color}")
        print(f"Is Moving: {self.is_moving}")

# สร้างอ็อบเจกต์หุ่นยนต์ใหม่จากคลาส Robot
robot = Robot(name="Educational Robot", color="Blue")

# เรียกใช้เมธอดแสดงข้อมูลของหุ่นยนต์
robot.get_info()

# ให้หุ่นยนต์เคลื่อนที่ไปข้างหน้า
robot.move_forward()

# ให้หุ่นยนต์หยุด
robot.stop()

# คำอธิบาย:
# ในโค้ดนี้เราได้สร้างคลาส `Robot` ซึ่งมีคุณสมบัติ (Attributes) คือ `name`, `color`, และ `is_moving`
# และมีเมธอด (Methods) ที่ช่วยให้หุ่นยนต์สามารถเคลื่อนที่ (`move_forward()`), หยุดการเคลื่อนที่ (`stop()`),
# และแสดงข้อมูลของหุ่นยนต์ (`get_info()`).
# เมื่อสร้างอ็อบเจกต์ `robot` ขึ้นมาใหม่จากคลาสนี้ ก็สามารถเรียกใช้เมธอดต่างๆ เพื่อควบคุมการทำงานของหุ่นยนต์ได้

# โครงสร้างของคลาส:
# - **Attributes**: 
#     - `name`: ชื่อของหุ่นยนต์ (เช่น "Educational Robot")
#     - `color`: สีของหุ่นยนต์ (เช่น "Blue")
#     - `is_moving`: สถานะการเคลื่อนที่ของหุ่นยนต์ (เช่น True หรือ False)
# - **Methods**:
#     - `move_forward()`: เคลื่อนที่ไปข้างหน้า
#     - `stop()`: หยุดการเคลื่อนที่
#     - `get_info()`: แสดงข้อมูลของหุ่นยนต์

# สรุป:
# - การใช้ OOP ช่วยให้เราแยกแยะข้อมูลและพฤติกรรมออกจากกันอย่างชัดเจนและสะดวกในการจัดการ
# - เราสามารถสร้างคลาสที่เป็นแม่แบบและนำมาใช้สร้างอ็อบเจกต์เพื่อให้โปรแกรมยืดหยุ่นและสามารถนำไปใช้ซ้ำได้ในหลายกรณี
# - คลาสและอ็อบเจกต์ทำให้โปรแกรมมีความเป็นระเบียบและสามารถขยายได้ง่ายขึ้น
