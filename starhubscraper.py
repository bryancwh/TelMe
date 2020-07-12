import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()

import requests
from bs4 import BeautifulSoup
from products.models import Product

#from django.core.mail import send_mail
#from profiles.models import FavoritesProducts

URL = 'https://www.starhub.com/personal/mobile.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='tab-content')
narrow = results.find_all('div', class_='desktop-tile')
contract_lengths = ["2 years", "1 year", "No contract"]


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
            price = int(remove_text_inside_brackets(
                plan_cost.text.replace('$', '')))
            data = int(plan_data.text.replace('GB', ''))
            call_time = remove_text_inside_brackets(
                plan_calltime.text.replace(' outgoing mins', ''))
            if plan_sms is not None:
                sms = plan_sms.text.replace('SMS', '')
            else:
                sms = 0
            contract_length = contract_lengths[pointer]
            description = ""
            for points in plan_desc_points:
                description = description + points.text + "\n"
            product = Product.objects.create(
                title=title, telco=telco, category=category, price=price, data=data, call_time=call_time, sms=sms,
                contract_length=contract_length, description=description,
            )
            product.save()
        pointer = pointer + 1



if __name__ == '__main__':
    add_starhub_products()
    print('Done.')

#  #check if the price of product has dropped
#  if data['last_price'] < item.requested_price:
#    #filter out users who have this product in their favorites list
#    users = FavoritesProducts.objects.filter(product=item).only("user")
#    
#    #send email to each user
#    for user in users:
#        email_message = item + " in your Favorites List has dropped in price, go check it out now!"
#        send_mail(
#            'Price dropped, act now!',
#            email_message,
#            'TelMe <bryancwh98@gmail.com>',
#            [user.email],
#            fail_silently=False,
#        )