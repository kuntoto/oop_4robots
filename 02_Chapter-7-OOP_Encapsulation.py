# การอธิบายคุณสมบัติ Encapsulation (การห่อหุ้ม) ใน OOP

# Encapsulation หรือ การห่อหุ้ม คือการซ่อนรายละเอียดภายในของอ็อบเจกต์ และเปิดเผยเฉพาะข้อมูลที่จำเป็น
# โดยการซ่อนข้อมูลภายในคลาส (ตัวแปร และฟังก์ชัน) ทำให้ผู้ใช้คลาสไม่สามารถเข้าถึงหรือแก้ไข
# ข้อมูลโดยตรงได้ ซึ่งจะช่วยเพิ่มความปลอดภัยให้กับข้อมูลและลดความซับซ้อนในการใช้งาน

# **ข้อดีของ Encapsulation**:
# 1. การปกป้องข้อมูล: ข้อมูลที่สำคัญถูกปกป้องไม่ให้ถูกเปลี่ยนแปลงโดยตรงจากภายนอก
# 2. การควบคุมการเข้าถึงข้อมูล: สามารถควบคุมว่าใครสามารถเข้าถึงหรือแก้ไขข้อมูลได้บ้าง
# 3. การปรับปรุงและดูแลรักษาง่าย: เมื่อข้อมูลถูกห่อหุ้มไว้ในคลาส ก็สามารถเปลี่ยนแปลงได้โดยไม่กระทบกับผู้ใช้

# ตัวอย่าง:

class Robot:
    """
    คลาสนี้แสดงถึงหุ่นยนต์ โดยใช้ Encapsulation เพื่อห่อหุ้มข้อมูลต่างๆ
    ข้อมูลที่สำคัญจะถูกซ่อนไว้ในตัวแปรภายใน และการเข้าถึงจะต้องผ่านเมธอด
    """

    def __init__(self, name, battery_level):
        # ตัวแปรที่ห่อหุ้ม (Encapsulated) จะไม่สามารถเข้าถึงได้จากภายนอกโดยตรง
        self.__name = name  # ชื่อหุ่นยนต์
        self.__battery_level = battery_level  # ระดับแบตเตอรี่

    def get_name(self):
        # ฟังก์ชันที่ให้เข้าถึงชื่อหุ่นยนต์
        return self.__name

    def get_battery_level(self):
        # ฟังก์ชันที่ให้เข้าถึงระดับแบตเตอรี่
        return self.__battery_level

    def set_battery_level(self, new_battery_level):
        # ฟังก์ชันที่ให้เปลี่ยนแปลงระดับแบตเตอรี่ (ผ่านการตรวจสอบ)
        if 0 <= new_battery_level <= 100:
            self.__battery_level = new_battery_level
        else:
            print("Battery level must be between 0 and 100.")

    def move(self):
        # ฟังก์ชันที่ใช้ในการเคลื่อนที่ของหุ่นยนต์
        if self.__battery_level > 0:
            print(f"{self.__name} is moving!")
            self.__battery_level -= 10  # ลดระดับแบตเตอรี่ทุกครั้งที่หุ่นยนต์เคลื่อนที่
        else:
            print(f"{self.__name} cannot move. Battery is empty.")

# สร้างอ็อบเจกต์ของหุ่นยนต์
robot = Robot("Robo1", 50)

# การเข้าถึงข้อมูลจะต้องผ่านเมธอด
print(robot.get_name())  # Output: Robo1
print(robot.get_battery_level())  # Output: 50

# การปรับระดับแบตเตอรี่
robot.set_battery_level(80)
print(robot.get_battery_level())  # Output: 80

# หุ่นยนต์เคลื่อนที่
robot.move()  # Output: Robo1 is moving!
print(robot.get_battery_level())  # Output: 70

# หุ่นยนต์เคลื่อนที่ต่อไป
robot.move()  # Output: Robo1 is moving!
print(robot.get_battery_level())  # Output: 60

# การพยายามเปลี่ยนแปลงระดับแบตเตอรี่ให้เกินขอบเขต
robot.set_battery_level(150)  # Output: Battery level must be between 0 and 100.

