# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import re
# import time
import tozdautils as utilz
import time


# url_no_fluff_job = 'https://nofluffjobs.com/pl/warszawa/testing?criteria=employment%3Dpermanent,b2b&page=1'
# url_just_join_it = 'https://justjoin.it/?tab=with-salary'
# url_bulldog_job = 'https://bulldogjob.pl/companies/jobs'
# driver.get(url_no_fluff_job)

logger = utilz.get_logger('tozda')
logger.info("TEST")
# NO FLUFF JOB
driver = utilz.get_browser('incognito')
driver.get('https://nofluffjobs.com/pl/warszawa/testing?criteria=employment%3Dpermanent,b2b&page=1')
assert "Praca Testing" in driver.title
assert "Warszawa" in driver.title
assert "No Fluff Jobs" in driver.title


# click "Akceptuj wszystkie pliki cookies" button
driver.find_element(By.ID, value="onetrust-accept-btn-handler").click()
elements = driver.find_elements(By.CLASS_NAME, value='page-item active ng-star-inserted')

driver.close()

print("EOF")