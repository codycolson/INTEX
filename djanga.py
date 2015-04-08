#!/usr/bin/env python

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django
django.setup()

from chf import models as chfmod
from django.db import connection
import subprocess
import sys
from django.contrib.auth.models import Group, Permission
from datetime import datetime, timedelta

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

address1 = chfmod.Address()
address1.street1 = '2300 North State st.'
address1.city = 'Orem'
address1.state = 'UT'
address1.zip_code = '84606'
address1.save()

address2 = chfmod.Address()
address2.street1 = '788 East 750 North'
address2.city = 'Provo'
address2.state = 'UT'
address2.zip_code = '84606'
address2.save()

user = chfmod.User()
user.first_name = 'Homer'
user.last_name = 'Simpson'
user.username = 'homer'
user.email = 'codymcolson@gmail.com'
user.set_password('password')
user.is_superuser = True
user.is_staff = True
user.save()
print('User Cody Created')

user1 = chfmod.User()
user1.first_name = 'Bart'
user1.last_name = 'Simpson'
user1.username = 'bart'
user1.email = 'mrcolson12@gmail.com'
user1.set_password('password')
user1.is_staff = True
user1.save()
print('User Blake Created')

user2 = chfmod.User()
user2.first_name = 'Marge'
user2.last_name = 'Simpson'
user2.username = 'marge'
user2.email = 'cody.colson@mozenda.com'
user2.set_password('password')
user2.save()
print('User Jordan Created')

cat1 = chfmod.Category()
cat1.name = 'Weapons'
cat1.save()

cat2 = chfmod.Category()
cat2.name = 'Decoration'
cat2.save()

cat3 = chfmod.Category()
cat3.name = 'Clothing'
cat3.save()

cat4 = chfmod.Category()
cat4.name = 'Custom Orders'
cat4.save()

subcat1 = chfmod.SubCategory()
subcat1.name = "Hats"
subcat1.category = cat3
subcat1.save()

subcat2 = chfmod.SubCategory()
subcat2.name = "Pants"
subcat2.category = cat3
subcat2.save()

subcat3 = chfmod.SubCategory()
subcat3.name = "Shirts"
subcat3.category = cat3
subcat3.save()

subcat4 = chfmod.SubCategory()
subcat4.name = "Uniforms"
subcat4.category = cat3
subcat4.save()

photo = chfmod.Photograph()
photo.image = "chf/media/oldhat.jpg"
photo.save()

photo = chfmod.Photograph()
photo.image = "chf/media/oldpants.jpg"
photo.save()

photo = chfmod.Photograph()
photo.image = "chf/media/uniform.jpg"
photo.save()

photo = chfmod.Photograph()
photo.image = "chf/media/blueuniform.jpg"
photo.save()

photo = chfmod.Photograph()
photo.image = "chf/media/rifle.jpg"
photo.save()

prod1 = chfmod.RentalProduct()
prod1.name = "this hat"
prod1.description = "Do you see how nice it is?"
prod1.manufacturer = "CHF"
prod1.average_cost = 20
prod1.price = 30
prod1.category = cat3
prod1.subcategory = subcat1
prod1.sku = 1234567890
prod1.photo = chfmod.Photograph.objects.get(id=1)
prod1.quantity_on_hand = 5
prod1.cost = 35
prod1.notes = "I hate this hat"
prod1.times_rented = 4
prod1.price_per_day = 5
prod1.save()

prod2 = chfmod.RentalProduct()
prod2.name = "ragged pants"
prod2.description = "You do not want these pants."
prod2.manufacturer = "CHF"
prod2.average_cost = 50
prod2.price = 70
prod2.category = cat3
prod2.subcategory = subcat2
prod2.sku = 123456789
prod2.photo = chfmod.Photograph.objects.get(id=2)
prod2.quantity_on_hand = 1
prod2.cost = 35
prod2.notes = "I hate these pants"
prod2.times_rented = 4
prod2.price_per_day = 5
prod2.save()

prod3 = chfmod.ProductSpecification()
prod3.name = "Uniform that was actually worn"
prod3.description = "It hasn't been washed."
prod3.manufacturer = "CHF"
prod3.average_cost = 50
prod3.price = 120
prod3.category = cat3
prod3.subcategory = subcat4
prod3.sku = 12345678
prod3.photo = chfmod.Photograph.objects.get(id=3)
prod3.quantity_on_hand = 1
prod3.save()

prod4 = chfmod.ProductSpecification()
prod4.name = "Blue uniform"
prod4.description = "Very handsome"
prod4.manufacturer = "CHF"
prod4.average_cost = 50
prod4.price = 150
prod4.category = cat3
prod4.subcategory = subcat4
prod4.sku = 1234567
prod4.photo = chfmod.Photograph.objects.get(id=4)
prod4.quantity_on_hand = 1
prod4.save()

