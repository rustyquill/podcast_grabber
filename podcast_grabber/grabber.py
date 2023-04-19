import subprocess
from pprint import pprint
from time import sleep
from csv_maker import dict_2D
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class podcast_grabber(object):
    def __init__(self, podcast_name=None, podcast_object={}):
       #self.options.add_argument("--headless")
       #self.options.add_argument("browser.link.open_newwindow", 0)
       self.podcast_name = podcast_name
       self.podcast_object = podcast_object
       self.create_driver()
       
    def create_driver(self):
       self.options = Options()
       self.driver = webdriver.Chrome(options=self.options)
       self.googled_once = False
       self.driver.set_page_load_timeout(40)
       self.driver.implicitly_wait(5)
       
    def update_podcast_object(self, update):
       
       if self.podcast_object.get(self.podcast_name):
          self.podcast_object[self.podcast_name].update(update)
       else:
          self.podcast_object[self.podcast_name] = update


    def try_google(self, service):
       google_str = self.podcast_name + " " + service
       self.driver.get('https://www.google.com/search?q={}'.format(google_str.replace(' ', '+')))
       #sleep(5)
       if self.googled_once is not True:
          buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
          buttons[3].click()
          self.googled_once = True
       search_div = self.driver.find_element(By.ID, "search")
       first_link = search_div.find_element(By.CSS_SELECTOR, "a")
       first_link.click()
       #sleep(5)
       self.update_podcast_object({ service : self.driver.current_url})
       return self.podcast_object
       
    def get_stitcher(self):
       try: 
          return self.try_google("stitcher")
       except Exception as e:
          print(e)
          self.create_driver()
       self.driver.get('https://www.stitcher.com/search/{}'.format(self.podcast_name))
       try:
          button = clickable = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
          button.click()
       except Exception as e:
          print(e)
       clickables = self.driver.find_elements(By.CLASS_NAME, "show-container")
       for i in clickables:
          try:
             i.click()
             break
          except Exception as e:
             print(e)
       sleep(5)
       self.update_podcast_object({'stitcher' : self.driver.current_url})
       return self.podcast_object
   
    def get_google(self):
       try:
          button = clickable = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
          button.click()
       except Exception as e:
          print(e)
          self.create_driver()
       self.driver.get('https://podcasts.google.com/search/{}'.format(self.podcast_name))
       clickables = self.driver.find_elements(By.CSS_SELECTOR, "img")
       for i in clickables:
          #try:
          i.click()
          break
          #except Exception as e:
          #   print(e)
       #sleep(5)
       self.update_podcast_object({'google' : self.driver.current_url})
       return self.podcast_object
    

    def get_playerfm(self):
       try: 
          return self.try_google("playerfm")
       except Exception as e:
          print(e)
          self.create_driver()
       self.driver.get('https://player.fm/search/{}'.format(self.podcast_name))
       articles = self.driver.find_elements(By.CLASS_NAME, "record")
       for i in articles:
          try:
             i.find_element(By.CLASS_NAME, 'sponsored-label')
             continue
          except Exception as e:
             print(e)
          try:
             clickable = i.find_element(By.CSS_SELECTOR, 'a')
             clickable.click()
             break
          except Exception as e:
             print(e)
             self.create_driver()
          try:
             clickable = i.find_element(By.CSS_SELECTOR, 'img')
             clickable.click()
             break
          except Exception as e:
             print(e)
             self.create_driver()
       #sleep(5)
       self.update_podcast_object({'playerfm' : self.driver.current_url})
       return self.podcast_object

    def get_podchaser(self):
       try: 
          return self.try_google("podchaser")
       except Exception as e:
          print(e)
          self.create_driver()
       self.driver.get('https://www.podchaser.com/search/podcasts/q/{}'.format(self.podcast_name))
       clickables = self.driver.find_elements(By.CSS_SELECTOR, "[data-id='entity-card-title']")
       for i in clickables:
          try:
             i.click()
             break
          except Exception as e:
             print(e)
       #sleep(5)
       self.update_podcast_object({'podchaser' : self.driver.current_url})
       return self.podcast_object

    def get_podbean(self):
       try: 
          return self.try_google("podbean")
       except Exception as e:
          print(e)
          self.create_driver()
       self.driver.get('https://podbean.com/site/search/index?v={}'.format(self.podcast_name.replace(" ", "+")))
       clickables = self.driver.find_elements(By.CLASS_NAME, "pic")
       for i in clickables:
          try:
             i.click()
             break
          except Exception as e:
             print(e)
       #sleep(5)
       self.driver.switch_to.window(self.driver.window_handles[1])
       self.update_podcast_object({'podbean' : self.driver.current_url})
       return self.podcast_object

    def get_apple(self):
       try: 
          return self.try_google("apple")
       except Exception as e:
          print(e)
          self.create_driver()
       self.driver.get('https://www.apple.com/uk/search/{}?src=globalnav'.format(self.podcast_name.replace(" ", "-")))
       elements = self.driver.find_elements(By.CLASS_NAME, "rf-serp-explore-curated")
       for i in elements:
          try:
             pic = i.find_element(By.CSS_SELECTOR, 'img')
             pic.click()
             break
          except Exception as e:
             print(e)
             self.create_driver()
       sleep(5)
       self.update_podcast_object({'apple' : self.driver.current_url})
       return self.podcast_object

    def get_castbox(self):
       try: 
          return self.try_google("castbox")
       except Exception as e:
          print(e)
       return self.podcast_object

    def get_pocket_casts(self):
       try: 
          return self.try_google("pocket casts")
       except Exception as e:
          print(e)
       return self.podcast_object
    
    def get_podcast_republic(self):
       try: 
          return self.try_google("podcast republic")
       except Exception as e:
          print(e)
       return self.podcast_object
    
    def get_all_platforms(self):
       for func in [ 
          self.get_apple,
          self.get_podbean,
          self.get_playerfm,
          self.get_podchaser,
          self.get_stitcher,
          self.get_google,
          self.get_castbox,
	  self.get_pocket_casts,	
          self.get_podcast_republic
          ]:
          func()
          self.create_driver()
       return self.podcast_object
      
    def write_csv(self, filename=None):
       if filename is None:
          dict_2D(self.podcast_object,self.podcast_name)
       else:
          dict_2D(self.podcast_object, self.podcast_name, filename=filename)
        
    def close_browser(self):
       self.driver.close()
       subprocess.run("ps aux | awk /firefox/'{print $2}' | xargs kill", shell=True)
       return False
 
if __name__ == '__main__':
   p_object = {}
   podcasts = ['the magnus archives', 'rusty quill gaming podcast', 'stellar firma', '"outliers - stories from the edge of history"', '"enthusigasm"']
   for p in ["trice forgotten", "chapter and multiverse"]:
      print('starting ' + p) 
      pg = podcast_grabber(p, p_object)
      pg.get_all_platforms() 
      pg.write_csv(filename = p + '.csv')
      print(p)
   pg.write_csv()
