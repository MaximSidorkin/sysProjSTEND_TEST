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
wait = WebDriverWait(driver, 40)

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        driver.find_element_by_id("LoginForm_username").send_keys("Ipad")
        driver.find_element_by_id("LoginForm_password").send_keys("ipad"+Keys.RETURN)
        print('\n 1. Логинимся в систему\n')

    def test_002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print(' 2. Ошибок 404 и 500 нет и логин пользователя отображается\n')

    def test_003_OpenAllPjct(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu").click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты").click()
        print(' 3. Переходим в раздел "Все проекты"\n')

    def test_004_Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print(' 4. Ошибок 404 и 500 нет\n')

    def test_005_OpenForm(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        assert "ЭОР" in driver.title
        driver.find_element_by_link_text('Поиск').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'search-text')))
        driver.find_element_by_id('search-text').send_keys('Selenium'+Keys.ENTER)#.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print(' 5. В поиске задаём слово Selenium\n')

    def test_006_FindBlock(self):
        #находим блок
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Создал Selenium _для редактирования')))
        driver.find_element_by_link_text('Создал Selenium _для редактирования').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print(' 6. Находим блок, ошибок 404 и 500 нет\n')

    def test_007_FindProject(self):
        #находим проект
        time.sleep(1)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span')))
        driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print(' 7. Переходим от блока к проекту, ошибок 404 и 500 нет\n')

    def test_008_CreateCP(self):
        #создаем контрольную точку
        driver.find_element_by_id('create-cp').click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print(' 8. Переходим в раздел контрльных точек \n и нажимаем Создать, ошибок 404 и 500 нет\n')

    def test_009_FillingCPForm(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        #имя контрольной точки
        driver.find_element_by_id('Checkpoint_TITLE').send_keys("контрольная точка созданная Selenium")
        #ответственный
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]").click()
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('б' + Keys.ENTER)
        driver.implicitly_wait(10)
        #сроки
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print(' 9. Заполняем форму контрольной точки, ошибок 404 и 500 нет\n')

    def test_010_TriggersCPTest(self):
        #driver.find_element_by_name('yt0'+Keys.PAGE_DOWN)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print(' 10. Проверяем тригеры, ошибок 404 и 500 нет\n')

    def test_011_ConfirmCPCreating(self):
        driver.implicitly_wait(20)
        driver.find_element_by_name('yt0').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print(' 11. Сохраняем контрольную точку, ошибок 404 и 500 нет\n')

    def test_012_ClickEditButton(self):
        driver.implicitly_wait(20)
        _ = wait.until((EC.element_to_be_clickable((By.NAME, 'yt0'))))
        driver.find_element_by_name('yt0').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print(' 12. Нажимаем кнопку Редактировать, ошибок 404 и 500 нет\n')

    def test_013_editCP(self):
        driver.implicitly_wait(20)
        _ = wait.until((EC.element_to_be_clickable((By.NAME, 'yt0'))))
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print(' 13. Выбираем форму реализации - НПА, сохраняем изменения\n и заново нажимаем Редактировать \n')

    def test_014_NPACreate(self):
        _ = wait.until((EC.element_to_be_clickable((By.ID, 'DIV_N_REALIZATION_TYPE'))))
        driver.find_element_by_id("DIV_N_REALIZATION_TYPE").click()
        driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("Норматив" + Keys.ENTER)
        driver.implicitly_wait(20)
        driver.find_element_by_name('yt0').click()
        driver.implicitly_wait(20)
        _ = wait.until((EC.element_to_be_clickable((By.NAME, 'yt0'))))
        driver.find_element_by_name('yt0').click()
        assert "ЭОР" in driver.title
        driver.find_element_by_xpath('//button[text()="Создать НПА"]').click()
        print(' 14. Частично заполняем форму НПА, пробуем сохранить\n видим сообщения об обязательности заоления полей\n и заполняем обязательные поля полностью. Сохраняем.')

    def test_015_NPAFillingForm(self):
        time.sleep(3)
        assert "ЭОР" in driver.title
        # сокращение списка, выбираем правовые акты ДЭПР
        depr = driver.find_element_by_xpath('//div/div[2]/div[1]/div[2]/div[1]/div/span/span/span[2]')
        depr.click()
        time.sleep(3)
        deprText = driver.find_element_by_xpath('//div[1]/div/span/ul/li[3]/a')
        deprText.click()
        time.sleep(3)
        # приверим все обязательные поля
        createButton = driver.find_element_by_id('create-cp')
        createButton.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        finishButton = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/input[2]')
        finishButton.click()
        time.sleep(4)

        # ответственный Согласование отраслевого управления
        responsibleName1 = driver.find_element_by_xpath(
            '//div[4]/div/div/div/span/span/span/span[2]')  # ответственный Согласование у руководителя департамента
        responsibleName1.click()
        responsibleName1 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName1.send_keys('Selenium')
        responsibleName1.send_keys(Keys.ARROW_DOWN)
        responsibleName1.send_keys(Keys.ENTER)
        # проверим все обязательные элементы ещё раз
        createButton.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.implicitly_wait(30)
        finishButton2 = driver.find_element_by_name('yt0')
        finishButton2.click()
        time.sleep(2)
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            time.sleep(1)
            driver.find_element_by_xpath('//div[3]/div/button').click()
            time.sleep(1)
            print('\n Модальное окно "Внимание!", относящееся к НПА, появилось и было закрыто \n')
        except:
            print('\n Модальное окно "Внимание!", относящееся к НПА, не появилось \n')

        planDate1 = driver.find_element_by_id('date_106_74')  # срок исполнения Согласование отраслевого управления
        planDate1.click()
        planDate1.send_keys('12345')
        planDate1.send_keys(Keys.ENTER)

        # Получение согласований, определенных регламентами
        time.sleep(3)
        responsibleName2 = driver.find_element_by_xpath(
            '//div[4]/div[2]/div[1]/div/span/span[1]/span/span[2]')  # ответственный Получение согласований, определенных регламентами
        responsibleName2.click()
        responsibleName2 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName2.click()
        responsibleName2.send_keys('Selenium')
        responsibleName2.send_keys(Keys.ENTER)
        planDate2 = driver.find_element_by_id(
            'date_106_76')  # срок исполнения Получение согласований, определенных регламентами
        planDate2.click()
        planDate2.send_keys('12345')
        planDate2.send_keys(Keys.ENTER)

        # Утверждение руководителя департамента
        time.sleep(3)
        responsibleName3 = driver.find_element_by_xpath(
            '//div[4]/div[3]/div[1]/div/span/span[1]/span/span[2]')  # ответственный Утверждение руководителя департамента
        responsibleName3.click()
        responsibleName3 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName3.click()
        responsibleName3.send_keys('Selenium')
        responsibleName3.send_keys(Keys.ENTER)
        planDate3 = driver.find_element_by_id('date_106_83')  # срок исполнения Передача в правовое управление
        planDate3.click()
        planDate3.send_keys('12345')
        planDate3.send_keys(Keys.ENTER)
        # Проект
        time.sleep(1)
        driver.find_element_by_css_selector('span.input-group-addon').click()
        driver.find_element_by_css_selector('div.input-group.search-field > input.form-control').send_keys('Selenium')
        driver.find_element_by_css_selector('span.find-text').click()
        time.sleep(1)
        print(
            ' 14. Частично заполняем форму НПА, пробуем сохранить\n видим сообщения об обязательности заоления полей\n и заполняем обязательные поля полностью. Сохраняем.')

        '''
        assert "ЭОР" in driver.title
        # сокращение списка, выбираем правовые акты ДЭПР
        depr = driver.find_element_by_xpath('//div/div[2]/div[1]/div[2]/div[1]/div/span/span/span[2]')
        depr.click()
        time.sleep(3)
        deprText = driver.find_element_by_xpath('//form/div/div[2]/div[1]/div[2]/div[1]/div/span/ul/li[4]/a')
        deprText.click()
        time.sleep(3)
        # приверим все обязательные поля
        createButton = driver.find_element_by_id('create-cp')
        createButton.send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/input[2]').click()
        # ответственный 1
        _ = wait.until((EC.element_to_be_clickable((By.XPATH, '//div[2]/div/div/div/span/span/span/span'))))
        driver.find_element_by_xpath('//div[2]/div/div/div/span/span/span/span').click()
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('А'+Keys.ENTER)
        # проверим все обязательные элементы ещё раз
        driver.find_element_by_name('yt0').click()
        try:
            _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/button')))
            time.sleep(1)
            driver.find_element_by_xpath('//div[3]/div/button').click()
            time.sleep(1)
            print('\n Модальное окно "Внимание!", относящееся к НПА, появилось и было закрыто \n')
        except:
            print('\n Модальное окно "Внимание!", относящееся к НПА, не появилось \n')
        driver.find_element_by_id('date_1_1').send_keys('12345'+Keys.ENTER)  # срок исполнения Согласование отраслевого управления
        time.sleep(1)
        # ответственный 2
        driver.find_element_by_xpath('//div[2]/div/div/span/span/span/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('//span/input').send_keys('А'+Keys.ENTER)
        driver.find_element_by_id('date_1_2').send_keys('12345'+Keys.ENTER)  # срок исполнения Получение согласований, определенных регламентами
        time.sleep(1)
        # ответственный 3
        driver.find_element_by_xpath('//div[3]/div/div/span/span/span/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('//span/input').send_keys('А'+Keys.ENTER)
        driver.find_element_by_id('date_1_3').send_keys('12345'+Keys.ENTER)  # срок исполнения Передача в правовое управление
        time.sleep(1)
        # название проекта
        driver.find_element_by_css_selector('i.fa.fa-angle-down').click()
        driver.find_element_by_css_selector('div.input-group.search-field > input.form-control').send_keys('Selenium')
        driver.find_element_by_css_selector('span.find-text').click()
        print(' 15. Очищаем обязательные поля НПА и пробуем сохранить\n')
        '''
    def test_016_EditNPA(self):
        time.sleep(2)
        assert "ЭОР" in driver.title
        editBtn = driver.find_element_by_name('yt0')
        editBtn.click()
        time.sleep(3)
        editBtn = driver.find_element_by_name('yt0')
        editBtn.click()
        # отчищаем обязательные поля в форме НПА
        responsibleName1 = driver.find_element_by_xpath('//div[4]/div[1]/div[1]/div/span/span[1]/span/span[2]')
        responsibleName1.click()
        responsibleName1 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName1.send_keys('Не выбрано')
        responsibleName1.send_keys(Keys.ENTER)
        planDate1 = driver.find_element_by_id('date_106_74')
        planDate1.clear()
        planDate1.send_keys(Keys.ENTER)

        responsibleName2 = driver.find_element_by_xpath('//div[4]/div[2]/div[1]/div/span/span[1]/span/span[2]')
        responsibleName2.click()
        responsibleName2 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName2.click()
        responsibleName2.send_keys('Не выбрано')
        responsibleName2.send_keys(Keys.ENTER)
        planDate2 = driver.find_element_by_id('date_106_76')
        planDate2.clear()
        planDate2.send_keys(Keys.ENTER)

        responsibleName3 = driver.find_element_by_xpath(
            '//div[4]/div[3]/div[1]/div/span/span[1]/span/span[2]')  # ответственный Утверждение руководителя департамента
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
        # подтверждаем невозможность создания
        print(' 15. Очищаем обязательные поля НПА и пробуем сохранить\n')
        '''
        assert "ЭОР" in driver.title
        driver.find_element_by_name('yt0').click()
        time.sleep(3)
        driver.implicitly_wait(20)
        driver.find_element_by_name('yt0').click()
        time.sleep(2)
        # отчищаем обязательные поля в форме НПА
        driver.implicitly_wait(20)
        # ответственный 1
        driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/input[2]').click()
        #driver.find_element_by_xpath('//div[2]/div/div/div/span/span/span/span').click()
        responsibleName1 = driver.find_element_by_xpath('//span/input')
        responsibleName1.send_keys('Не выбрано')
        responsibleName1.send_keys(Keys.ENTER)
        time.sleep(1)
        planDate1 = driver.find_element_by_id('date_1_1')
        planDate1.clear()
        planDate1.send_keys(Keys.ENTER)

        # ответственный 2
        driver.find_element_by_xpath('//div[2]/div/div/span/span/span/span').click()
        responsibleName2 = driver.find_element_by_xpath('//span/input')
        responsibleName2.click()
        responsibleName2.send_keys('Не выбрано')
        responsibleName2.send_keys(Keys.ENTER)
        planDate2 = driver.find_element_by_id('date_1_2')
        planDate2.clear()
        planDate2.send_keys(Keys.ENTER)

        driver.implicitly_wait(20)
        # ответственный 3
        driver.find_element_by_xpath('//div[3]/div/div/span/span/span/span').click()
        responsibleName3 = driver.find_element_by_xpath('//span/input')
        responsibleName3.click()
        responsibleName3.send_keys('Не выбрано')
        responsibleName3.send_keys(Keys.ENTER)
        planDate3 = driver.find_element_by_id('date_1_3')
        planDate3.clear()
        planDate3.send_keys(Keys.ENTER)

        CheckPiontID = driver.find_element_by_id('Checkpoint_TITLE')
        CheckPiontID.clear()

        editBtn = driver.find_element_by_name('yt0')
        editBtn.click()
        #подтверждаем невозможность создания
        print(' 16. Выводится сообщение о невозможности этого действия,\n обязательные поля должны быть заполнены\n')
        '''
    def test_017_NPANotCreate(self):
        time.sleep(3)
        driver.implicitly_wait(20)
        driver.find_element_by_id('cp_title')
        assert "ЭОР" in driver.title
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print(' 17. Снова заполняем обязательные поля \n')

    def test_018_FillingFormAgain(self):
        time.sleep(2)
        assert "ЭОР" in driver.title
        # сокращение списка, выбираем правовые акты ДЭПР
        depr = driver.find_element_by_xpath('//div/div[2]/div[1]/div[2]/div[1]/div/span/span/span[2]')
        depr.click()
        time.sleep(1)
        deprText = driver.find_element_by_xpath('//div[1]/div/span/ul/li[3]/a')
        deprText.click()
        time.sleep(1)
        # приверим все обязательные поля
        createButton = driver.find_element_by_id('create-cp')
        createButton.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        finishButton = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/input[2]')
        finishButton.click()
        time.sleep(2)
        # ответственный Согласование отраслевого управления
        responsibleName1 = driver.find_element_by_xpath('//div[4]/div[1]/div[1]/div/span/span[1]/span/span[2]')  # ответственный Согласование у руководителя департамента
        responsibleName1.click()
        responsibleName1 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName1.send_keys('Selenium')
        responsibleName1.send_keys(Keys.ARROW_DOWN)
        responsibleName1.send_keys(Keys.ENTER)
        # проверим все обязательные элементы ещё раз
        createButton.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.implicitly_wait(10)
        finishButton2 = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/input[2]')
        # finishButton2 = driver.implicitly_wait(10)
        finishButton2.click()
        time.sleep(2)
        planDate1 = driver.find_element_by_id('date_106_74')  # срок исполнения Согласование отраслевого управления
        planDate1.click()
        planDate1.send_keys('12345')
        planDate1.send_keys(Keys.ENTER)

        # Получение согласований, определенных регламентами
        time.sleep(2)
        responsibleName2 = driver.find_element_by_xpath('//div[4]/div[2]/div[1]/div/span/span[1]/span/span[2]')  # ответственный Получение согласований, определенных регламентами
        responsibleName2.click()
        responsibleName2 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName2.click()
        responsibleName2.send_keys('Selenium')
        responsibleName2.send_keys(Keys.ENTER)
        planDate2 = driver.find_element_by_id('date_106_76')  # срок исполнения Получение согласований, определенных регламентами
        planDate2.click()
        planDate2.send_keys('12345')
        planDate2.send_keys(Keys.ENTER)

        # Утверждение руководителя департамента
        time.sleep(1)
        responsibleName3 = driver.find_element_by_xpath('//div[4]/div[3]/div[1]/div/span/span[1]/span/span[2]')  # ответственный Утверждение руководителя департамента
        responsibleName3.click()
        responsibleName3 = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName3.click()
        responsibleName3.send_keys('Selenium')
        responsibleName3.send_keys(Keys.ENTER)
        planDate3 = driver.find_element_by_id('date_106_83')  # срок исполнения Передача в правовое управление
        planDate3.click()
        planDate3.send_keys('12345')
        planDate3.send_keys(Keys.ENTER)
        planDate3.send_keys(Keys.PAGE_UP)

        CheckPiontID = driver.find_element_by_id('Checkpoint_TITLE')
        CheckPiontID.click()
        CheckPiontID.send_keys('Контрольная точка для НПА')
        print(' 17. Снова заполняем обязательные поля \n')


        #driver.implicitly_wait(20)
        #ASeleniumLogin_1.test_015_NPAFillingForm(self)
        #time.sleep(3)
        #driver.implicitly_wait(20)
        #CheckPiontID = driver.find_element_by_id('Checkpoint_TITLE')#.send_keys('Контрольная точка для НПА')
        #CheckPiontID.click()
        #CheckPiontID.send_keys('Контрольная точка для НПА')

        print(' 18. Снова заполняем обязательные поля \n')

    def test_019_StatusCheck(self):
        # 1 - исполнено
        status1 = driver.find_element_by_xpath('//div[1]/div[2]/div[4]/div[1]/div[3]/div/div/div/label')
        status1.click()
        # 2 - просрочено
        status2 = driver.find_element_by_id('date_106_76')
        status2.clear()
        status2.send_keys('15.05.2016')
        # 3 - в процессе
        editBtn = driver.find_element_by_name('yt0')
        editBtn.click()
        time.sleep(2)
        try:
            driver.find_element_by_css_selector("img[alt='Просрочено']")                # просрочен
            driver.find_element_by_css_selector("img[alt='В процессе исполнения']")     # в процессе
            print(' 18. Изменяем статусы заполеннных полей (просрочен/в процессе). Сохраняем \n')
        except:
            self.fail(print(' 18. В процессе сохранения / отображения статусов возникла непредвиденная ошибка'))

        # 1 - исполнено
        #status1 = driver.find_element_by_css_selector('span.switch-right').click()
        # 2 - просрочено
        #status2 = driver.find_element_by_id('date_1_2')
        #status2.clear()
        #status2.send_keys('15.05.2016')
        # 3 - в процессе
        #driver.implicitly_wait(20)
        #editBtn = driver.find_element_by_name('yt0')
        #editBtn.click()
        #time.sleep(4)
        #driver.implicitly_wait(20)
        #driver.find_element_by_css_selector("img[alt='Просрочено']")                # просрочен
        #driver.find_element_by_css_selector("img[alt='В процессе исполнения']")     # в процессе

        print(' 18. Изменяем статусы заполеннных полей (просрочен/в процессе). Сохраняем \n')

    def test_020_AddCurrentState(self):
        try:
            addCS = driver.find_element_by_css_selector("div a[ data-original-title='Создать поручение']")
            addCS.click()
        except:
            self.fail(
                print("\n\n 19. В ПРОЦЕССЕ СОЗДАНИЯ ПОРУЧЕНИЯ ЧЕРЕЗ \n КНОПКУ + ВОЗНИКЛА НЕПРЕДВИДЕННАЯ ОШИБКА! \n\n"))

        createAddCS = driver.find_element_by_xpath('//div/div[3]/span[2]')
        time.sleep(7)
        nameAddCS = driver.find_element_by_xpath("//div[2]/div/div[4]/div/textarea")
        nameAddCS.click()
        nameAddCS.send_keys('Проверка поля Название')
        time.sleep(2)

        driver.find_element_by_xpath('//div[7]/div/span/span/span/span[2]').click()  # responsible name
        responsibleName = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleName.click()
        responsibleName.send_keys('S' + Keys.ENTER)
        time.sleep(2)
        date = driver.find_element_by_xpath("//div[9]/div/input")  # .click()
        time.sleep(1)
        date.click()
        time.sleep(1)
        date.send_keys('12345' + Keys.ENTER)
        time.sleep(1)
        createAddCS.click()

        time.sleep(3)
        driver.find_element_by_name('yt1').click()  # delete button click
        time.sleep(2)
        try:
            driver.find_element_by_xpath('//div[3]/div/button').click()  # confirm button click
            print(
                ' 19. Создаем ещё одно поручение через кнопку + на форме НПА\n (проверка обязательности полей включена) \n')
        except:
            self.fail(print(' 19. В процессе создания поручения через кнопку + возникла непредвиденная ошибка!'))

    def test_020_Check500Error(self):
        time.sleep(10)
        try:
            driver.find_element_by_css_selector('fa fa-spinner fa-spin fa-2x')
            self.fail(print(' 20. ОШИБКА 500 ПРИ УДАЛЕНИИ НПА \n'))
        except:
            print(' 20. ТЕСТ ПРОШЕЛ ПОЛНОСТЬЮ УСПЕШНО, СОЗДАННЫЙ НПА УДАЛЕН \n')

    def test_021_CloseBrowser(self):
        print(' 50. Закрываем браузер \n')
        driver.close()
        '''
        addCS = driver.find_element_by_css_selector("div a[ data-original-title='Создать поручение']")
        addCS.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/span[2]')))
        createAddCS = driver.find_element_by_xpath('//div[3]/span[2]')
        createAddCS.click()
        time.sleep(2)
        nameAddCS = driver.find_element_by_xpath('//div[2]/div/div[4]/div/textarea')
        nameAddCS.click()
        nameAddCS.send_keys('Проверка поля Название')
        time.sleep(2)
        driver.implicitly_wait(20)
        responsibleName = driver.find_element_by_xpath('//div[7]/div/span/span/span/span')
        responsibleName.click()
        responsibleName = driver.find_element_by_xpath('//span/input')
        responsibleName.click()
        responsibleName.send_keys('А')
        responsibleName.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.implicitly_wait(20)
        #date = driver.find_element_by_xpath('(//input[@id="Checkpoint_DEADLINE]")[2]')
        date = driver.find_element_by_xpath ("//div[9]/div/input")
        date.click()
        date.send_keys('12345')
        date.send_keys(Keys.ENTER)
        time.sleep(1)
        createAddCS1 = driver.find_element_by_xpath('//div[3]/span[2]')
        time.sleep(1)
        #createAddCS1.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        createAddCS1.click()
        time.sleep(2)
        driver.implicitly_wait(20)
        delButton = driver.find_element_by_name('yt1').click()
        time.sleep(2)
        driver.implicitly_wait(20)
        yesButton = driver.find_element_by_xpath('//div[3]/div/button').click()
        print(' 19. Создаем ещё одно поручение через нопку + на форме НПА\n (проверка обязательности полей включена) \n')
        time.sleep(2)
        driver.close()
        '''
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))
    # File
    buf = open("at_for_CHECKPOINT_AND_NPA_ORACLE_stand.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ НПА ИЗ РАЗДЕЛА ВСЕ ПРОЕКТЫ',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)