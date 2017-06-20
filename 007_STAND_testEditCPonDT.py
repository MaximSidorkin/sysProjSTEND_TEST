# СОЗДАНИЕ И РЕДАКТИРВОАНИЕ КОНТРОЛЬНОЙ ТОЧКИ НА РАБОЧЕМ СТОЛЕ
import time, unittest, HTMLTestRunner, sys, datetime

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#
oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'
dev = 'https://dev.eor.gosapi.ru/new/site/login'

driver = webdriver.Chrome()
driver.get(pgs)
driver.maximize_window()
wait = WebDriverWait(driver, 40)
test_time = datetime.datetime.now()
test_day = test_time.day
test_month = test_time.month

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        driver.find_element_by_id("LoginForm_username").send_keys('ipad')
        driver.find_element_by_id("LoginForm_password").send_keys('ipad'+Keys.RETURN)
        print('Логинимся в систему')

    def test_002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print('Ожидаем окончания загрузки страницы рабочего стола\n - страница загружена успешно')

    def test_003_CreateCPfromDT(self):
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='cps_panel']/div/div/ul/div/a/i").click()
        time.sleep(2)
        print('На рабочем столе выбираем создать контрольную\n точку путем нажатия кнопки "+"')

    def test_004_FillingCPForm(self):
        #имя родителя
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.fa.fa-angle-down')))
        driver.find_element_by_css_selector("i.fa.fa-angle-down").click()
        driver.find_element_by_css_selector("input.form-control").send_keys("Selenium")
        driver.find_element_by_css_selector('span.find-text').click()
        #имя контрольной точки
        driver.find_element_by_id('Checkpoint_TITLE').send_keys("Создание и редактирование контрольной точки на рабочем столе Selenium")
        #ответственный
        driver.find_element_by_xpath("//div[5]/div/span/span/span/span[2]").click()
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Selenium' + Keys.ENTER)
        # new responsible name
        driver.find_element_by_xpath('//div[6]/div/span/span/span/span[2]').click()
        driver.find_element_by_xpath('//span/input').send_keys('Selenium' + Keys.ENTER)
        #сроки
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('123' + Keys.ENTER)
        driver.find_element_by_xpath("//div/div[3]/span[2]").click()
        print('Заполняем форму контрольной точки')

    def test_005_EditResponsible(self):
        # Отвественный
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'D_ID_RESPONSIBLE')))
        driver.find_element_by_id('D_ID_RESPONSIBLE').click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'select2-selection__arrow')))
        driver.find_element_by_class_name('select2-selection__arrow').click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'select2-search__field')))
        driver.find_element_by_class_name('select2-search__field').send_keys('иванов и'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('//button[2]').click()
        print("Изменяем ответственного")

    def test_006_EditDate(self):
        # Срок исполнения (план)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'D_DEADLINE')))
        driver.find_element_by_id('D_DEADLINE').click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'Checkpoint_DEADLINE')))
        driver.find_element_by_id('Checkpoint_DEADLINE').clear()
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys(test_day+2,'.',test_month,'.','2017'+Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath("//span[@id='E_DEADLINE']/div/button[2]").click()
        print("Изменяем срок исполнения - сегодняшний день +1")

    def test_007_EditName(self):
        # Название контрольной точки
        driver.find_element_by_id('D_TITLE').click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'Checkpoint_TITLE')))
        driver.find_element_by_id('Checkpoint_TITLE').send_keys(' РЕДАКТИРОВАНО ',test_day,'/',test_month)
        time.sleep(1)
        driver.find_element_by_xpath('//button[2]').click()
        print("Изменяем название контрольной точки")

    def test_008_HideParams(self):
        # Скрытые доп. параметры
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='cp_passport']/div/div[2]/div/div[3]").click()
        print("Открываем скрытые параметры")

    def test_009_EditExecutor(self):
        # Исполнитель
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'D_ID_EXECUTOR')))
        driver.find_element_by_id('D_ID_EXECUTOR').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[2]/span[2]/span/form/span/span/span/span').click()
        time.sleep(1)
        driver.find_element_by_css_selector('input.select2-search__field').send_keys('Анашкина Н.В.'+Keys.ENTER)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='E_ID_EXECUTOR']/div/button[2]")))
        driver.find_element_by_xpath("//span[@id='E_ID_EXECUTOR']/div/button[2]").click()
        print('Редактируем поле "Исполнитель"')

    def test_010_CheckChanges(self):
        # открыть вкладку "Ближайшие" и проверить корректность внесённых изменений
        driver.find_element(By.XPATH, ".//*[text()='Ближайшие']/..").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Selenium Qa.").send_keys(Keys.PAGE_DOWN)  # +Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Selenium Qa.").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Selenium Qa.").send_keys(Keys.PAGE_DOWN)
        try:
            driver.find_element_by_link_text('Анашкина Н.В.')
            print('Ответственный корретно изменён')
        except:
            print('\nNO TEXT')
        try:
            _ = driver.find_element_by_id('D_DEADLINE').text == test_day+2,test_month,'2017'
            print('Дата корретно изменена')
        except:
            print("\nNO DATE")
        driver.find_element_by_name('yt2').click()
        print('После проверки корректности внесённых изменений удаляем контрольную точку')
        driver.find_element_by_xpath("//div[3]/div/button").click()
        time.sleep(3)
        t = driver.find_element_by_css_selector('div.toast-message')
        print(t.text)

        driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_CREATE_AND_EDIT_CP_IN_DT.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ И РЕДАКТИРОВАНИЕ КОНТРОЛЬНОЙ ТОЧКИ НА РАБОЧЕМ СТОЛЕ',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)
