import requests
from bs4 import BeautifulSoup

starhub_all_plans = []

from products.models import Product

URL = 'https://www.starhub.com/personal/mobile.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='tab-content')
narrow = results.find_all('div', class_='desktop-tile')
contract_lengths = ["24", "12", "No contract"]


def remove_text_inside_brackets(text, brackets="()"):
    count = [0] * (len(brackets) // 2)  # count open/close brackets
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b:  # found bracket
                kind, is_close = divmod(i, 2)
                count[kind] += (-1)**is_close  # `+1`: open, `-1`: close
                if count[kind] < 0:  # unbalanced bracket
                    count[kind] = 0  # keep it
                else:  # found bracket to remove
                    break
        else:  # character is not a [balanced] bracket
            if not any(count):  # outside brackets
                saved_chars.append(character)
    return ''.join(saved_chars)


def add_starhub_products():
    pointer = 0
    for section in narrow:
        plans = section.find_all('div', class_='tile-wrapper')
        for plan in plans:
            plan_name = plan.find('div', class_='data-plan-name')

            plan_data = plan.find('div', class_='data-plan-gigs')

            plan_cost_div = plan.find('div', class_="data-plan-cost")
            plan_cost = plan_cost_div.find('span')

            plan_desc = plan.find('div', class_="data-plan-desc")

            plan_sms = plan.find('li', text=lambda t: t and "SMS" in t)

            plan_calltime = plan.find('li', text=lambda t: t and "mins" in t)

            plan_desc_points = plan_desc.find_all('li')

            # print("name:" + plan_name.text, end='\n')
            # print("data:" + plan_data.text.replace('GB', ''), end='\n')
            # if plan_sms is not None:
            #     print("sms:" + plan_sms.text.replace('SMS', ''), end="\n")
            # if plan_calltime is not None:
            #     print("calltime:" +
            #           remove_text_inside_brackets(plan_calltime.text.replace('outgoing mins', '')), end="\n")
            # print(
            #     "cost:" + remove_text_inside_brackets(plan_cost.text.replace('$', '')), end='\n')
            # for points in plan_desc_points:
            #     print(points.text, end='\n')
            # print('\n')

            telco = "Starhub"
            title = telco + " " + plan_name.text
            category = "Postpaid"
            price = remove_text_inside_brackets(
                plan_cost.text.replace('$', ''))
            data = plan_data.text.replace('GB', '')
            call_time = remove_text_inside_brackets(plan_calltime.text).replace(' outgoing mins', '').replace(',', '').replace(' \xa0', '')
            if plan_sms is not None:
                sms = plan_sms.text.replace('SMS', '')
            else:
                sms = 0
            contract_length = contract_lengths[pointer]
            description = ""

            for points in plan_desc_points:
                if description != "":
                    description = description + ", " + points.text
                else:
                    description = points.text

            plan_item = {
                'telco': telco,
                'title': title,
                'category': category,
                'price': price,
                'data': data,
                'call_time': call_time,
                'sms': sms,
                'contract_length': contract_length,
                'description': description           
            }

            starhub_all_plans.append(plan_item)

        pointer = pointer + 1


