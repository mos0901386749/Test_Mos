from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest
from selenium.webdriver.chrome.service import Service

#สำเร็จ
class RegisSuccessTest(unittest.TestCase):

    def setUp(self):
        # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
        service = Service('C:/Mos/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        # ปิดเบราว์เซอร์
        self.driver.quit()

    def test_Register_Success(self):

        self.driver.get("https://online-web-mauve.vercel.app/")
        
        register_button = self.driver.find_element(By.XPATH, "//span[text()='สมัครสมาชิก']")
        register_button.click()

        id_card_input = self.driver.find_element(By.XPATH, "//input[@name='id_card']")
        id_card_input.clear()
        id_card_input.send_keys("1111111111111")
        

        prefix_select = self.driver.find_element(By.XPATH, "//select[@name='prefix_name']")
        prefix_dropdown = Select(prefix_select)
        prefix_dropdown.select_by_value("นาย")
        

        first_name_input = self.driver.find_element(By.XPATH, "//input[@name='first_name']")
        first_name_input.clear()
        first_name_input.send_keys("สมจิตร")
        

        last_name_input = self.driver.find_element(By.XPATH, "//input[@name='last_name']")
        last_name_input.clear()
        last_name_input.send_keys("จองจอหอ")
        

        gender_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='gender']"))
        gender_dropdown.select_by_value("ชาย")
        

        birthday_input = self.driver.find_element(By.XPATH, "//input[@name='birthday']")
        birthday_input.clear()
        birthday_input.send_keys("10-09-1969")
        

        weight_input = self.driver.find_element(By.XPATH, "//input[@name='weight']")
        weight_input.clear()
        weight_input.send_keys("69")
        

        height_input = self.driver.find_element(By.XPATH, "//input[@name='height']")
        height_input.clear()
        height_input.send_keys("169")
        

        phone_input = self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']")
        phone_input.clear()
        phone_input.send_keys("0812345678")
        

        congenital_disease_input = self.driver.find_element(By.XPATH, "//input[@name='congenital_disease']")
        congenital_disease_input.clear()
        congenital_disease_input.send_keys("โรคหัวใจ")
        

        drugallergy_input = self.driver.find_element(By.XPATH, "//input[@name='drugallergy']")
        drugallergy_input.clear()
        drugallergy_input.send_keys("พารา")
        

        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.clear()
        password_input.send_keys("111111")
        

        contact_first_name_input = self.driver.find_element(By.XPATH, "//input[@name='contact_first_name']")
        contact_first_name_input.clear()
        contact_first_name_input.send_keys("สมใจ")
        

        contact_last_name_input = self.driver.find_element(By.XPATH, "//input[@name='contact_last_name']")
        contact_last_name_input.clear()
        contact_last_name_input.send_keys("จองจอหอ")
        

        relation_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='contact_relation_id']"))
        relation_dropdown.select_by_value("ภรรยา")
        

        contact_phone_input = self.driver.find_element(By.XPATH, "//input[@name='contact_phoneNumber']")
        contact_phone_input.clear()
        contact_phone_input.send_keys("0812512323")
        

        address_input = self.driver.find_element(By.XPATH, "//input[@name='address']")
        address_input.clear()
        address_input.send_keys("88")
        

        province_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='province']"))
        province_dropdown.select_by_value("สุพรรณบุรี")
        

        district_input = self.driver.find_element(By.XPATH, "//input[@name='district']")
        district_input.clear()
        district_input.send_keys("สองพี่น้อง")
        

        subdistrict_input = self.driver.find_element(By.XPATH, "//input[@name='subdistrict']")
        subdistrict_input.clear()
        subdistrict_input.send_keys("เนินพระปรางค์")
        

        postcode_input = self.driver.find_element(By.XPATH, "//input[@name='postcode']")
        postcode_input.clear()
        postcode_input.send_keys("72110")
        time.sleep(2)

        save_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-success mx-1' and contains(text(), 'บันทึก')]")
        save_button.click()
        time.sleep(3)

        confirm_button = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='ตกลง']")
        confirm_button.click()
        time.sleep(5)

