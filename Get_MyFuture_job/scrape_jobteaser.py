from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Firefox()
import pandas as pd

browser.implicitly_wait(5) 
browser.get('https://groupeinsa.jobteaser.com/fr/job-offers?q=Data&contract=stage,internship&location=France..France,Morocco..Morocco&start_date=2022_02&locale=en,fr')

browser.implicitly_wait(5) 
username = browser.find_element_by_xpath('//*[@id="user_email"]')
username.send_keys(['your_email'])

browser.implicitly_wait(5) 
password = browser.find_element_by_xpath('//*[@id="user_password"]')
password.send_keys(['your_password'])

browser.implicitly_wait(3)
signInButton = browser.find_element_by_xpath('//*[@id="user_submit"]')
signInButton.click()

browser.implicitly_wait(3) 

titles=[]
companies=[]
locations=[]
links =[]
descriptions=[]
jobType = []
job_published_since = []

browser.implicitly_wait(6)

for i in range(0,1) :
    jobCard = browser.find_elements_by_xpath('.//section/div/a')
    for job in jobCard:
        browser.implicitly_wait(3)
        #get job title
        title = job.find_element_by_xpath('.//h1[@class="jt-JobOffer-title__3C0yg"]').text
        titles.append(title)
        #get company name
        company = job.find_element_by_xpath('.//div[@class="jt-Wrap__1W_ho jt-Wrap--inline__32UZ4"]').text
        companies.append(company)
        #get the location
        location = job.find_element_by_xpath('.//li[2][@class="jt-JobOffer-descriptionListItem__1p2rE"]').text
        locations.append(location)
        #get the date the job has been published
        published = job.find_element_by_xpath('.//li[3][@class="jt-JobOffer-descriptionListItem__1p2rE"]').text
        job_published_since.append(published)
        #the link description for each job
        link= job.get_attribute(name='href')
        print(link)
        links.append(link)
    try: 
        next_page= browser.find_element('<a href="#" class="jt-Paginator-link__hHHN4 cc-theme-color--text_hover">{}</a>'.format(i+2))
        next_page.click()
    except:
        next_page= browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[5]/ul/li[6]/a')
        next_page.click()
    print("Page: {}".format(str(i+2)))


print('the data we get locations {}, company {}, job title {}, job link description'.format(locations,companies,titles,links))

#Récupération des job description pour chaque jobCards  

for link in links:
    browser.implicitly_wait(10)
    browser.get(link)
    job_description = browser.find_element_by_xpath('//div[@class="jds-Text jds-Text--normal jod-WysiwygText"]').text
    descriptions.append(job_description)
    

data = pd.DataFrame()
data["companies"]=companies
data["job title"]=titles
data["job Description"]=descriptions
data["job link"] = links



