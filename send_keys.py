
ניסיתי לפתור את זה בשני דרכים.

1.
self.click_element(By.XPATH, '//form/div[2]/div[5]/div[2]/div[1]/label') # press button photo/video
self.send_keys("C:/Users/shayo/passover.png") # NOT WORKING

2.
self.upload_File(By.XPATH, '//form/div[2]/div[5]/div[2]/div[1]/label', "C:/Users/shayo/passover.png") # NOT WORKING.


base_page.py:

  def upload_File(self, locator_type, locator_value, path):
      self.driver.find_element(locator_type, locator_value).click()
      self.driver.send_keys(path)
      
      
Console error:

>       self.driver.send_keys(path)
E       AttributeError: 'WebDriver' object has no attribute 'send_keys'