#กรณี id_card ซ้ำ
class Id_cardTest(unittest.TestCase):

    def setUp(self):
        # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
        service = Service('C:/Mos/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        # ปิดเบราว์เซอร์
        self.driver.quit()

    def test_Register_idcard(self):

        self.driver.get("https://online-web-mauve.vercel.app/")
        
        register_button = self.driver.find_element(By.XPATH, "//span[text()='สมัครสมาชิก']")
        register_button.click()

        id_card_input = self.driver.find_element(By.XPATH, "//input[@name='id_card']")
        id_card_input.clear()
        id_card_input.send_keys("1111111111111")
        

        prefix_select = self.driver.find_element(By.XPATH, "//select[@name='prefix_name']")
        prefix_dropdown = Select(prefix_select)
        prefix_dropdown.select_by_value("นาย")
        

        first_name_input = self.driver.find_element(By.XPATH, "//input[@name='first_name']")
        first_name_input.clear()
        first_name_input.send_keys("สมจิตร")
        

        last_name_input = self.driver.find_element(By.XPATH, "//input[@name='last_name']")
        last_name_input.clear()
        last_name_input.send_keys("จองจอหอ")
        

        gender_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='gender']"))
        gender_dropdown.select_by_value("ชาย")
        

        birthday_input = self.driver.find_element(By.XPATH, "//input[@name='birthday']")
        birthday_input.clear()
        birthday_input.send_keys("10-09-1969")
        

        weight_input = self.driver.find_element(By.XPATH, "//input[@name='weight']")
        weight_input.clear()
        weight_input.send_keys("69")
        

        height_input = self.driver.find_element(By.XPATH, "//input[@name='height']")
        height_input.clear()
        height_input.send_keys("169")
        

        phone_input = self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']")
        phone_input.clear()
        phone_input.send_keys("0812345678")
        

        congenital_disease_input = self.driver.find_element(By.XPATH, "//input[@name='congenital_disease']")
        congenital_disease_input.clear()
        congenital_disease_input.send_keys("โรคหัวใจ")
        

        drugallergy_input = self.driver.find_element(By.XPATH, "//input[@name='drugallergy']")
        drugallergy_input.clear()
        drugallergy_input.send_keys("พารา")
        

        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.clear()
        password_input.send_keys("111111")
        

        contact_first_name_input = self.driver.find_element(By.XPATH, "//input[@name='contact_first_name']")
        contact_first_name_input.clear()
        contact_first_name_input.send_keys("สมใจ")
        

        contact_last_name_input = self.driver.find_element(By.XPATH, "//input[@name='contact_last_name']")
        contact_last_name_input.clear()
        contact_last_name_input.send_keys("จองจอหอ")
        

        relation_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='contact_relation_id']"))
        relation_dropdown.select_by_value("ภรรยา")
        

        contact_phone_input = self.driver.find_element(By.XPATH, "//input[@name='contact_phoneNumber']")
        contact_phone_input.clear()
        contact_phone_input.send_keys("0812512323")
        

        address_input = self.driver.find_element(By.XPATH, "//input[@name='address']")
        address_input.clear()
        address_input.send_keys("88")
        

        province_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='province']"))
        province_dropdown.select_by_value("สุพรรณบุรี")
        

        district_input = self.driver.find_element(By.XPATH, "//input[@name='district']")
        district_input.clear()
        district_input.send_keys("สองพี่น้อง")
        

        subdistrict_input = self.driver.find_element(By.XPATH, "//input[@name='subdistrict']")
        subdistrict_input.clear()
        subdistrict_input.send_keys("เนินพระปรางค์")
        

        postcode_input = self.driver.find_element(By.XPATH, "//input[@name='postcode']")
        postcode_input.clear()
        postcode_input.send_keys("72110")
        time.sleep(2)

        save_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-success mx-1' and contains(text(), 'บันทึก')]")
        save_button.click()
        time.sleep(3)

        confirm_button = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='ตกลง']")
        confirm_button.click()
        time.sleep(5)

