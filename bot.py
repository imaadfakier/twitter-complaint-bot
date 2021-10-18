from selenium import webdriver
import time
import os


def wait(secs):
    time.sleep(secs)


class InternetSpeedTwitterBot:
    """
    ...
    """

    # class attributes
    # ...

    def __init__(self, chrome_driver_path, internet_down_speed, internet_up_speed):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.down_speed_promised = internet_down_speed
        self.up_speed_promised = internet_up_speed

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.maximize_window()
        test_internet_speed = self.driver.find_element_by_class_name('start-text')
        test_internet_speed.click()
        wait(50)
        current_down_speed = float(self.driver.find_element_by_class_name('download-speed').text)
        current_up_speed = float(self.driver.find_element_by_class_name('upload-speed').text)
        print('down: {down}\n'.format(down=current_down_speed), f'up: {current_up_speed}', sep='')
        return current_down_speed, current_up_speed

    def log_into_twitter(self):
        self.driver.get('https://twitter.com/')
        wait(1)
        log_in_link = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span'
        )
        log_in_link.click()
        wait(1)
        peu_login_option = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a'
        )
        peu_login_option.click()
        wait(1)
        username_input_field = self.driver.find_element_by_name(name='session[username_or_email]')
        username_input_field.send_keys(os.environ.get('TWITTER_USERNAME'))
        password_input_field = self.driver.find_element_by_name(name='session[password]')
        password_input_field.send_keys(os.environ.get('TWITTER_PASSWORD'))
        log_in_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'
        )
        log_in_button.click()
        wait(2)

    def tweet_at_provider(self, down_speed, up_speed):
        whats_happening_input_actually_span = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]'
            '/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]'
            '/div/div/div/div/div[2]/div/div/div/div/span'
        )
        whats_happening_input_actually_span.send_keys(
            'Hey Internet Provider, why is my internet speed {down_speed}down/{up_speed}up when I '
            'pay for {contract_down_speed}down/{contract_up_speed}up?'.format(
                down_speed=down_speed,
                up_speed=up_speed,
                contract_down_speed=self.down_speed_promised,
                contract_up_speed=self.up_speed_promised
            )
        )
        compose_tweet_button_actually_div = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div'
            '/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div'
            '/div[2]/div[3]/div/span/span'
        )
        compose_tweet_button_actually_div.click()
