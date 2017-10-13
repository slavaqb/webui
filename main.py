import os, time, threading, datetime
from selenium import webdriver

class Speaker():
    def __init__(self, interval):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while (True):
            print('{dt}'.format(dt=datetime.datetime.now()))
            sleep(self.interval)

def main():
    print('def main()')
    driver = webdriver.Firefox()
    driver.get("http://rolling-horse.000webhostapp.com/")
    html_source = driver.page_source
    print(html_source)
    Speaker(30)
    time.sleep(60*30)
    driver.close()
    print('Ok')
if __name__ == '__main__':
    main()