#ไม่กรอก id card
class Register_NoIdcard(unittest.TestCase):

    def setUp(self):
        # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
        service = Service('C:/Mos/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        # ปิดเบราว์เซอร์
        self.driver.quit()

    def test_Register_noidcard(self):

        self.driver.get("https://online-web-mauve.vercel.app/")
        
        register_button = self.driver.find_element(By.XPATH, "//span[text()='สมัครสมาชิก']")
        register_button.click()

        id_card_input = self.driver.find_element(By.XPATH, "//input[@name='id_card']")
        id_card_input.clear()
        id_card_input.send_keys("")
        

        prefix_select = self.driver.find_element(By.XPATH, "//select[@name='prefix_name']")
        prefix_dropdown = Select(prefix_select)
        prefix_dropdown.select_by_value("นาย")
        

        first_name_input = self.driver.find_element(By.XPATH, "//input[@name='first_name']")
        first_name_input.clear()
        first_name_input.send_keys("มอส")
        

        last_name_input = self.driver.find_element(By.XPATH, "//input[@name='last_name']")
        last_name_input.clear()
        last_name_input.send_keys("สุปรานนท์")
        

        gender_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='gender']"))
        gender_dropdown.select_by_value("ชาย")
        

        birthday_input = self.driver.find_element(By.XPATH, "//input[@name='birthday']")
        birthday_input.clear()
        birthday_input.send_keys("12-12-2000")
        

        weight_input = self.driver.find_element(By.XPATH, "//input[@name='weight']")
        weight_input.clear()
        weight_input.send_keys("65")
        

        height_input = self.driver.find_element(By.XPATH, "//input[@name='height']")
        height_input.clear()
        height_input.send_keys("178")
        

        phone_input = self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']")
        phone_input.clear()
        phone_input.send_keys("0989751545")
        

        congenital_disease_input = self.driver.find_element(By.XPATH, "//input[@name='congenital_disease']")
        congenital_disease_input.clear()
        congenital_disease_input.send_keys("โรคภูมิแพ้")
        

        drugallergy_input = self.driver.find_element(By.XPATH, "//input[@name='drugallergy']")
        drugallergy_input.clear()
        drugallergy_input.send_keys("พารา")
        

        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.clear()
        password_input.send_keys("12122544")
        

        contact_first_name_input = self.driver.find_element(By.XPATH, "//input[@name='contact_first_name']")
        contact_first_name_input.clear()
        contact_first_name_input.send_keys("ภัทธรวดี")
        

        contact_last_name_input = self.driver.find_element(By.XPATH, "//input[@name='contact_last_name']")
        contact_last_name_input.clear()
        contact_last_name_input.send_keys("สุปรานนท์")
        

        relation_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='contact_relation_id']"))
        relation_dropdown.select_by_value("ภรรยา")
        

        contact_phone_input = self.driver.find_element(By.XPATH, "//input[@name='contact_phoneNumber']")
        contact_phone_input.clear()
        contact_phone_input.send_keys("08181475874")
        

        address_input = self.driver.find_element(By.XPATH, "//input[@name='address']")
        address_input.clear()
        address_input.send_keys("88")
        

        province_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='province']"))
        province_dropdown.select_by_value("สุพรรณบุรี")
        

        district_input = self.driver.find_element(By.XPATH, "//input[@name='district']")
        district_input.clear()
        district_input.send_keys("สองพี่น้อง")
        

        subdistrict_input = self.driver.find_element(By.XPATH, "//input[@name='subdistrict']")
        subdistrict_input.clear()
        subdistrict_input.send_keys("เนินพระปรางค์")
        

        postcode_input = self.driver.find_element(By.XPATH, "//input[@name='postcode']")
        postcode_input.clear()
        postcode_input.send_keys("72110")
        time.sleep(2)

        save_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-success mx-1' and contains(text(), 'บันทึก')]")
        save_button.click()
        time.sleep(3)

        confirm_button = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='ตกลง']")
        confirm_button.click()
        time.sleep(5)
        
