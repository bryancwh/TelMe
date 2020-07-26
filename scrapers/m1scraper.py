import requests
from bs4 import BeautifulSoup
from products.models import Product

m1_all_plans = []

telco = "M1"

URL_Sim= 'https://www.m1.com.sg/Mobile/sim-only-plan'
URL_Plan = 'https://www.m1.com.sg/Mobile/plan-with-device'

def add_m1_products():
    page = requests.get(URL_Sim)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='text-gradient-component align-grid-height-equal')
    narrow = results.find_all('div', class_='col-xs-12 col-sm-12 col-lg-6 col-md-6 padding-false text-gradient-item theme-purple')
    for plan in narrow:
        # plan_name = plan.find('div', class_='data-plan-name')

        plan_data = plan.find('p', text=lambda t: t and "GB" in t)

        plan_cost = plan.find('p', text=lambda t: t and "$" in t)

        talktime_sms = plan.find('li', text=lambda t: t and "SMS" in t).text.split('+ ')
        plan_calltime = talktime_sms[0].replace(',', '')
        plan_sms = talktime_sms[1].replace(',', '')

        plan_desc = plan.find('div', class_="ticked-list")

        plan_desc_points = plan_desc.find_all('li')

        details = ""

        # print("name: " + plan_name.text, end='\n')
        # print("data: " + plan_data.text.replace('GB', ''), end='\n')
        # print("sms: " + plan_sms, end="\n")
        # print("calltime: " +
        #         plan_calltime, end="\n")
        # print(
        #     "cost: " + plan_cost.text, end='\n')
        for points in plan_desc_points:
            if details == "":
                details = points.text
            else:
                details = details + " " + points.text
        #     print(points.text, end='\n')
        # print('\n')

        plan_item = {
                'telco': telco,
                'data': plan_data.text.replace('GB', ''),
                'contract_length': "0",
                'title': telco + " " + plan_data.text + " " + "No Contract Plan",
                'category': "Postpaid",
                'price': plan_cost.text.replace('$', '').replace('/MTH', '').replace('/mth',''),
                'call_time': plan_calltime.replace(' Mins', ''),
                'sms': plan_sms.replace(' SMS', ''),
                'description': details,         
            }

        m1_all_plans.append(plan_item)

    page = requests.get(URL_Plan)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(class_='text-gradient-component align-grid-height-equal')
    narrow = results.find_all('div', class_='col-xs-12 col-sm-12 col-lg-12 col-md-12 padding-false text-gradient-item theme-purple')

    for plan in narrow:  
        # plan_name = plan.find('div', class_='data-plan-name')

        plan_data = plan.find('p', text=lambda t: t and "GB" in t)

        plan_cost = plan.find('p', text=lambda t: t and "$" in t)

        talktime_sms = plan.find('li', text=lambda t: t and "SMS" in t).text.split('+ ')
        plan_calltime = talktime_sms[0].replace(',', '')
        plan_sms = talktime_sms[1].replace(',', '')

        plan_desc = plan.find('div', class_="ticked-list")

        plan_desc_points = plan_desc.find_all('li')

        details = ""

        # print("name: " + plan_name.text, end='\n')
        # print("data: " + plan_data.text.replace('GB', ''), end='\n')
        # print("sms: " + plan_sms, end="\n")
        # print("calltime: " +
        #         plan_calltime, end="\n")
        # print(
        #     "cost: " + plan_cost.text, end='\n')
        for points in plan_desc_points:
            if details == "":
                details = points.text
            else:
                details = details + ", " + points.text
        #     print(points.text, end='\n')
        # print('\n')

        plan_item = {
                'telco': telco,
                'data': plan_data.text.replace('GB', ''),
                'contract_length': "24",
                'title': telco + " " + plan_data.text + " " + "24 Month Plan",
                'category': "Postpaid",
                'price': plan_cost.text.replace('$', '').replace('/MTH', '').replace('/mth',''),
                'call_time': plan_calltime.replace(' Mins', ''),
                'sms': plan_sms.replace(' SMS', ''),
                'description': details
                
            }

        m1_all_plans.append(plan_item)


