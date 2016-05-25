import time
import unittest
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://test.eor.gosapi.ru/site/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

class ASeleniumLogin_1(unittest.TestCase):
    def test_001LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
    def test_002Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

    def test_003OpenAllPjct(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(4)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

    def test_004Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_005OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        btn1 = driver.find_element_by_id("create-cp")
        btn1.click()
        time.sleep(1)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('selenium')
        elemSearch.send_keys(Keys.ENTER)
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_006FindBlock(self):
        #находим блок
        findBlock = driver.find_element_by_link_text('Создал Selenium')
        findBlock.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_007FindProject(self):
        #находим проект
        findProject = driver.find_element_by_link_text("Проект создал Selenium")
        findProject.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_008CreateCP(self):
        #создаем контрольную точку
        CreateCP = driver.find_element_by_xpath('html/body/div[1]/div[2]/div[4]/nav/div/div[2]/ul[7]/li/button')
        CreateCP.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_009FillingCPForm(self):
        time.sleep(2)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'  # test
        time.sleep(1)
        #имя контрольной точки
        nameCP = driver.find_element_by_xpath('//div[2]/div[2]/div[4]/form/div/div[2]/div[4]/div/textarea')
        nameCP.click()
        nameCP.send_keys("контрольная точка созданная Selenium")
        time.sleep(1)
        #автор
        autorName = driver.find_element_by_xpath('//form/div/div[2]/div[8]/div/span/span[1]/span/span[2]')
        autorName.click()
        autorNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        autorNameText.send_keys('Башаев' + Keys.ENTER)
        time.sleep(1)
        #ответственный
        responsibleName = driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span").click()
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('Башаев' + Keys.ENTER)
        time.sleep(1)
        #responsibleNameText.send_keys(Keys.ENTER)
        time.sleep(1)
        #сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE')
        terms.click()
        terms.send_keys("12345")
        terms.send_keys(Keys.ENTER)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_010TriggersCPTest(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        #туда
        triggerKPI = driver.find_element_by_xpath('//div[2]/div[4]/form/div/div[2]/div[17]/div/div/div/label')
        triggerKPI.click()
        time.sleep(1)
        triggerPriority = driver.find_element_by_xpath('//div[2]/div[4]/form/div/div[2]/div[18]/div/div/div/label')
        triggerPriority.click()
        time.sleep(1)
        triggerDone = driver.find_element_by_xpath('//div[2]/div[4]/form/div/div[2]/div[19]/div/div[1]/div/label')
        triggerDone.click()
        time.sleep(1)
        #и обратно
        triggerKPI.click()
        time.sleep(1)
        triggerPriority.click()
        time.sleep(1)
        triggerDone.click()
        time.sleep(1)

        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_011ConfirmCPCreating(self):
        finishButton = driver.find_element_by_xpath('//div[2]/div[2]/div[4]/form/div/div[2]/div[23]/input[2]')
        finishButton.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)

    def test_012ClickEditButton(self):
        editButton = driver.find_element_by_name('yt0')
        editButton.click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)


    def test_013editCP(self):
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'
        nameCP = driver.find_element_by_xpath('//form/div/div[2]/div[4]/div/textarea')
        nameCP.click()
        nameCP.send_keys(' редактировано ')
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        saveButton = driver.find_element_by_xpath('//div[2]/div[2]/div[4]/div/div/form/div/div[2]/div[23]/input[2]')
        saveButton.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_014AllRight(self):
        time.sleep(3)
        _ = driver.find_element_by_id('C_TITLE').text == ' редактировано '
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_015SeekAndDestroy(self):
        time.sleep(2)
        destrBtn = driver.find_element_by_name('yt2').click()
        time.sleep(2)
        _ = driver.find_element_by_xpath("//div[3]/div/button").click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "Error" not in driver.title

if __name__ == '__main__':
    unittest.main()
