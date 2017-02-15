import time
import unittest
import HTMLTestRunner, sys
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://test.eor.gosapi.ru/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)

class ASeleniumAutoTest_1(unittest.TestCase):
        def test_001_CreatedInEORDev(self):
            assert "Login" in driver.title
            _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
            elem = driver.find_element_by_id("LoginForm_username")
            elem.send_keys("Ipad")
            elem = driver.find_element_by_id("LoginForm_password")
            elem.send_keys("ipad")
            driver.save_screenshot('LoginPassPage.png')
            elem.send_keys(Keys.RETURN)

            print('1. Логинимся в систему')

        def test_002_Not500or404andLoginIsVisible(self):
            assert "500" not in driver.title  # проверка на 500/404 ошибку
            assert "404" not in driver.title
            _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

            print('2. Ожидаем окончания загрузки страниы рабочего стола')

        def test_003_OpenAllPjct(self):
            _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
            assert "ЭОР" in driver.title
            menu = driver.find_element_by_css_selector("i.entypo-menu")
            menu.click()
            time.sleep(5)
            allpj = driver.find_element_by_link_text("Все проекты")
            allpj.click()

            print('3. Переходим в раздел "Все проекты"')

        def test_004_Not500or404(self):
            assert "500" not in driver.title  # проверка на 500/404 ошибку
            assert "404" not in driver.title

            print('4. Загрузка прошла успешно ошибок 500/404 не обнаружено')

        def test_005_CreateNewBlock(self):
            time.sleep(4)
            _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
            btn1 = driver.find_element_by_id("create-cp")
            btn1.click()
            time.sleep(4)
            _ = driver.find_element_by_class_name('warn-cp')
            btn2 = driver.find_element_by_name("yt0")
            btn2.click()
            time.sleep(4)
            _ = driver.find_element_by_id('Checkpoint_TITLE_em_')

            print('5. Нажимаем кнопку "Создать", открывается форма создания блока,\n пытаемся подтвердить создание без заполнения обятательных полей')

        def test_006_CreateNewBlockRight(self):
            elemTitle = driver.find_element_by_id("Checkpoint_TITLE")
            elemTitle.send_keys("Создал Selenium _для редактирования")
            btn2 = driver.find_element_by_name("yt0")
            btn2.click()
            driver.save_screenshot('CreateNewBlock.png')

            print('6. Создаём блок заполняя все обязательные поля')

        def test_007_FindBlock(self):
            time.sleep(3)
            _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
            searchButton = driver.find_element_by_id('search-show')
            searchButton.click()
            textFild = driver.find_element_by_id('search-text')
            textFild.send_keys('Создал Selenium _для редактирования')
            textFild.send_keys(Keys.ENTER)
            time.sleep(3)

            print('7. Находим созданный блок')

        # редактируем блок
        def test_008_EditBlock(self):
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div[2]/div/table/tbody/tr/td[2]/button[1]')))
            editButton = driver.find_element_by_xpath('//div[2]/div[2]/div/table/tbody/tr/td[2]/button[1]')
            editButton.click()
            time.sleep(3)
            NewTitle = driver.find_element_by_id('Checkpoint_TITLE')
            NewTitle.send_keys(' edit ')
            plus = driver.find_element_by_css_selector('i.fa.fa-plus')
            plus.click()
            time.sleep(3)
            newCat = driver.find_element_by_id('Category_S_NAME')
            newCat.send_keys('1')
            catOk = driver.find_element_by_id('catOk')
            catOk.click()

            time.sleep(2)
            plus = driver.find_element_by_css_selector('i.fa.fa-plus')
            plus.click()
            time.sleep(2)
            newCat2 = driver.find_element_by_id('Category_S_NAME')
            newCat2.send_keys('2')
            time.sleep(3)
            driver.implicitly_wait(10)
            catOk2 = driver.find_element_by_id('catOk')
            catOk2.click()
            time.sleep(4)
            driver.save_screenshot('EditBlock.png')

            print('8. Редактируем форму блока')

        def test_009_NegativEditBlock(self):
            plus = driver.find_element_by_css_selector('i.fa.fa-plus')
            plus.click()
            driver.implicitly_wait(10)
            catOk = driver.find_element_by_id('catOk')
            catOk.click()
            negativMsg = driver.find_element_by_id('result').text == 'Не удалось сохранить категорию'
            time.sleep(3)
            driver.save_screenshot('NoCategories.png')
            catCancel = driver.find_element_by_id('catCancel')
            catCancel.click()

            print('9. Пытаемся добавить категорию без названия')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumAutoTest_1))
    # File
    buf = open("at_for_BLOCK_stand_test.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ/РЕДАКТИРОВАНИЕ БЛОКА стенд тест',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)