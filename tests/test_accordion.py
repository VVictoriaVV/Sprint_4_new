import allure
from page_object.main_page import MainPage
from page_object.base_page import BasePage


class TestAccordionElements:

    @allure.title('Первый вопрос')
    def test_one_question(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_one_question()
        assert main_page.get_one_answer_text() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Второй вопрос')
    def test_two_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_on_two_question()
        assert main_page.get_two_answer_text() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Третий вопрос')
    def test_three_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_on_three_question()
        assert main_page.get_three_answer_text() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Четвертый вопрос')
    def test_four_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_four_question()
        assert main_page.get_four_answer_text() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Пятый вопрос')
    def test_five_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_five_question()
        assert main_page.get_five_answer_text() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Шестой вопрос')
    def test_six_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_six_question()
        assert main_page.get_six_answer_text() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Седьмой вопрос')
    def test_seven_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_seven_question()
        assert main_page.get_seven_answer_text() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Восьмой вопрос')
    def test_eight_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_eight_question()
        assert main_page.get_eight_answer_text() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

