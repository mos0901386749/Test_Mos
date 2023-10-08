from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
from selenium.webdriver.chrome.service import Service


#หาคิว
class JudkanQueueTest(unittest.TestCase):


    def setUp(self):
        # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
        service = Service('C:/Mos/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        # ปิดเบราว์เซอร์
        self.driver.quit()

    def test_Judkan_Queue(self):
        self.driver.get("https://online-web-mauve.vercel.app/")
    
    # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

    # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
        password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

    # กรอกข้อมูลใน input field
        id_input.send_keys("7777777777777")
        password_input.send_keys("123456")

    # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
        login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
        login_button.click()
        time.sleep(5)
    # รอ element ปรากฏด้วย WebDriverWait
        div_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "จัดการจองคิว")]'))
    )
    # คลิกที่ <div>
        div_element.click()
        time.sleep(5)

        birthday_input = self.driver.find_element(By.XPATH, "//input[@name='queue_date']")

        # ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
        birthday_input.clear()

        # กรอกวันที่ที่คุณต้องการ (ในรูปแบบ 'yyyy-mm-dd')
        birthday_input.send_keys("10-09-2023")  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
        time.sleep(5)

#update สถานะ ปกติเป็นยืนยัน
class JudkanQueueUpdate(unittest.TestCase):

            def setUp(self):
            # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
                service = Service('C:/Mos/chromedriver.exe')
                self.driver = webdriver.Chrome(service=service)
                self.driver.maximize_window()

            def tearDown(self):
            # ปิดเบราว์เซอร์
                self.driver.quit()

            def test_Judkan_Queue_Update(self):
                self.driver.get("https://online-web-mauve.vercel.app/")
    
    # คลิกปุ่ม "เข้าสู่ระบบ"
                open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
                open_modal_button.click()

    # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
                id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
                password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

    # กรอกข้อมูลใน input field
                id_input.send_keys("7777777777777")
                password_input.send_keys("123456")

    # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
                login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
                login_button.click()
                time.sleep(5)
    # รอ element ปรากฏด้วย WebDriverWait
                div_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "จัดการจองคิว")]'))
                )
    # คลิกที่ <div>
                div_element.click()
                time.sleep(5)

                birthday_input = self.driver.find_element(By.XPATH, "//input[@name='queue_date']")

                # ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
                birthday_input.clear()

        # กรอกวันที่ที่คุณต้องการ (ในรูปแบบ 'yyyy-mm-dd')
                birthday_input.send_keys("10-09-2023")  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
                time.sleep(5)

        # คลิกที่ <div>
                div_element.click()
                time.sleep(5)

        # คลิกที่ปุ่ม
                div_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.ID,"buttonStatus"))
                )
                div_element.click()
                time.sleep(3)

        # ระบุ element ของปุ่ม "ตกลง" ด้วย XPath
                confirm_button = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='อัพเดต']")

        # คลิกปุ่ม "ตกลง"
                confirm_button.click()
                time.sleep(5)


#update สถานะ ปกติเป็นเข้ารับการรักษา
class JudkanQueueUpdateStatus3(unittest.TestCase):

            def setUp(self):
            # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
                service = Service('C:/Mos/chromedriver.exe')
                self.driver = webdriver.Chrome(service=service)
                self.driver.maximize_window()

            def tearDown(self):
            # ปิดเบราว์เซอร์
                self.driver.quit()

            def test_Judkan_Queue_Update_3(self):
                self.driver.get("https://online-web-mauve.vercel.app/")
    
    # คลิกปุ่ม "เข้าสู่ระบบ"
                open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
                open_modal_button.click()

    # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
                id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
                password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

    # กรอกข้อมูลใน input field
                id_input.send_keys("7777777777777")
                password_input.send_keys("123456")

    # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
                login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
                login_button.click()
                time.sleep(5)
    # รอ element ปรากฏด้วย WebDriverWait
                div_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "จัดการจองคิว")]'))
                )
    # คลิกที่ <div>
                div_element.click()
                time.sleep(5)

                birthday_input = self.driver.find_element(By.XPATH, "//input[@name='queue_date']")

                # ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
                birthday_input.clear()

        # กรอกวันที่ที่คุณต้องการ (ในรูปแบบ 'yyyy-mm-dd')
                birthday_input.send_keys("10-09-2023")  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
                time.sleep(5)

        # คลิกที่ <div>
                div_element.click()
                time.sleep(5)

        # คลิกที่ปุ่ม
                div_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.ID,"buttonStatus"))
                )
                div_element.click()
                time.sleep(3)

        # ระบุ element ของปุ่ม "ตกลง" ด้วย XPath
                confirm_button = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='อัพเดต']")

        # คลิกปุ่ม "ตกลง"
                confirm_button.click()
                time.sleep(5)

