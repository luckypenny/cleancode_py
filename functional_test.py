from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
print("binary : %s", binary)
browser = webdriver.Firefox(firefox_binary=binary)
browser.get('http://localhost:8000')

assert 'Django' in browser.title