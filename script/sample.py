#!/usr/local/bin/python3
import random
from time import sleep
import datetime

from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def execSearch(browser: webdriver, url, container_num, sleep_time):
    """
    :param browser: webdriver
    """
    # スクリーンショットのファイル名用に日付を取得
    dt = datetime.datetime.today()
    datetime_str = dt.strftime('%Y-%m-%d %H:%M:%S')

    browser.get(url)
    print(datetime_str + ' container_num ' + str(container_num) + ' : ' + str(sleep_time), flush=True)
    sleep(sleep_time)

    # スクリーンショット
    dt_fiilname = dt.strftime('%Y%m%d_%H%M%S')
    browser.save_screenshot('images/' + dt_fiilname + '.png')

def exec(container_num):
    USER_AGENT_STRING = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 12_1_2 like Mac OS X; ja-jp) AppleWebKit/605.1.15 (KHTML,like Gecko) Version/12.0 Mobile/15E148Safari/604.1')
    ua_select = container_num % len(USER_AGENT_STRING)

    try:
        #browser = webdriver.Firefox()  # 普通のFilefoxを制御する場合
        #browser = webdriver.Chrome()   # 普通のChromeを制御する場合
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-agent={USER_AGENT_STRING[ua_select]}')

        # HEADLESSブラウザに接続
        browser = webdriver.Remote(
            command_executor='http://selenium-hub' + str(container_num) + ':4444/wd/hub',
            options=options,
            desired_capabilities=DesiredCapabilities.CHROME)

        execSearch(browser, 'https://google.com/', container_num, random.randint(8, 10))
        execSearch(browser, 'https://www.google.com/search?q=au%E3%81%AE%E6%97%A5%E8%A8%98', container_num, random.randint(8, 10))
        execSearch(browser, 'https://program-shoshinsya.hatenablog.com/', container_num, random.randint(8, 10))

    finally:
        # 閉じて終了
        browser.close()
        browser.quit()


if __name__ == '__main__':
    while(True):
        for container_num in range(3):
            exec(container_num)
