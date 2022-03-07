from selenium.webdriver.chrome.options import Options

"""PATHS"""
DEFAULT_PATHS = {
    "DEFAULT_WEBDRIVER": "C:\Program Files (x86)\chromedriver.exe",
    "DEFAULT_CINEPLEX_WEBPAGE": "https://www.cineplex.com/Theatre/cineplex-cinemas-marine-gateway-and-vip"
}

"""Web Driver Options"""
DEFAULT_WEBDRIVER_OPTION = Options()
# DEFAULT_WEBDRIVER_OPTION.add_argument('--no-sandbox')
# DEFAULT_WEBDRIVER_OPTION.add_argument("--start-maximized")
# DEFAULT_WEBDRIVER_OPTION.add_argument("--window-size=1920x1080")
DEFAULT_WEBDRIVER_OPTION.add_argument('--disable-extensions')
DEFAULT_WEBDRIVER_OPTION.add_argument("--disable-gpu")
DEFAULT_WEBDRIVER_OPTION.add_argument("--disable-dev-shm-usage")
DEFAULT_WEBDRIVER_OPTION.add_argument("--proxy-bypass-list=*")
DEFAULT_WEBDRIVER_OPTION.add_argument('--ignore-certificate-errors')
DEFAULT_WEBDRIVER_OPTION.add_argument("--headless")
