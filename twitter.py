from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TwitterBot:
    
    # initializing our bot 
    def __init__(self, username, password):
        # username and pass so we can log in
        self.username = username
        self.password = password
        # our bot which is connected to the webdriver
        self.bot = webdriver.Firefox()
        
    # login function, takes care of opening, entering username and pass and logs in
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        # in case it needs time to load
        time.sleep(5)
        
        # access email and pass using element name 
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        
        # clear the inputs before sending any
        email.clear()
        password.clear()

        # enter (send) email and pass to the broswer
        email.send_keys(self.username)
        password.send_keys(self.password)
        
        # return the keys (login)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        
    def like_tweet(self):
        bot = self.bot
        bot.get('https://twitter.com/RealGrumpyCat')
        #bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
        time.sleep(5)
        #for i in range(1,3):
        #bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        '''
        first way below needs a bit of tweeking, it scraps more info that needed
        the 2nd way works as intended
        '''
        #tweets = bot.find_elements_by_class_name('css-1dbjc4n')
        #links = [elem.get_attribute('href') for elem in bot.find_elements_by_xpath("//a[@dir='auto']")]
        #filteredLinks = list(filter(lambda x: 'status' in x, links))
        tweets = bot.find_elements(By.XPATH, '//*[@data-testid="tweet"]//a[@dir="auto"]')  
        links = [elem.get_attribute('href') for elem in tweets]    
        for link in links:
            bot.get(link)
            time.sleep(5)
            try:
                bot.find_element_by_xpath("//div[@data-testid='like']").click()
                time.sleep(5)
            except Exception as ex:
                time.sleep(10)
def Read_Email_Pass_File(destination):
    infile = open(destination,'r')
    filecontent = infile.readlines()
    infile.close()
    Email_and_Pass = []
    for line in filecontent:
        tmp = line.strip().split(':')
        Email_and_Pass.append(tmp[1])
    return Email_and_Pass     
def main():
    Email_and_Pass = Read_Email_Pass_File('../Email&Pass.txt')     
    App = TwitterBot(Email_and_Pass[0], Email_and_Pass[1])
    App.login()
    App.like_tweet()
    
if __name__ == '__main__':
    main()