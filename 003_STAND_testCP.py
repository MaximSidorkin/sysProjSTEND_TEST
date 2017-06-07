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

driver.get(pgs)
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

        print('\n 1. Логинимся в ЭОР')

    def test_002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'hidden-xs')))

        print('\n 2. Ждем пока страница загрузится проверяем на 500/404')

    def test_003_OpenAllPjct(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

        print('\n 3. переходим в раздел все проекты')

    def test_004_Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 4. Подтверждаем, что страница успешно загрузилась')

    def test_005_OpenForm(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(1)
        driver.implicitly_wait(20)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.implicitly_wait(20)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 5. В поиске по ключевому слову selenium находим блок')

    def test_006_FindBlock(self):
        #находим блок
        findBlock = driver.find_element_by_link_text('Создал Selenium _для редактирования')
        findBlock.click()
        time.sleep(1)
        driver.implicitly_wait(20)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 6. Переходим от блока к проекту')

    def test_007_FindProject(self):
        #находим проект
        findProject = driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span')
        findProject.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 7. переходим от проекта к контрольным точкам')
    def test_008_CreateCP(self):
        #создаем контрольную точку
        CreateCP = driver.find_element_by_id('create-cp')
        CreateCP.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 8. нажимаем кнопку "Создать"')

    def test_009_FillingCPForm(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'  # test
        time.sleep(2)
        driver.implicitly_wait(20)
        #имя контрольной точки
        nameCP = driver.find_element_by_id('Checkpoint_TITLE').send_keys("контрольная точка созданная Selenium")
        time.sleep(2)
        driver.implicitly_wait(20)
        #автор
        autorName = driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]")
        autorName.click()
        autorNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        autorNameText.send_keys('Б' + Keys.ENTER)
        time.sleep(3)
        driver.implicitly_wait(20)
        #ответственный
        #сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 9. Находим кнопку "Сохранить"')

    def test_010_TriggersCPTest(self):
        time.sleep(3)
        driver.implicitly_wait(20)
        EditProject = driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 10. Сохраняем новую контрольную точку')

    def test_011_ConfirmCPCreating(self):
        finishButton = driver.find_element_by_name('yt0')
        finishButton.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(4)

        print('\n 11. Нажимаем кнопку "редактировать" на паспорте контрольной точки')

    def test_012_ClickEditButton(self):
        driver.implicitly_wait(20)
        editButton = driver.find_element_by_name('yt0').click()
        time.sleep(5)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 12. вносим изменения в контрольную точку и сохраняем')

    def test_013_editCP(self):
        driver.implicitly_wait(20)
        time.sleep(2)
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'
        nameCP = driver.find_element_by_id('Checkpoint_TITLE')
        nameCP.click()
        nameCP.send_keys(' редактировано ')
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        saveButton = driver.find_element_by_name('yt0')
        saveButton.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 13. Подтверждаем, что изменения отображаются в \n паспорте контрольной точки')

    def test_014_AllRight(self):
        time.sleep(3)
        driver.implicitly_wait(20)
        _ = driver.find_element_by_id('C_TITLE').text == ' редактировано '
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 14. Создаём копию контрольной точки')

    def test_015_DelCP(self):
        DelCP = driver.find_element_by_name('yt2').click()
        time.sleep(1)
        driver.implicitly_wait(20)
        elemYes = driver.find_element_by_xpath('html/body/div[5]/div[3]/div/button[1]')
        elemYes.click()

        print('\n 15. Удаляем контрольную точку')
        time.sleep(2)
        driver.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_CHECKPOINT_stand_test.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ КОНТРОЛЬНОЙ ТОЧКИ стенд тест',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)