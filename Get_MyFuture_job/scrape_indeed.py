from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')


browser.implicitly_wait(5) 
browser.get('https://fr.indeed.com/jobs?q=Data+Manager&l=Paris+%2875%29&radius=50&from=sug&vjk=4dc33b41cd78b45a')
import pandas as pd


#search data science 
search_job = browser.find_element_by_xpath('//*[@id="text-input-what"]')
search_job.send_keys(['Data Engineer junior'])

search_button = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div[1]/form/button')
search_button.click()

close_popup =  WebDriverWait(browser, 1000000).until(EC.element_to_be_clickable(browser.find_element_by_xpath('/html/body/div[5]/div[1]/button'))).click()

browser.implicitly_wait(3) 

titles=[]
companies=[]
locations=[]
links =[]
reviews=[]
salaries = []
descriptions=[]
jobType = []


for i in range(0,1):
    job_card = browser.find_elements_by_class_name('tapItem')
    for job in job_card:
        try:
            review = job.find_element_by_xpath('.//span[@class="ratingsDisplay withRatingLink"]').text
        except:
            review = "None"
        reviews.append(review)
        title = job.find_element_by_xpath('.//span[@title]').text
        titles.append(title)
        link = job.get_attribute(name="href")
        links.append(link)
        companies.append(job.find_element_by_xpath('.//span[contains(@class,"companyName")]').text)
    try: 
        next_page= browser.find_element_by_xpath('//a[@aria-label={}]//span[@class="pn"]'.format(i+2))
        next_page.click()
    except:
        next_page= browser.find_element_by_xpath('//a[@aria-label="Next"]//span[@class="pn"]//span[@class="np"]')
        next_page.click()
    print("Page: {}".format(str(i+2)))

print("la partie 1 du scrapping est terminé...")

print("Récupération des job Descriptions en cours....")

#Récupération des job description pour chaque jobCards  

for link in links:
    browser.implicitly_wait(10)
    browser.get(link)
    job_description = browser.find_element_by_xpath('//div[@id="jobDescriptionText"]').text
    descriptions.append(job_description)
    try:
        job_type = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/span').text
    except:
        job_type="None"
    jobType.append(job_type)

print("la partie scrapping est terminé")

dataPost = pd.DataFrame()
dataPost["companies"]=companies
dataPost["job title"]=titles
dataPost["job Type"]=jobType
dataPost["job Description"]=descriptions
dataPost["job link"] = links

print(dataPost)



