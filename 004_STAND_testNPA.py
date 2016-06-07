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
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
    def test_2FindBlock(self):
        #находим блок
        findBlock = driver.find_element_by_link_text('Создал Selenium _для редактирования')
        findBlock.click()
        time.sleep(1)
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
        #имя контрольной точки
        nameCP = driver.find_element_by_id('Checkpoint_TITLE').send_keys("контрольная точка созданная Selenium")
        time.sleep(2)
        #автор
        autorName = driver.find_element_by_xpath('//div[10]/div/span/span/span/span[2]')
        autorName.click()
        autorNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        autorNameText.send_keys('Б' + Keys.ENTER)
        time.sleep(2)
        #ответственный
        responsibleName = driver.find_element_by_xpath('//div[11]/div/span/span/span/span[2]')
        responsibleName.click()
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleNameText.send_keys('А' + Keys.ENTER)
        time.sleep(2)
        #сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    if __name__ == '__main__':
        unittest.main()

    def test_2TriggersCPTest(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        #туда
        driver.implicitly_wait(20)
        triggerKPI = driver.find_element_by_css_selector('span.switch-right')
        triggerKPI.click()
        time.sleep(2)
        triggerPriority = driver.find_element_by_xpath('//div[19]/div/div/div/span[2]')
        triggerPriority.click()
        time.sleep(2)
        triggerDone = driver.find_element_by_xpath('//div[20]/div/div/div/span[2]')
        triggerDone.click()
        time.sleep(2)
        #и обратно
        driver.implicitly_wait(20)
        #triggerKPI = driver.find_element_by_xpath('//div[18]/div/div/div/label')
        #triggerKPI.click()
        time.sleep(2)
        triggerPriority.click()
        time.sleep(2)
        triggerDone.click()
        time.sleep(2)

        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_3ConfirmCPCreating(self):
        driver.implicitly_wait(20)
        finishButton = driver.find_element_by_name('yt0').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(5)

class ESeleniumEditCP(unittest.TestCase):
    def test_1ClickEditButton(self):
        driver.implicitly_wait(20)
        editButton = driver.find_element_by_name('yt0').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)

    def test_2editCP(self):
        driver.implicitly_wait(20)
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        triggerPrior = driver.find_element_by_xpath("//div[19]/div/div/div/label").click()
        triggerDone = driver.find_element_by_xpath("//div[20]/div/div/div/label").click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_3NPACreate(self):
        time.sleep(3)
        nap = driver.find_element_by_xpath("//div[17]/div/span/span[1]/span/span[1]").click()
        # nap = driver.find_element_by_xpath("//div[16]/div/span/span/span/span[2]").click()
        time.sleep(2)
        nap = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("Норматив" + Keys.ENTER)
        time.sleep(2)
        driver.implicitly_wait(20)
        EditProject = driver.find_element_by_name('yt0').click()
        time.sleep(3)
        driver.implicitly_wait(20)
        EditProject = driver.find_element_by_name('yt0').click()
        time.sleep(2)
        assert "ЭОР" in driver.title
        NPACr = driver.find_element_by_xpath('//button[text()="Создать НПА"]').click()
        time.sleep(2)

    def test_4NPAFillingForm(self):
        time.sleep(4)
        assert "ЭОР" in driver.title
        # сокращение списка, выбираем правовые акты ДЭПР
        depr = driver.find_element_by_xpath('//div/div[2]/div[1]/div[2]/div[1]/div/span/span/span[2]')
        depr.click()
        time.sleep(3)
        deprText = driver.find_element_by_link_text('Правовые акты ДЭПР')
        deprText.click()
        time.sleep(3)
        # приверим все обязательные поля
        createButton = driver.find_element_by_id('create-cp')
        #createButton.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        finishButton = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/input[2]')
        finishButton.click()
        time.sleep(4)
        # ответственный Согласование отраслевого управления
        responsibleName1 = driver.find_element_by_xpath('//div[5]/div/div/div/span/span/span/span[2]').click()  # ответственный Согласование у руководителя департамента
        responsibleName1 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName1.send_keys('А')
        #responsibleName1.send_keys(Keys.ARROW_DOWN)
        responsibleName1.send_keys(Keys.ENTER)
        # проверим все обязательные элементы ещё раз
        createButton.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.implicitly_wait(10)
        finishButton2 = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/input[2]')
        #finishButton2 = driver.implicitly_wait(10)
        finishButton2.click()
        time.sleep(4)
        planDate1 = driver.find_element_by_id('date_106_75')# срок исполнения Согласование отраслевого управления
        planDate1.click()
        planDate1.send_keys('12345')
        planDate1.send_keys(Keys.ENTER)

        # Получение согласований, определенных регламентами
        time.sleep(4)
        driver.implicitly_wait(20)
        responsibleName2 = driver.find_element_by_xpath('//div[5]/div[2]/div/div/span/span/span/span[2]') # ответственный Получение согласований, определенных регламентами
        responsibleName2.click()
        responsibleName2 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName2.click()
        responsibleName2.send_keys('А')
        responsibleName2.send_keys(Keys.ENTER)
        planDate2 = driver.find_element_by_id('date_106_76')# срок исполнения Получение согласований, определенных регламентами
        planDate2.click()
        planDate2.send_keys('12345')
        planDate2.send_keys(Keys.ENTER)

        # Утверждение руководителя департамента
        time.sleep(3)
        responsibleName3 = driver.find_element_by_xpath('//div[5]/div[3]/div/div/span/span/span/span[2]')# ответственный Утверждение руководителя департамента
        responsibleName3.click()
        responsibleName3 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName3.click()
        responsibleName3.send_keys('А')
        responsibleName3.send_keys(Keys.ENTER)
        planDate3 = driver.find_element_by_id('date_106_83')# срок исполнения Передача в правовое управление
        planDate3.click()
        planDate3.send_keys('12345')
        planDate3.send_keys(Keys.ENTER)

    def test_5EditNPA(self):
        time.sleep(4)
        assert "ЭОР" in driver.title
        editBtn = driver.find_element_by_name('yt0')
        editBtn.click()
        time.sleep(3)
        driver.implicitly_wait(20)
        editBtn = driver.find_element_by_name('yt0')
        editBtn.click()
        # отчищаем обязательные поля в форме НПА
        driver.implicitly_wait(20)
        responsibleName1 = driver.find_element_by_xpath('//div[5]/div/div/div/span/span/span/span[2]')
        responsibleName1.click()
        responsibleName1 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName1.send_keys('Не выбрано')
        responsibleName1.send_keys(Keys.ENTER)
        planDate1 = driver.find_element_by_id('date_106_75')
        planDate1.clear()
        planDate1.send_keys(Keys.ENTER)

        driver.implicitly_wait(20)
        responsibleName2 = driver.find_element_by_xpath('//div[5]/div[2]/div/div/span/span/span/span[2]')
        responsibleName2.click()
        responsibleName2 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName2.click()
        responsibleName2.send_keys('Не выбрано')
        responsibleName2.send_keys(Keys.ENTER)
        planDate2 = driver.find_element_by_id('date_106_76')
        planDate2.clear()
        planDate2.send_keys(Keys.ENTER)

        driver.implicitly_wait(20)
        responsibleName3 = driver.find_element_by_xpath('//div[5]/div[3]/div/div/span/span/span/span[2]')# ответственный Утверждение руководителя департамента
        responsibleName3.click()
        responsibleName3 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName3.click()
        responsibleName3.send_keys('Не выбрано')
        responsibleName3.send_keys(Keys.ENTER)
        planDate3 = driver.find_element_by_id('date_106_83')
        planDate3.clear()
        planDate3.send_keys(Keys.ENTER)

        CheckPiontID = driver.find_element_by_id('Checkpoint_TITLE')
        CheckPiontID.clear()

        editBtn = driver.find_element_by_name('yt0')
        editBtn.click()

        #подтверждаем невозможность создания

    def test_6NPANotCreate(self):
        time.sleep(3)
        driver.implicitly_wait(20)
        driver.find_element_by_id('cp_title')
        assert "ЭОР" in driver.title
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_7FillingFormAgain(self):
        time.sleep(2)
        assert "ЭОР" in driver.title
        driver.implicitly_wait(20)
        ESeleniumEditCP.test_4NPAFillingForm(self)
        time.sleep(3)
        driver.implicitly_wait(20)
        CheckPiontID = driver.find_element_by_id('Checkpoint_TITLE')
        CheckPiontID.click()
        CheckPiontID.send_keys('Контрольная точка для НПА')

    def test_8StatusCheck(self):
        # 1 - исполнено
        status1 = driver.find_element_by_xpath('//div[5]/div/div[3]/div/div/div/span[2]').click()
        # 2 - просрочено
        status2 = driver.find_element_by_id('date_106_76')
        status2.clear()
        status2.send_keys('15.05.2016')
        # 3 - в процессе
        driver.implicitly_wait(20)
        editBtn = driver.find_element_by_name('yt0')
        editBtn.click()
        time.sleep(4)
        driver.implicitly_wait(20)
        driver.find_element_by_css_selector("img[alt='Просрочено']")                # просрочен
        #driver.find_element_by_partial_link_text("Срок исполнения (факт)")          # исполнен
        driver.find_element_by_css_selector("img[alt='В процессе исполнения']")     # в процессе

    def test_9AddCurrentState(self):
        addCS = driver.find_element_by_css_selector("div a[ data-original-title='Создать поручение']")
        addCS.click()
        wait.until(EC.element_to_be_clickable((By.ID, 'mission_form_save')))
        createAddCS = driver.find_element_by_id('mission_form_save')
        createAddCS.click()

        nameAddCS = driver.find_element_by_xpath('(//textarea[@id="Checkpoint_TITLE"])[2]')
        nameAddCS.click()
        nameAddCS.send_keys('Проверка поля Название')
        time.sleep(4)
        driver.implicitly_wait(20)
        autorName = driver.find_element_by_xpath('//div[2]/form/div[2]/div/span/span')
        autorName.click()
        autorName.send_keys('Багреева')
        autorName.send_keys(Keys.ENTER)
        time.sleep(4)
        driver.implicitly_wait(20)
        responsibleName = driver.find_element_by_xpath('//div[2]/form/div[3]/div/span/span[1]/span/span[2]')
        responsibleName.click()
        responsibleName = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName.click()
        responsibleName.send_keys('А')
        responsibleName.send_keys(Keys.ENTER)
        time.sleep(4)
        driver.implicitly_wait(20)
        #date = driver.find_element_by_xpath('(//input[@id="Checkpoint_DEADLINE]")[2]')
        date = driver.find_element_by_xpath ("//form[@id='npa-mission-form']/div[5]/div/input")
        date.click()
        date.send_keys('12345')
        date.send_keys(Keys.ENTER)
        createAddCS.click()

        time.sleep(2)
        driver.implicitly_wait(20)
        delButton = driver.find_element_by_name('yt1').click()
        time.sleep(2)
        driver.implicitly_wait(20)
        yesButton = driver.find_element_by_xpath('//div[3]/div/button').click()

        print(' finish!')

if __name__ == '__main__':
    unittest.main()