prod5 = chfmod.ProductSpecification()
prod5.name = "Rifle"
prod5.description = "This is a dangerous gun. Do not fire."
prod5.manufacturer = "Smith & Wesson"
prod5.average_cost = 200
prod5.price = 499
prod5.category = cat1
prod5.sku = 123456
prod5.photo = chfmod.Photograph.objects.get(id=5)
prod5.quantity_on_hand = 5
prod5.save()

photo3 = chfmod.Photograph()
photo3.image = 'item/media/printing_press.jpg'
photo3.save()

p1 = chfmod.ProductSpecification()
p1.name = 'Comfy Boots'
p1.price = 1000.00
p1.description = 'These are easily the best boots you will ever wear.'
p1.manufacturer = 'Smith & Wesson'
p1.category = chfmod.Category.objects.get(name='Clothing')
p1.sku = 123456789
p1.average_cost = 1000.00
p1.photo = chfmod.Photograph.objects.create(image="chf/media/boots.jpg")
print('image #1:' + p1.photo.image)
p1.quantity_on_hand = 5
p1.shelf_location = 'somehwere'
p1.save()

p2 = chfmod.ProductSpecification()
p2.name = 'Old Flag'
p2.price = 100.50
p2.description = 'Just a flag'
p2.manufacturer = "'Merica"
p2.category = chfmod.Category.objects.get(name='Decoration')
p2.sku = 123456789
p2.average_cost = 100.00
p2.photo = chfmod.Photograph.objects.create(image="chf/media/old_flag.jpg")
print('image #2:' + p2.photo.image)
p2.quantity_on_hand = 1
p2.shelf_location = 'somehwere'
p2.save()

p3 = chfmod.ProductSpecification()
p3.name = 'Custom Basket'
p3.price = 80.00
p3.description = 'This is a homeade basket made for you by a professional basketweaver.'
p3.manufacturer = 'Basketweaver'
p3.category = chfmod.Category.objects.get(name='Custom Orders')
p3.sku = 123456789
p3.average_cost = 80.00
p3.photo = chfmod.Photograph.objects.create(image="chf/media/basket.jpg")
print('image #1:' + p1.photo.image)
p3.quantity_on_hand = 5
p3.shelf_location = 'somehwere'
p3.order_form_name = 'chf/media/basket_order.pdf'
p3.save()

# prod = chfmod.RentalProduct()
# prod.name = "the thing"
# prod.price = 2.00
# prod.save()

# item = chfmod.RentalItem()
# item.date_due = '2014-3-6'
# item.rental_product= chfmod.RentalProduct.objects.get(id=prod.id)
# item.save()

event = chfmod.Event()
event.name = 'Colonial Heritage Festival'
event.description = 'Annual gathering of colonial heritage fans. Fun for all ages.'
event.start_date = '2015-04-20'
event.end_date = '2015-04-23'
event.map_file_name = 'CHF-2015.pdf'
event.venue_name = 'Scera Outdoor Park'
event.address = chfmod.Address.objects.get(id=address1.id)
event.save()

area = chfmod.Area()
area.name = 'Cow milking'
area.description = 'People will come and milk cows for enjoyment'
area.event = chfmod.Event.objects.get(id = event.id)
area.place_number = 1
area.save()

area = chfmod.Area()
area.name = 'Blacksmith'
area.description = 'Make a horseshoe to take home!'
area.event = chfmod.Event.objects.get(id = event.id)
area.place_number = 2
area.save()

area = chfmod.Area()
area.name = 'Civil war musket-shooting'
area.description = 'Shoot a gun, win a prize.'
area.event = chfmod.Event.objects.get(id = event.id)
area.place_number = 3
area.save()

eventItem = chfmod.ExpectedSaleItem()
eventItem.name = 'Cow milking bucket'
eventItem.description = "It's a bucket for milking cows, keep it forever as a memory to this epic day when you milked a cow with your bare hands."
eventItem.low_price = 2.00
eventItem.high_price = 10.00
eventItem.photo = chfmod.Photograph.objects.create(image="chf/media/bucket.jpg")
eventItem.event = chfmod.Event.objects.get(id = event.id)
eventItem.save()

eventItem = chfmod.ExpectedSaleItem()
eventItem.name = 'Horseshoe'
eventItem.description = "Buy some metal and forge your own shoe."
eventItem.low_price = 12.00
eventItem.high_price = 25.00
eventItem.photo = chfmod.Photograph.objects.create(image="chf/media/shoe.png")
eventItem.event = chfmod.Event.objects.get(id = event.id)
eventItem.save()

eventItem = chfmod.ExpectedSaleItem()
eventItem.name = 'Basket'
eventItem.description = "Get a basket made for you and your family. Customizable."
eventItem.low_price = 30.00
eventItem.high_price = 50.00
eventItem.photo = chfmod.Photograph.objects.get(image="chf/media/basket.jpg")
eventItem.event = chfmod.Event.objects.get(id = event.id)
eventItem.save()

