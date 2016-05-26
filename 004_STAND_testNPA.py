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
        time.sleep(2)
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
        time.sleep(2)

    def test_013ClickNPA(self):
        time.sleep(1)
        npa = driver.find_element_by_xpath("//div[@id='DIV_N_REALIZATION_TYPE']/div/span/span/span/span")
        npa.click()
        npa = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys('Норматив' + Keys.ENTER)
        time.sleep(1)
        pageDown = driver.find_element_by_xpath('//a/span[2]').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        editButton = driver.find_element_by_name('yt0').click()
        time.sleep(2)
        #editButton.click()

    def test_014CreateNPA(self):
        time.sleep(2)
        editButton = driver.find_element_by_name('yt0')
        editButton.click()
        time.sleep(2)
        crBtnclick = driver.find_element_by_xpath('//button[text()="Создать НПА"]').click()

    def test_015FillingNPAForm(self):
        time.sleep(4)
        assert "ЭОР" in driver.title
        # сокращение списка, выбираем правовые акты ДЭПР
        depr = driver.find_element_by_xpath('//div/div[2]/div[1]/div[2]/div[1]/div/span/span/span[2]').click()
        time.sleep(3)
        deprText = driver.find_element_by_link_text('Правовые акты ДЭПР').click()
        time.sleep(3)
        # приверим все обязательные поля
        finishButton = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/input[2]').click()
        time.sleep(3)
        # ответственный Согласование отраслевого управления
        responsibleName1 = driver.find_element_by_xpath("//div[@id='type_106']/div/div/div/span/span/span/span[2]").click()  # ответственный Согласование у руководителя департамента
        responsibleName1 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName1.send_keys('Башаев')
        responsibleName1.send_keys(Keys.ARROW_DOWN)
        responsibleName1.send_keys(Keys.ENTER)
        # проверим все обязательные элементы ещё раз
        time.sleep(1)
        driver.implicitly_wait(10)
        finishButton2 = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/input[2]').click()
        time.sleep(2)
        planDate1 = driver.find_element_by_id('date_106_75')#.click()  # срок исполнения Согласование отраслевого управления
        planDate1.send_keys('12345' + Keys.ENTER)

        # Получение согласований, определенных регламентами
        time.sleep(3)
        responsibleName2 = driver.find_element_by_xpath("//div[@id='type_106']/div[2]/div/div/span/span/span/span").click()  # ответственный Получение согласований, определенных регламентами
        responsibleName2 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName2.send_keys('Башаев' + Keys.ENTER)
        planDate2 = driver.find_element_by_id('date_106_76')  # срок исполнения Получение согласований, определенных регламентами
        planDate2.send_keys('12345' + Keys.ENTER)

        # Утверждение руководителя департамента
        time.sleep(3)
        responsibleName3 = driver.find_element_by_xpath("//div[@id='type_106']/div[3]/div/div/span/span/span/span[2]").click()  # ответственный Утверждение руководителя департамента
        responsibleName3 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName3.send_keys('Башаев' + Keys.ENTER)
        planDate3 = driver.find_element_by_id('date_106_83')  # срок исполнения Передача в правовое управление
        planDate3.send_keys('12345' + Keys.ENTER)
        time.sleep(2)
        editBtn = driver.find_element_by_name('yt0')
        editBtn.click()
        time.sleep(3)

    def test_016EditNPA(self):
        time.sleep(1)
        driver.implicitly_wait(10)
        editBtn = driver.find_element_by_name('yt0').click()
        time.sleep(3)

        # отчищаем обязательные поля в форме НПА
        responsibleName1 = driver.find_element_by_xpath("//div[@id='type_106']/div/div/div/span/span/span/span[2]").click()
        responsibleName1 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName1.send_keys('Не выбрано')
        responsibleName1.send_keys(Keys.ENTER)
        planDate1 = driver.find_element_by_id('date_106_75')
        planDate1.clear()
        planDate1.send_keys(Keys.ENTER)

        responsibleName2 = driver.find_element_by_xpath("//div[@id='type_106']/div[2]/div/div/span/span/span/span").click()
        responsibleName2 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName2.click()
        responsibleName2.send_keys('Не выбрано')
        responsibleName2.send_keys(Keys.ENTER)
        planDate2 = driver.find_element_by_id('date_106_76')
        planDate2.clear()
        planDate2.send_keys(Keys.ENTER)

        responsibleName3 = driver.find_element_by_xpath("//div[@id='type_106']/div[3]/div/div/span/span/span/span[2]").click()  # ответственный Утверждение руководителя департамента
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

        # подтверждаем невозможность создания
    def test_017FillingFormAgain(self):
        time.sleep(1)
        title = driver.find_element_by_id('Checkpoint_TITLE').send_keys('контрольная точка созданная Selenium')
        time.sleep(1)
        ASeleniumLogin_1.test_015FillingNPAForm(self)

    def test_018StatusCheck(self):
        time.sleep(1)
        driver.implicitly_wait(10)
        editBtn = driver.find_element_by_name('yt0').click()
        # 1 - исполнено
        status1 = driver.find_element_by_xpath('//form/div/div[2]/div[1]/div[2]/div[5]/div[1]/div[3]/div/div/div/label')
        status1.click()
        # 2 - просрочено
        status2 = driver.find_element_by_id('date_106_76')
        status2.clear()
        status2.send_keys('15.05.2016')
        # 3 - в процессе
        editBtn = driver.find_element_by_name('yt0')
        editBtn.click()
        time.sleep(2)
        driver.find_element_by_css_selector("img[alt='Просрочено']")                # просрочен
        #driver.find_element_by_partial_link_text("Срок исполнения (факт)")          # исполнен
        driver.find_element_by_css_selector("img[alt='В процессе исполнения']")     # в процессе

    def test_019AddCurrentState(self):
        addCS = driver.find_element_by_css_selector("div a[ data-original-title='Создать поручение']")
        addCS.click()
        wait.until(EC.element_to_be_clickable((By.ID, 'mission_form_save')))
        createAddCS = driver.find_element_by_id('mission_form_save')
        createAddCS.click()

        nameAddCS = driver.find_element_by_xpath('(//textarea[@id="Checkpoint_TITLE"])[2]')
        nameAddCS.click()
        nameAddCS.send_keys('Проверка поля Название')
        time.sleep(2)
        autorName = driver.find_element_by_xpath('//div[2]/form/div[2]/div/span/span')
        autorName.click()
        autorName.send_keys('Багреева')
        autorName.send_keys(Keys.ENTER)
        time.sleep(2)
        responsibleName = driver.find_element_by_xpath('//div[2]/form/div[3]/div/span/span[1]/span/span[2]')
        responsibleName.click()
        responsibleName = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName.click()
        time.sleep(1)
        responsibleName.send_keys('А')
        responsibleName.send_keys(Keys.ENTER)
        time.sleep(2)
        # date = driver.find_element_by_xpath('(//input[@id="Checkpoint_DEADLINE]")[2]')
        date = driver.find_element_by_xpath("//form[@id='npa-mission-form']/div[5]/div/input")
        date.click()
        date.send_keys('12345')
        date.send_keys(Keys.ENTER)
        createAddCS.click()

    def test_020delNPA(self):
        time.sleep(3)
        delButton = driver.find_element_by_name('yt1')
        delButton.click()
        time.sleep(1)
        yesButton = driver.find_element_by_xpath('//div[3]/div/button').click()

        print(' finish!')



if __name__ == '__main__':
    unittest.main()
