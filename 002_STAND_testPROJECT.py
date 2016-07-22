import time
import unittest
global str
import page_objects

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://test.eor.gosapi.ru/")
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

class CSeleniumCreateNewPjct_3(unittest.TestCase):
    def test_1OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        btn1 = driver.find_element_by_id("create-cp")
        btn1.click()
        time.sleep(5)
        _ = driver.find_element_by_class_name('warn-cp')    #есть текст "Вы собираетесь создать блок."
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div/div[1]/div[1]/span/i')))
        btn1 = driver.find_element_by_xpath('//div/div[1]/div[1]/span/i')
        btn1.click()

    if __name__ == '__main__':
        unittest.main()

    def test_2SearchBlock(self):
        SrcSelenBlock = driver.find_element_by_xpath('//form/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/input')
        SrcSelenBlock.send_keys('Selenium')
        time.sleep(3)
        GetTarget = driver.find_element(By.CLASS_NAME, "find-text").click()
        time.sleep(3)

    if __name__ == '__main__':
        unittest.main()

    def test_3NewPjctFormBlock(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'btnCloseForm')))      #test
        _ = driver.find_element_by_xpath("//form/div/div[2]/div[1]/div/div[4]/b")
        nameOfpjct = driver.find_element_by_id("Checkpoint_TITLE")#.send_keys("Тестовый проект созданный Selenium")
        nameOfpjct.click()  #test
        nameOfpjct.send_keys("Тестовый проект созданный Selenium")
        time.sleep(3)
        _ = driver.find_element_by_class_name('warn-cp').text == 'проект'   # test
        autorDown = driver.find_element_by_xpath("//div[@id='DIV_AUTHOR_MISSION']/div/span/span/span/span[2]").click()
        autorName = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("б" + Keys.ENTER)
        pjctMansger = driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]").click()
        pjctMansgerName = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("а" + Keys.ENTER)

    def test_5ConfirmCreatingPjct(self):
        time.sleep(1)
        CreateButton = driver.find_element_by_name("yt0").click()

class DSeleniumEditProject(unittest.TestCase):
    def test_1CheckPage(self):
        # проверить элементы на странице
        time.sleep(5)
        driver.set_page_load_timeout(5)
        _ = WebDriverWait(driver, 50)
        _ = wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        EditProject.click()

    def test_2editProject(self):
        time.sleep(4)
        ShortName = driver.find_element_by_id("Checkpoint_SHORT_NAME").send_keys("Краткое наименование")
        FullName = driver.find_element_by_id("Checkpoint_TITLE").send_keys(" edit ")
        SaveEdit = driver.find_element_by_name('yt0').click()

    if __name__ == '__main__':
        unittest.main()

    def test_3AllRight(self):
        time.sleep(4)
        _ = driver.find_element_by_id('C_TITLE').text == ' edit '
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_4SeekAndDestroy(self):
       time.sleep(3)
       assert "ЭОР" in driver.title
       elem = driver.find_element_by_link_text('Поиск')
       elem.click()
       time.sleep(3)
       elemSearch = driver.find_element_by_id('search-text')
       elemSearch.click()
       elemSearch.send_keys('Тестовый проект созданный Selenium edit ')
       elemSearch.send_keys(Keys.ENTER)
       time.sleep(2)
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

    if __name__ == '__main__':
        unittest.main()





