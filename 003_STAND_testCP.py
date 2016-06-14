import time
import unittest
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://test.eor.gosapi.ru/site/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

class ASeleniumLogin_1(unittest.TestCase):
    def test_1LoginInEORDev(self):
        assert "Login" in driver.title
        #wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
    def test_2Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

        if __name__ == '__main__':
            unittest.main()

class BSeleniumOpenAllPjct_2(unittest.TestCase):
    def test_1OpenAllPjct(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

    if __name__ == '__main__':
        unittest.main()

    def test_2Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        if __name__ == '__main__':
            unittest.main()

class CSeleniumCreateNewCP(unittest.TestCase):
    def test_1OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        btn1 = driver.find_element_by_id("create-cp")
        btn1.click()
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
    def test_2FindBlock(self):
        #находим блок
        findBlock = driver.find_element_by_link_text('Создал Selenium _для редактирования')
        findBlock.click()
        time.sleep(1)
        driver.implicitly_wait(20)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_3FindProject(self):
        #находим проект
        findProject = driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span')
        findProject.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_4CreateCP(self):
        #создаем контрольную точку
        CreateCP = driver.find_element_by_id('create-cp')
        CreateCP.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    if __name__ == '__main__':
        unittest.main()

class DSeleniumTestCPForm(unittest.TestCase):
    def test_1FillingCPForm(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'  # test
        time.sleep(2)
        driver.implicitly_wait(20)
        #имя контрольной точки
        nameCP = driver.find_element_by_id('Checkpoint_TITLE').send_keys("контрольная точка созданная Selenium")
        time.sleep(2)
        driver.implicitly_wait(20)
        #автор
        autorName = driver.find_element_by_xpath('//div[10]/div/span/span[1]/span/span[1]')
        autorName.click()
        autorNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        autorNameText.send_keys('Б' + Keys.ENTER)
        time.sleep(3)
        driver.implicitly_wait(20)
        #ответственный
        responsibleName = driver.find_element_by_xpath('//div[11]/div/span/span[1]/span/span[1]')
        responsibleName.click()
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleNameText.send_keys('Б' + Keys.ENTER)
        time.sleep(4)
        driver.implicitly_wait(20)
        #сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title


    def test_2TriggersCPTest(self):

        time.sleep(3)
#
        driver.implicitly_wait(20)
        EditProject = driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

#
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_3ConfirmCPCreating(self):
        finishButton = driver.find_element_by_name('yt0')
        finishButton.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(4)

class ESeleniumEditCP(unittest.TestCase):
    def test_1ClickEditButton(self):
        driver.implicitly_wait(20)
        editButton = driver.find_element_by_name('yt0').click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)


    def test_2editCP(self):
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

    def test_3AllRight(self):
        time.sleep(3)
        driver.implicitly_wait(20)
        _ = driver.find_element_by_id('C_TITLE').text == ' редактировано '
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

class FSeleniumSeekAndDestroy(unittest.TestCase):
    def test_1DelCP(self):
        DelCP = driver.find_element_by_name('yt2').click()
        time.sleep(1)
        driver.implicitly_wait(20)
        elemYes = driver.find_element_by_xpath('html/body/div[5]/div[3]/div/button[1]')
        elemYes.click()
'''
    def test_1FilterSetting(self):
        assert "ЭОР" in driver.title

        FilterSetting = driver.find_element_by_xpath('html/body/div[1]/div[2]/div[4]/nav/div/div[2]/ul[2]/li/a/span')
        FilterSetting.click()
        time.sleep(1)
        SnipClick = driver.find_element_by_link_text('Багреева').click()
        #SnipClick.click()
        #SnipClick = driver.find_element_by_xpath('//nav/div/div[2]/ul[2]/li/ul/li[3]/div/ul/li[1]/div/label[1]/div')
        #SnipClick.click()
        ConfirmFilter = driver.find_element_by_xpath('//div[1]/div[2]/div[4]/nav/div/div[2]/ul[2]/li/ul/li[4]/button[2]')
        ConfirmFilter.click()
        driver.implicitly_wait(20)
        time.sleep(3)

    def test_2TextFilterSetting(self):
        ClearText = driver.find_element_by_css_selector('span.clear').click()
        FindNew = driver.find_element_by_id('search-text').send_keys('контрольная точка созданная Selenium редактировано ' + Keys.ENTER)
        time.sleep(2)

    def test_3BlockAndProjectListing(self):
        driver.implicitly_wait(20)
        findBlock = driver.find_element_by_xpath('//div[2]/div[4]/div[2]/div[2]/div/table/tbody/tr/td[1]/h4/strong/a')
        findBlock.click()
        time.sleep(2)
        driver.implicitly_wait(20)
        findProject = driver.find_element_by_xpath('//div[2]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a')
        findProject.click()
        time.sleep(2)

    def test_4DelCPAndConfirmThis(self):
        #_ = driver.find_element_by_xpath('//div[2]/div[4]/div[2]/div[2]/div[3]/div/div[1]/div/h4/a/div/span').text == 'контрольная точка созданная Selenium редактировано'
        DelCP = driver.find_element_by_xpath('//div[2]/div[4]/div[2]/div[2]/div[3]/div/div[1]/div/div/button[3]')
        DelCP.click()
        time.sleep(1)
        driver.implicitly_wait(20)
        elemNo = driver.find_element_by_xpath("//div[3]/div/button[2]")
        elemNo.click()
        DelCP.click()
        driver.implicitly_wait(20)
        time.sleep(1)
        elemYes = driver.find_element_by_xpath('//div[3]/div/button')
        elemYes.click()


        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        unittest.removeResult()
        '''
if __name__ == '__main__':
    unittest.main()