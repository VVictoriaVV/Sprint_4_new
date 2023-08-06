from selenium.webdriver.common.by import By


class MainPageLocators:

    title_questions_about_important = [By.XPATH, ".//div[text()='Вопросы о важном']"]
    menu = [By.XPATH, ".//*[@class='accordion']"]
    questions_menu = [By.XPATH, ".//*[contains(@id, 'accordion__heading-')]"]
    answers_menu = [By.XPATH, ".//*[contains(@id, 'accordion__panel-')]/p"]
    accept_cookies = [By.XPATH, ".//button[@class='App_CookieButton__3cvqF' and text()='да все привыкли']"]
    button_order_up = [By.XPATH, ".//*[@class='Button_Button__ra12g']"]
    button_order_down = [By.XPATH, ".//*[contains(@class, 'Button_Middle__1CSJM')]"]
    button_scooter = [By.XPATH, ".//*[@alt='Scooter']"]
    button_yandex = [By.XPATH, ".//*[@alt='Yandex']"]


class OrderPageLocators:
    field_name = [By.XPATH, ".//*[@placeholder='* Имя']"]
    field_last_name = [By.XPATH, ".//*[@placeholder='* Фамилия']"]
    field_address = [By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']"]
    field_phone_number = [By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']"]
    field_subway_station = [By.XPATH, ".//*[@placeholder='* Станция метро']"]
    button_next = [By.XPATH, ".//*[text()='Далее']"]  # Кнопка Далее
    field_when_to_bring = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]
    field_rental_period = [By.XPATH, ".//*[@class='Dropdown-arrow']"]
    rental_period_menu = [By.XPATH, ".//*[@class='Dropdown-menu']/div"]
    field_scooter_color = [By.XPATH, ".//*[@class='Checkbox_Label__3wxSf']"]
    field_comment = [By.XPATH, ".//*[@placeholder='Комментарий для курьера']"]
    button_to_order = [By.XPATH, ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') "
                                 "and text()='Заказать']"]
    yes_or_no_buttons = [By.XPATH, ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM')""and text()='Нет'or text()='Да']"]

    info_about_order = [By.XPATH, ".//*[@class='Order_ModalHeader__3FDaJ']"]