#ไม่กรอกอะไรเลย
class Register_Nodata(unittest.TestCase):

    def setUp(self):
        # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
        service = Service('C:/Mos/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        # ปิดเบราว์เซอร์
        self.driver.quit()

    def test_Register_nodata(self):

        self.driver.get("https://online-web-mauve.vercel.app/")
        
        register_button = self.driver.find_element(By.XPATH, "//span[text()='สมัครสมาชิก']")
        register_button.click()

        id_card_input = self.driver.find_element(By.XPATH, "//input[@name='id_card']")
        id_card_input.clear()
        id_card_input.send_keys("")
        

        prefix_select = self.driver.find_element(By.XPATH, "//select[@name='prefix_name']")
        prefix_dropdown = Select(prefix_select)
        prefix_dropdown.select_by_value("")
        

        first_name_input = self.driver.find_element(By.XPATH, "//input[@name='first_name']")
        first_name_input.clear()
        first_name_input.send_keys("")
        

        last_name_input = self.driver.find_element(By.XPATH, "//input[@name='last_name']")
        last_name_input.clear()
        last_name_input.send_keys("")
        

        gender_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='gender']"))
        gender_dropdown.select_by_value("")
        

        birthday_input = self.driver.find_element(By.XPATH, "//input[@name='birthday']")
        birthday_input.clear()
        birthday_input.send_keys("")
        

        weight_input = self.driver.find_element(By.XPATH, "//input[@name='weight']")
        weight_input.clear()
        weight_input.send_keys("")
        

        height_input = self.driver.find_element(By.XPATH, "//input[@name='height']")
        height_input.clear()
        height_input.send_keys("")
        

        phone_input = self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']")
        phone_input.clear()
        phone_input.send_keys("")
        

        congenital_disease_input = self.driver.find_element(By.XPATH, "//input[@name='congenital_disease']")
        congenital_disease_input.clear()
        congenital_disease_input.send_keys("")
        

        drugallergy_input = self.driver.find_element(By.XPATH, "//input[@name='drugallergy']")
        drugallergy_input.clear()
        drugallergy_input.send_keys("")
        

        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.clear()
        password_input.send_keys("")
        

        contact_first_name_input = self.driver.find_element(By.XPATH, "//input[@name='contact_first_name']")
        contact_first_name_input.clear()
        contact_first_name_input.send_keys("")
        

        contact_last_name_input = self.driver.find_element(By.XPATH, "//input[@name='contact_last_name']")
        contact_last_name_input.clear()
        contact_last_name_input.send_keys("")
        

        relation_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='contact_relation_id']"))
        relation_dropdown.select_by_value("")
        

        contact_phone_input = self.driver.find_element(By.XPATH, "//input[@name='contact_phoneNumber']")
        contact_phone_input.clear()
        contact_phone_input.send_keys("")
        

        address_input = self.driver.find_element(By.XPATH, "//input[@name='address']")
        address_input.clear()
        address_input.send_keys("")
        

        province_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='province']"))
        province_dropdown.select_by_value("")
        

        district_input = self.driver.find_element(By.XPATH, "//input[@name='district']")
        district_input.clear()
        district_input.send_keys("")
        

        subdistrict_input = self.driver.find_element(By.XPATH, "//input[@name='subdistrict']")
        subdistrict_input.clear()
        subdistrict_input.send_keys("")
        

        postcode_input = self.driver.find_element(By.XPATH, "//input[@name='postcode']")
        postcode_input.clear()
        postcode_input.send_keys("")
        time.sleep(2)

        save_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-success mx-1' and contains(text(), 'บันทึก')]")
        save_button.click()
        time.sleep(3)

        confirm_button = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='ตกลง']")
        confirm_button.click()
        time.sleep(5)
        
