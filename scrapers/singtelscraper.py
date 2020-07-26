from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests
from bs4 import BeautifulSoup
import re
from products.models import Product

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome("")

url = 'https://shop.singtel.com/plans'

telco = "Singtel"

singtel_all_plans = []

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)

links = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div')

num_links = len(links.find_elements_by_class_name('Tabs__TabItem-lrvfil-2'))

def add_singtel_products():
    for i in range(num_links):
        button = links.find_elements_by_class_name('Tabs__TabItem-lrvfil-2')[i]
        button.click()
        driver.implicitly_wait(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find(class_='Row-v1llhy-0 jaHyfS PlanCatalog__StyledRow-pdkswt-0 eMUUbI')
        plans = results.find_all(class_='PlanCatalogCard__StyledCard-sc-1one2th-0 hedRUD')
        for plan in plans:
            title = plan.find(class_='Base__Body-sc-1tk6mnl-9 Base__BodySecondary-sc-1tk6mnl-11 PlanCatalogCard__StyledName-sc-1one2th-3 fWRava')
            
            contract_length = re.search(r'\(([^)]+)', title.text)
            if contract_length is not None:
                contract_length = contract_length.group(1)
                if contract_length != "No Contract":
                    contract_length = contract_length[:2]
                else:
                    contract_length = "0"                
            else:
                contract_length = "24"
            
            data = plan.find(class_='Base__H3-sc-1tk6mnl-2 ioiCgH')
            
            price = plan.find(class_='Base__Subtitle-sc-1tk6mnl-6 Base__SubtitlePrimary-sc-1tk6mnl-7 hpCTsy')
            
            details = plan.find(class_='Base__Caption-sc-1tk6mnl-15 Ribbon-sc-1flxzf-0 kyrcYu').text
            
            more_details = plan.find(class_='Base__Body-sc-1tk6mnl-9 Base__BodySecondary-sc-1tk6mnl-11 eYNSTK')
            talktime_sms = more_details.find('li', text=lambda t: t and "SMS" in t).text.split('& ')
            talktime = talktime_sms[0].replace(' Talktime ', '')
            sms = talktime_sms[1]
            if sms == "SMS":
                sms = "Unlimited"
            dets = more_details.find_all('li')
            for points in dets:
                if details != "":
                    details = details + ", " + points.text
                else:
                    details = points.text
            
            plan_item = {
                'telco': telco,
                'title': telco + " " + title.text + " Plan",
                'category': "Postpaid",
                'price': price.text.replace('/mth','').replace('$',''),
                'data': data.text.replace('GB', ''),
                'call_time': talktime.replace(' mins', ''),
                'sms': sms.replace(' SMS', ''),
                'contract_length': contract_length,
                'description': details           
            }

            singtel_all_plans.append(plan_item)

            # print("name: Singtel " + title.text)
            # print("data: " + data.text)
            # print("price: " + price.text)
            # print("talktime: " + talktime)
            # print("sms: " + sms)
            # print(details)

    driver.quit()

