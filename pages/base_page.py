class BasePage:
    def __init__(self,page):
        self.page=page
        
    
    def navigate(self,url):
        self.page.goto(url)
    
    def fill(self,locator,input):
        self.page.fill(locator,input)
        
    
    def click(self,button):
        self.page.click(button)
    

  