rental = chfmod.RentalProduct()
rental.name = "Martha Washington's dress"
rental.price = 50000.00
rental.description = "Martha's actual dress. Handle with great care."
rental.manufacturer = 'Colonial Outerwear'
rental.average_cost = 35000.00
rental.sku = '23gK85hQT56'
rental.order_form_name = ''
rental.production_time = ''
rental.category = cat3
rental.subcategory = subcat3
rental.shelf_location = 'in the back'
rental.product_order_file = ''
rental.photo = chfmod.Photograph.objects.create(image="chf/media/dress.jpg")
rental.serial_number = 'asdpfi136137qef'
rental.date_acquired = '2014-03-07'
rental.cost = rental.average_cost
rental.notes = 'Pristine condition. Selective rentals only.'
rental.price_per_day = 250.00
rental.save()

rental2 = chfmod.RentalProduct()
rental2.name = 'Green Dress'
rental2.price = 1500.00
rental2.description = "It's an old timey dress"
rental2.manufacturer = 'Colonial Collectables'
rental2.average_cost = 1500.00
rental2.sku = '23gK85hQT56-67rpV'
rental2.order_form_name = ''
rental2.production_time = '2.5 months on average'
rental2.category = cat3
rental2.subcategory = subcat3
rental2.shelf_location = 'In the locker'
rental2.product_order_file = ''
rental2.photo = chfmod.Photograph.objects.create(image="chf/media/dress_green.jpg")
rental2.serial_number = 'g1645Frif6137qef'
rental2.date_acquired = '2014-09-07'
rental2.cost = rental.average_cost
rental2.notes = 'Slight rip along seam. Good condition.'
rental2.price_per_day = 20.00
rental2.save()

transaction = chfmod.Transaction()
transaction.order_date = datetime.today()
transaction.customer = user
transaction.save()

rent = chfmod.RentalItem()
rent.rental_product = chfmod.RentalProduct.objects.get(id=rental.id)
rent.date_due = '2014-11-26 00:00:00'
rent.amount = rent.rental_product.price_per_day * 7
rent.date_in = None
rent.discount_percent = None
rent.transaction = transaction
rent.save()
rent.date_out = '2014-11-25 00:00:00'
rent.save()

rent2 = chfmod.RentalItem()
rent2.rental_product = chfmod.RentalProduct.objects.get(id=rental2.id)
rent2.date_due = '2014-11-26 00:00:00'
rent2.amount = rent.rental_product.price_per_day * 7
rent2.date_in = None
rent2.discount_percent = None
rent2.transaction = transaction
rent2.save()
rent2.date_out = '2014-11-25 00:00:00'
rent2.save()


transaction.save()

transaction = chfmod.Transaction()
transaction.order_date = '2015-01-02 00:00:00'
transaction.customer = user1
transaction.save()

rent = chfmod.RentalItem()
rent.rental_product = chfmod.RentalProduct.objects.get(id=prod1.id)
rent.date_due = '2015-01-10 00:00:00'
rent.amount = rent.rental_product.price_per_day * 7
rent.date_in = None
rent.discount_percent = None
rent.transaction = transaction
rent.save()
rent.date_out = '2014-01-07 00:00:00'
rent.save()

rent2 = chfmod.RentalItem()
rent2.rental_product = chfmod.RentalProduct.objects.get(id=prod2.id)
rent2.date_due = '2015-01-10 00:00:00'
rent2.amount = rent.rental_product.price_per_day * 7
rent2.date_in = '2015-01-09 00:00:00'
rent2.discount_percent = None
rent2.transaction = transaction
rent2.save()
rent2.date_out = '2014-01-07 00:00:00'
rent2.save()

transaction.save()

transaction = chfmod.Transaction()
transaction.order_date = '2014-10-03 00:00:00'
transaction.customer = user
transaction.save()

rent = chfmod.RentalItem()
rent.rental_product = chfmod.RentalProduct.objects.get(id=prod2.id)
rent.date_due = '2015-02-10 00:00:00'
rent.amount = rent.rental_product.price_per_day * 7
rent.date_in = None
rent.discount_percent = None
rent.transaction = transaction
rent.save()
rent.date_out = '2015-02-03 00:00:00'
rent.save()

transaction.save()

transaction = chfmod.Transaction()
transaction.order_date = '2015-03-05 00:00:00'
transaction.customer = user2
transaction.save()

item = chfmod.SaleItem()
item.quantity = 4
item.product = prod3
item.transaction = transaction
item.save()

item = chfmod.SaleItem()
item.quantity = 1
item.product = prod4
item.transaction = transaction
item.save()

item = chfmod.SaleItem()
item.quantity = 10
item.product = prod5
item.transaction = transaction
item.save()

item = chfmod.SaleItem()
item.quantity = 1
item.product = p1
item.transaction = transaction
item.save()

transaction.save()