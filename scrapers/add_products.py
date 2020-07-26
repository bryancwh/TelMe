from products.models import Product
from scrapers.starhubscraper import starhub_all_plans
#from scrapers.singtelscraper import singtel_all_plans
from scrapers.m1scraper import m1_all_plans
from scrapers.myrepublicscraper import myrepublic_all_plans
from scrapers.gigascraper import giga_all_plans

all_plans = []

def add_all_products():
    all_plans = starhub_all_plans + m1_all_plans + myrepublic_all_plans + giga_all_plans #+ singtel_all_plans
    # this can be used to test the price drop. it requires you to add the run the scrape without it first then run it with it.
    # plan_item = {
    #             'telco': "Starhub",
    #             'data': "15",
    #             'contract_length': "No Contract",
    #             'title': "Starhub $55 2-year plan",
    #             'category': "Postpaid",
    #             'price': "45.00",
    #             'call_time': "100",
    #             'sms': "0",
    #             'description': "details",         
    #         }
    # all_plans.append(plan_item)
    for product in all_plans:
        if not Product.objects.filter(title=product['title']):
            product = Product.objects.create(
                    title=product['title'], telco=product['telco'], category=product['category'], price=product['price'], data=int(product['data']), call_time=product['call_time'], sms=product['sms'],
                    contract_length=int(product['contract_length']), description=product['description'],
                )
            product.save()
        else:
            if Product.objects.filter(title=product['title'], price__gt=product['price']):
                print("price dropped, change the price of product and infrom users")
            else:
                # this else statement is not needed
                print("do nothing, product already exists")


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