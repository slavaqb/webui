import os
from selenium import webdriver

def main():
    print('def main()')
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    html_source = driver.page_source
    print(html_source)
    driver.close()
if __name__ == '__main__':
    main()
