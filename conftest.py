import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.page_load_strategy = "eager"
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=firefox_options)
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    print(f"\nstart {browser_name} browser for test with {user_language} language..")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def language(request) -> str:
    """
    Фикстура для получения языка из параметров командной строки
    """
    return request.config.getoption("language")