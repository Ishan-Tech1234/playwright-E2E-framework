from playwright_logger_module import logging

from playwright.sync_api import expect

class BasePage:
    def __init__(self,page):
        self.page=page
        self.page.on("console",
                     lambda msg:logging.error(f"Error text:{msg.text} Error type : {msg.type}") if msg.type=="error" else None)

    

    def navigate(self,url):
        self.page.goto(url)
        logging.info("After navigating to webpage undertest which is %s",self.page.url)
        
        
    
       
           
           
    
    def fill(self,locator,input,description=None):
        target=self.page.locator(locator)
        expect(target).to_be_editable()
        target.fill(input)
        if description!=None:
         logging.info("entering %s",description)
        else:
         logging.info("entering details in fields")
        
        
    
    def click(self, locator,description=None):
      if isinstance(locator, str):
        locator = self.page.locator(locator)
      expect(locator).to_be_enabled()
      expect(locator).to_be_visible()
      locator.click()
      if description !=None:
         logging.info("%s",description)
      else:
         logging.info("performing click action")
      
  