class Register_passworld(unittest.TestCase):

    def setUp(self):
        # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
        service = Service('C:/Mos/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        # ปิดเบราว์เซอร์
        self.driver.quit()

    def test_Register_passworld(self):

        self.driver.get("https://online-web-mauve.vercel.app/")
        
        register_button = self.driver.find_element(By.XPATH, "//span[text()='สมัครสมาชิก']")
        register_button.click()

        id_card_input = self.driver.find_element(By.XPATH, "//input[@name='id_card']")
        id_card_input.clear()
        id_card_input.send_keys("1212121212121")
        

        prefix_select = self.driver.find_element(By.XPATH, "//select[@name='prefix_name']")
        prefix_dropdown = Select(prefix_select)
        prefix_dropdown.select_by_value("นาย")
        

        first_name_input = self.driver.find_element(By.XPATH, "//input[@name='first_name']")
        first_name_input.clear()
        first_name_input.send_keys("ณรงค์")
        

        last_name_input = self.driver.find_element(By.XPATH, "//input[@name='last_name']")
        last_name_input.clear()
        last_name_input.send_keys("สุปรานนท์")
        

        gender_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='gender']"))
        gender_dropdown.select_by_value("ชาย")
        

        birthday_input = self.driver.find_element(By.XPATH, "//input[@name='birthday']")
        birthday_input.clear()
        birthday_input.send_keys("12-12-2000")
        

        weight_input = self.driver.find_element(By.XPATH, "//input[@name='weight']")
        weight_input.clear()
        weight_input.send_keys("65")
        

        height_input = self.driver.find_element(By.XPATH, "//input[@name='height']")
        height_input.clear()
        height_input.send_keys("178")
        

        phone_input = self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']")
        phone_input.clear()
        phone_input.send_keys("0989751545")
        

        congenital_disease_input = self.driver.find_element(By.XPATH, "//input[@name='congenital_disease']")
        congenital_disease_input.clear()
        congenital_disease_input.send_keys("โรคภูมิแพ้")
        

        drugallergy_input = self.driver.find_element(By.XPATH, "//input[@name='drugallergy']")
        drugallergy_input.clear()
        drugallergy_input.send_keys("พารา")
        

        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.clear()
        password_input.send_keys("1212")
        

        contact_first_name_input = self.driver.find_element(By.XPATH, "//input[@name='contact_first_name']")
        contact_first_name_input.clear()
        contact_first_name_input.send_keys("ภัทธรวดี")
        

        contact_last_name_input = self.driver.find_element(By.XPATH, "//input[@name='contact_last_name']")
        contact_last_name_input.clear()
        contact_last_name_input.send_keys("สุปรานนท์")
        

        relation_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='contact_relation_id']"))
        relation_dropdown.select_by_value("ภรรยา")
        

        contact_phone_input = self.driver.find_element(By.XPATH, "//input[@name='contact_phoneNumber']")
        contact_phone_input.clear()
        contact_phone_input.send_keys("08181475874")
        

        address_input = self.driver.find_element(By.XPATH, "//input[@name='address']")
        address_input.clear()
        address_input.send_keys("88")
        

        province_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='province']"))
        province_dropdown.select_by_value("สุพรรณบุรี")
        

        district_input = self.driver.find_element(By.XPATH, "//input[@name='district']")
        district_input.clear()
        district_input.send_keys("สองพี่น้อง")
        

        subdistrict_input = self.driver.find_element(By.XPATH, "//input[@name='subdistrict']")
        subdistrict_input.clear()
        subdistrict_input.send_keys("เนินพระปรางค์")
        

        postcode_input = self.driver.find_element(By.XPATH, "//input[@name='postcode']")
        postcode_input.clear()
        postcode_input.send_keys("72110")
        time.sleep(2)

        save_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-success mx-1' and contains(text(), 'บันทึก')]")
        save_button.click()
        time.sleep(3)

        confirm_button = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='ตกลง']")
        confirm_button.click()
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()