import requests
from bs4 import BeautifulSoup
from products.models import Product

giga_all_plans = []

telco = "giga!"

URL = 'https://www.giga.com.sg/SignUp.aspx'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='p35 display-flex PlanSelectionWrapper WithBestPlan web')
narrow = results.find_all('div', class_='position-relative OSInline')

def add_giga_products():
    for plan in narrow:  
        # plan_name = plan.find('div', class_='data-plan-name')
        plan_data = plan.find('span', class_='fw700')

        plan_cost = plan.find('div', class_='fw700')

        talktime_sms = plan.find('div', class_='fw600')

        plan_calltime = talktime_sms.find('div', text=lambda t: t and "mins" in t)
        plan_sms = talktime_sms.find('div', text=lambda t: t and "sms" in t)

        narrower = plan.find(class_='position-absolute')
        plan_desc = narrower.find('div', class_="display-flex").find(class_='fs-two-wbp')
        if plan_desc is not None:
            details = plan_desc.text
        else:
            details = ''
        # print("name: " + plan_name.text, end='\n')
        # print("data: " + plan_data.text, end='\n')
        # print("sms: " + plan_sms.text, end="\n")
        # print("calltime: " +
        #         plan_calltime.text, end="\n")
        # print(
        #     "cost: " + plan_cost.text, end='\n')
        
        # print(details)
        plan_item = {
                'telco': telco,
                'data': plan_data.text.replace('GB', ''),
                'contract_length': "No Contract",
                'title': telco + " " + plan_data.text + " " + "No Contract Plan",
                'category': "Postpaid",
                'price': plan_cost.text.replace('$', ''),
                'call_time': plan_calltime.text.replace('mins', ''),
                'sms': plan_sms.text.replace('sms', ''),
                'description': details,         
            }

        giga_all_plans.append(plan_item)