# คำอธิบาย:
# - ในตัวอย่างนี้, เราใช้ **Encapsulation** เพื่อห่อหุ้มข้อมูลของหุ่นยนต์ เช่น ชื่อหุ่นยนต์ (`__name`) และ
#   ระดับแบตเตอรี่ (`__battery_level`) โดยทำให้ไม่สามารถเข้าถึงหรือแก้ไขข้อมูลเหล่านี้โดยตรงจากภายนอกคลาส
# - ข้อมูลเหล่านี้สามารถถูกเข้าถึงและเปลี่ยนแปลงได้เพียงผ่านเมธอดที่กำหนดเท่านั้น (เช่น `get_name()`, `get_battery_level()`)
#   และหากต้องการเปลี่ยนแปลงระดับแบตเตอรี่ ก็ต้องผ่านเมธอด `set_battery_level()` ที่มีการตรวจสอบข้อมูลก่อน

# ขยายความ:

# 1. **การปกป้องข้อมูล**:
#    - การใช้ **Encapsulation** ช่วยปกป้องข้อมูลจากการถูกเปลี่ยนแปลงหรือเข้าถึงโดยตรงจากภายนอก
#    - ตัวแปรที่เริ่มต้นด้วย `__` เช่น `__name` และ `__battery_level` จะถูกซ่อนไว้และไม่สามารถเข้าถึงจากภายนอกได้
#    - การใช้เมธอด (getter/setter) เพื่อเข้าถึงหรือปรับข้อมูลให้เกิดการควบคุมการเข้าถึงข้อมูลที่ดีขึ้น
#    - ในที่นี้, การตรวจสอบค่าระดับแบตเตอรี่ผ่าน `set_battery_level()` จะช่วยป้องกันการตั้งค่าแบตเตอรี่ที่ไม่ถูกต้อง (เช่น เกิน 100%)

# 2. **การควบคุมการเข้าถึง**:
#    - ด้วยการห่อหุ้มข้อมูล, เราสามารถควบคุมว่าใครสามารถเปลี่ยนแปลงข้อมูลได้บ้าง
#    - เมธอด `set_battery_level()` จะทำการตรวจสอบค่าที่เข้ามาเพื่อให้แน่ใจว่าค่าของแบตเตอรี่จะไม่เกินขอบเขตที่กำหนด
#    - นอกจากนี้, การเคลื่อนที่ของหุ่นยนต์จะลดระดับแบตเตอรี่ แต่ถ้าระดับแบตเตอรี่เป็น 0 ก็ไม่สามารถเคลื่อนที่ได้

# 3. **ปรับปรุงและดูแลรักษาง่าย**:
#    - หากในอนาคตต้องการเปลี่ยนแปลงวิธีการคำนวณระดับแบตเตอรี่หรือรายละเอียดอื่นๆ ภายในคลาส `Robot`
#      เราสามารถทำได้โดยไม่กระทบกับการใช้งานจากภายนอก เพราะข้อมูลเหล่านั้นถูกห่อหุ้มไว้ภายในคลาส
#    - หากเราต้องการเพิ่มฟังก์ชันใหม่หรือเปลี่ยนวิธีการทำงานของหุ่นยนต์, ก็สามารถทำได้โดยไม่ต้องเปลี่ยนแปลงการเข้าถึงข้อมูลจากภายนอก

# **ข้อดีเพิ่มเติม**:
#  - สามารถทำให้ระบบมีความยืดหยุ่นมากขึ้น โดยการห่อหุ้มข้อมูลและการควบคุมการเข้าถึงทำให้เราสามารถเปลี่ยนแปลงรายละเอียดภายใน
#    ได้โดยไม่กระทบกับส่วนอื่น ๆ ของโปรแกรม
#  - ลดความซับซ้อนในการใช้งาน: ผู้ใช้ไม่ต้องรู้รายละเอียดภายในหุ่นยนต์ แต่สามารถใช้งานเมธอดที่ง่ายและสะดวก
#  - เสริมความปลอดภัย: เราสามารถตรวจสอบความถูกต้องของข้อมูลก่อนให้มีการปรับเปลี่ยน ทำให้ระบบปลอดภัยมากขึ้น

# สรุป:
# **Encapsulation** ช่วยให้เราสามารถควบคุมการเข้าถึงข้อมูลภายในคลาส ทำให้ข้อมูลภายในไม่ถูกเปลี่ยนแปลงจากภายนอก และเพิ่มความปลอดภัยในการจัดการข้อมูล