#กดปุ่มดูบัตรคิว
class JudkanShowQueue(unittest.TestCase):

            def setUp(self):
            # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
                service = Service('C:/Mos/chromedriver.exe')
                self.driver = webdriver.Chrome(service=service)
                self.driver.maximize_window()

            def tearDown(self):
            # ปิดเบราว์เซอร์
                self.driver.quit()

            def test_Judkan_Show_Queue(self):
                self.driver.get("https://online-web-mauve.vercel.app/")
    
    # คลิกปุ่ม "เข้าสู่ระบบ"
                open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
                open_modal_button.click()

    # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
                id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
                password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

    # กรอกข้อมูลใน input field
                id_input.send_keys("7777777777777")
                password_input.send_keys("123456")

    # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
                login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
                login_button.click()
                time.sleep(5)
    # รอ element ปรากฏด้วย WebDriverWait
                div_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "จัดการจองคิว")]'))
                )
    # คลิกที่ <div>
                div_element.click()
                time.sleep(5)

                birthday_input = self.driver.find_element(By.XPATH, "//input[@name='queue_date']")

                # ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
                birthday_input.clear()

        # กรอกวันที่ที่คุณต้องการ (ในรูปแบบ 'yyyy-mm-dd')
                birthday_input.send_keys("10-09-2023")  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
                time.sleep(5)

        # คลิกที่ <div>
                div_element.click()
                time.sleep(5)

        # คลิกที่ปุ่ม
                div_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.ID,"Manager_button_print"))
                )
                div_element.click()
                time.sleep(3)

#Delete queue
class JudkanDeleteQueue(unittest.TestCase):

            def setUp(self):
            # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
                service = Service('C:/Mos/chromedriver.exe')
                self.driver = webdriver.Chrome(service=service)
                self.driver.maximize_window()

            def tearDown(self):
            # ปิดเบราว์เซอร์
                self.driver.quit()

            def test_Judkan_Delete_Queue(self):
                self.driver.get("https://online-web-mauve.vercel.app/")
    
    # คลิกปุ่ม "เข้าสู่ระบบ"
                open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
                open_modal_button.click()

    # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
                id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
                password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

    # กรอกข้อมูลใน input field
                id_input.send_keys("7777777777777")
                password_input.send_keys("123456")

    # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
                login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
                login_button.click()
                time.sleep(5)
    # รอ element ปรากฏด้วย WebDriverWait
                div_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "จัดการจองคิว")]'))
                )
    # คลิกที่ <div>
                div_element.click()
                time.sleep(5)

                birthday_input = self.driver.find_element(By.XPATH, "//input[@name='queue_date']")

                # ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
                birthday_input.clear()

        # กรอกวันที่ที่คุณต้องการ (ในรูปแบบ 'yyyy-mm-dd')
                birthday_input.send_keys("10-09-2023")  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
                time.sleep(5)

        # คลิกที่ <div>
                div_element.click()
                time.sleep(5)

        # คลิกที่ปุ่ม
                div_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.ID,"buttoCancels"))
                )
                div_element.click()
                time.sleep(3)

                # ระบุ element ของปุ่ม "ตกลง" ด้วย XPath
                confirm_button = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='ยืนยัน']")

        # คลิกปุ่ม "ตกลง"
                confirm_button.click()
                time.sleep(5)



if __name__ == "__main__":
    unittest.main()










