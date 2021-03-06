import time
import unittest
import HTMLTestRunner, sys

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
pgs = 'https://task.eor.gosapi.ru/pgs/'
dev = 'https://dev.eor.gosapi.ru/new/'
oracle = 'https://task.eor.gosapi.ru/oracle/'

driver.get(oracle)
driver.maximize_window()
wait = WebDriverWait(driver, 20)

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        time.sleep(4)
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)

        print('1. Логинимся в систему')

    def test_002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(5)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

        print('2. Логинимся в систему')

    def test_003_OpenAllPjct(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

        print('3. Переходим в раздел "Все проекты"')

    def test_004_Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('4. Загрузка прошла успешно ошибок 500/404 не обнаружено')

    def test_005_OpenForm(self):
        # new
        wait = WebDriverWait(driver, 20)
        time.sleep(4)
        wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(3)
        searchButton = driver.find_element_by_id('search-show').click()
        time.sleep(2)
        textFild = driver.find_element_by_id('search-text')#('html/body/div[1]/div[2]/div[4]/nav/div/div[2]/ul[8]/li[1]/input')
        textFild.send_keys('Создал Selenium _для редактирования')
        textFild.send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_xpath("//a[contains(text(),'Создал Selenium _для редактирования')]").click()
        # new fnc
        time.sleep(5)
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        btn1 = driver.find_element_by_id("create-cp")
        btn1.click()
        time.sleep(10)
        _ = driver.find_element_by_class_name('warn-cp')    #есть текст "Вы собираетесь создать проект."

        print('5. Находим блок, от него переходим в проект, нажимаем "Создать"')

    def test_006_SearchBlock(self):
        time.sleep(3)

        print('6. Ожидаем окончания загрузки формы проекта')

    def test_007_NewPjctFormBlock(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'btnCloseForm')))      #test
        _ = driver.find_element_by_xpath("//form/div/div[2]/div[1]/div/div[4]/b")
        nameOfpjct = driver.find_element_by_id("Checkpoint_TITLE")#.send_keys("Тестовый проект созданный Selenium")
        nameOfpjct.click()  #test
        nameOfpjct.send_keys("Тестовый проект созданный Selenium")
        time.sleep(3)
        _ = driver.find_element_by_class_name('warn-cp').text == 'проект'   # test
        initDown = driver.find_element_by_xpath("//div[@id='DIV_INITIATOR_ID']/div/span/span/span/span[2]").click()
        initName = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("Б" + Keys.ENTER)
        pjctManger = driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]").click()
        pjctMangerName = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("А" + Keys.ENTER)
        pjctCurator = driver.find_element_by_xpath("//div[@id='DIV_PROJECT_CURATOR']/div/span/span/span/span[2]").click()
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Б' + Keys.ENTER)

        print('7. Заполняем форму проекта')

    def test_008_ConfirmCreatingPjct(self):
        time.sleep(3)
        driver.find_element_by_name("yt0").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        CreateButton = driver.find_element_by_name("yt0").click()

        print('8. Подтверждаем создание проекта')

    def test_009_CheckPage(self):
        # проверить элементы на странице
        time.sleep(5)
        driver.set_page_load_timeout(5)
        _ = WebDriverWait(driver, 50)
        _ = wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        EditProject.click()

        print('9. ПРоверяем элементы в пасотре проекта и нажимаем редактировать')

    def test_010_editProject(self):
        time.sleep(4)
        ShortName = driver.find_element_by_id("Checkpoint_SHORT_NAME").send_keys("Краткое наименование")
        FullName = driver.find_element_by_id("Checkpoint_TITLE").send_keys(" edit ")
        SaveEdit = driver.find_element_by_name('yt0').click()

        print('10. Редактируем проект')

    def test_011_AllRight(self):
        time.sleep(4)
        _ = driver.find_element_by_id('C_TITLE').text == ' edit '
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('11. ПРоверяем, что изменения отображаются на форме проекта')

    def test_012_SeekAndDestroy(self):
       time.sleep(3)
       assert "ЭОР" in driver.title
       driver.find_element_by_id('search-text').clear()
       time.sleep(1)
       driver.find_element_by_id('search-text').send_keys('Тестовый проект созданный Selenium edit ')   #new text for search
       driver.find_element_by_id('search-text-push').click()    # Search click
       time.sleep(6)

       elemTestBlock = driver.find_element_by_xpath('//div[2]/div[2]/div/table/tbody/tr/td[1]/h4')
       elemTestBlock.click()
       time.sleep(3)
       DelProject = driver.find_element_by_xpath('//div[2]/div[2]/div[2]/table/tbody/tr/td[2]/button[2]')
       DelProject.click()
       time.sleep(2)
       elemNo = driver.find_element_by_xpath("//div[3]/div/button[2]")
       elemNo.click()
       DelProject.click()
       time.sleep(3)
       driver.implicitly_wait(10)
       elemYes = driver.find_element_by_xpath('//div[3]/div/button')
       elemYes.click()

       print('12. Находим проект заново через поиск, и удаляем его')
       time.sleep(2)
       driver.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_PROJECT_stand_ORACLE.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ ПРОЕКТА стенд тест',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)