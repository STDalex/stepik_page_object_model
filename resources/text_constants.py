class TextConstants:
    class English:
        LOGIN_LINK = "Login or register"
        SUCCESS_MESSAGE = "Product successfully added to the basket"
        EMPTY_BASKET_MESSAGE = "Your basket is empty. Continue shopping"
        REGISTRATION_EMAIL_LABEL = "Email address"
        REGISTRATION_PASSWORD_LABEL = "Password"
        REGISTRATION_CONFIRM_PASSWORD_LABEL = "Confirm password"
        REGISTRATION_BUTTON = "Register"
        
    class Russian:
        LOGIN_LINK = "Войти или зарегистрироваться"
        SUCCESS_MESSAGE = "Товар добавлен в корзину"
        EMPTY_BASKET_MESSAGE = "Ваша корзина пуста Продолжить покупки"
        REGISTRATION_EMAIL_LABEL = "Адрес электронной почты"
        REGISTRATION_PASSWORD_LABEL = "Пароль"
        REGISTRATION_CONFIRM_PASSWORD_LABEL = "Подтвердите пароль"
        REGISTRATION_BUTTON = "Зарегистрироваться"

    @staticmethod
    def get_text(language: str = "en") -> object:
        """
        Возвращает класс с текстовыми константами для выбранного языка
        :param language: код языка ('en' или 'ru')
        :return: класс с текстовыми константами
        """
        if language.lower() == "ru":
            return TextConstants.Russian
        return TextConstants.English 