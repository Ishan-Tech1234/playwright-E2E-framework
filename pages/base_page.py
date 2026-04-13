from playwright_logger_module import logging


class BasePage:
    def __init__(self,page):
        self.page=page
        self.page.on("console",
                     lambda msg:logging.error(f"Error text:{msg.text} Error type : {msg.type}") if msg.type=="error" else None)

    

    def navigate(self,url):
        self.page.goto(url)
        logging.info("Navigating to %s",self.page.url)
        
    
       
           
           
    
    def fill(self,locator,input,description=None):
        self.page.fill(locator,input)
        logging.info("entering %s",description)
        
        
    
    def click(self, locator,description=None):
      if isinstance(locator, str):
        locator = self.page.locator(locator)
      locator.click()
      if description !=None:
         logging.info("%s",description)
      else:
         logging.info("performing click action")
      
  