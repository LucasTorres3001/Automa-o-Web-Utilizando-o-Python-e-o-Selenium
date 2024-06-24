from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)
service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(options=options, service=service)
browser.get(url='https://en.wikipedia.org/wiki/Main_Page')
browser.find_element('xpath', '//*[@id="searchInput"]').send_keys('Python (programming language)')
browser.find_element('xpath', '//*[@id="searchform"]/button').click()