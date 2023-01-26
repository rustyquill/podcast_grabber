from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class emote_grabber(object):
    def __init__(self, channel_name=None):
       self.driver = webdriver.Chrome()
       self.channel_name = channel_name
       self.channel_url = None
       self.emotes      = None 
       if self.channel_name is not None:
           self.channel_url = self.get_channel_url()
       
    def get_channel_url(self, channel_name=None):
       if channel_name is None and self.channel_name is None:
           return 'please provide channel_name'
       elif channel_name is None:
          pass
       elif channel_name != self.channel_name:
          self.emotes = None
          self.channel_url = None
          self.channel_name = channel_name
       self.driver.get('https://twitchemotes.com/')
       search_bar = self.driver.find_element(By.NAME, 'query')
       search_bar.send_keys(self.channel_name)
       search_bar.send_keys(Keys.RETURN)
       self.channel_url = self.driver.current_url
       return self.driver.current_url
    
    def get_emotes(self):
       if self.channel_url is None:
          self.get_channel_url
       self.driver.get(self.channel_url)
       images = self.driver.find_elements(By.CLASS_NAME, 'emote')
       self.emotes = {i.get_attribute('data-regex') : i.get_attribute('src') for i in images}
       return self.emotes
       
    
if __name__ == '__main__':
   eg = emote_grabber()
   eg.get_channel_url('askmartyn')
   print(eg.get_emotes())

