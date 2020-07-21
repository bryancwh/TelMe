import requests
from bs4 import BeautifulSoup
from products.models import Product

myrepublic_all_plans = []

telco = "My Republic"

URL = 'https://mobile.myrepublic.com.sg/plans'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='col-md-10 col-centered')
narrow = results.find_all('div', class_='item')

def add_myrepublic_products():
    for plan in narrow:  
        plan_name = plan.find('div', class_='promo-plan-title')

        plan_cost = plan.find('div', class_="purple_text")

        plan_rows = plan.find_all('div', class_='row')

        plan_data = ''

        plan_calltime = ''

        plan_sms = ''
        
        details = ""

        for row in plan_rows:
            element = row.find(class_='col-md-12 plan-title')
            if element is None:
                break
                
            words = element.text.replace('\n', '')

            if words and "Data" in words:
                data = words.split(' Data')[0]
                details = words.split(' Data')[1].replace('*', '')
                if data and "+" in data:
                    plan_data = data.split(' +')[0].replace(' GB', '')
                elif data and "GB" in data:
                    plan_data = data.replace(' GB', '')
                else:
                    plan_data = data
            elif words and "Talktime" in words:
                plan_calltime = words.split(' Talktime')[0].replace(' Minutes', '')
            elif words and "SMS" in words:
                plan_sms = words.split(' SMS')[0]


        # print("name: " + plan_name.text, end='\n')
        # print("data: " + plan_data, end='\n')
        # print("sms: " + plan_sms, end="\n")
        # print("calltime: " +
        #         plan_calltime, end="\n")
        # print(
        #     "cost: " + plan_cost.text, end='\n')
        # print(details)
        plan_item = {
                'telco': telco,
                'data': plan_data,
                'contract_length': "No Contract",
                'title': telco + " " + plan_name.text,
                'category': "Postpaid",
                'price': plan_cost.text.replace('$', '').replace('/MTH', ''),
                'call_time': plan_calltime,
                'sms': plan_sms,
                'description': details,         
            }

        myrepublic_all_plans.append(plan_item)
