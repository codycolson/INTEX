from django.db import models
from django.contrib.auth.models import AbstractUser
from polymorphic import PolymorphicModel
import requests
from datetime import datetime


class Address(models.Model):
    street1 = models.TextField(max_length=200)
    street2 = models.TextField(max_length=200, null=True, blank=True)
    city = models.TextField(max_length=100)
    state = models.TextField(max_length=20)
    zip_code = models.TextField(max_length=20)

    class Meta:
        ordering = ['state', 'city', 'zip_code', 'street1', 'street2']
        verbose_name_plural = 'addresses'

    def __str__(self):
        return '{} {} {}, {}  {}'.format(self.street1, self.street2, self.city, self.state, self.zip_code)

class Photograph(models.Model):
    '''
        A photo.
    '''
    date_taken = models.DateTimeField(null=True)
    place_taken = models.TextField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.TextField()

    def __str__(self):
        return self.image

class User(AbstractUser):
    '''
        A user.
    '''
    phone = models.TextField(max_length=40)
    security_question = models.TextField(max_length=200)
    security_answer = models.TextField(max_length=200)
    organization_name = models.TextField(max_length=200, null=True, blank=True)
    organization_type = models.TextField(max_length=40, null=True, blank=True)
    date_appointed_agent = models.DateField(null=True)
    emergency_contact = models.TextField(max_length=200, null=True, blank=True)
    emergency_phone = models.TextField(max_length=200, null=True, blank=True)
    emergency_relationship = models.TextField(max_length=200, null=True, blank=True)
    address = models.ForeignKey(Address, related_name='+', null=True, blank=True)
    photo = models.ForeignKey(Photograph, related_name='+', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Event(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    map_file_name = models.TextField(max_length=200, null=True)
    venue_name = models.TextField(max_length=200, null = True)
    address = models.ForeignKey(Address, related_name='+',null=True)

class Area(models.Model):
    '''
        An area of an event.
    '''
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    place_number = models.PositiveIntegerField()
    event = models.ForeignKey(Event, related_name='+')
    photo = models.ForeignKey(Photograph, null = True)

class ExpectedSaleItem(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.TextField(max_length=200)
    event = models.ForeignKey(Event, related_name='+')

class Transaction(models.Model):
    order_date = models.DateTimeField()
    phone = models.TextField()
    date_packed = models.DateTimeField(null=True)
    date_shipped = models.DateTimeField(null=True)
    tracking_number = models.FloatField(null=True)
    ships_to = models.ForeignKey('Address', related_name='+', null = True)
    packed_by = models.ForeignKey('User', related_name='packedby_set', null = True)
    payment_processed_by = models.ForeignKey('User', related_name='paymentprocessedby_set', null = True)
    shipped_by = models.ForeignKey('User', related_name='shippedby_set', null = True)
    handled_by = models.ForeignKey('User', related_name='handledby_set', null = True)
    customer = models.ForeignKey('User', related_name='orders', null = True)
    cc_charge_id = models.TextField(null = True)
    date_charged = models.DateTimeField(null = True)
    #confirmation = models.TextField(null = True)

    @property
    def number_of_items(self):
        items = self.LineItem
        return_dictionary = {}
        for item in items:
            if type(item) == SaleItem:
                return_dictionary[item.name] = item.quantity
            return_dictionary[item.name] = 1
        return return_dictionary

    def add_item(self, line_item):
        line_item.transaction = self
        return None

    @property
    def total(self):
        items = chfmod.LineItem.objects.get(transaction = self.id)
        return_dictionary = {}
        total = 0
        for item in items:
            if type(item) == chfmod.SaleItem:
                return_dictionary[item.name] = item.quantity * item.amount
            else:
                return_dictionary[item.name] = item.amount
            total += return_dictionary[item.name]
        return_dictionary['total'] = total
        return return_dictionary

    def charge_card(self, cc_number, cc_type, cc_exp_month, cc_exp_year, cc_cvc, cc_name):
        API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
        API_KEY = 'd15442a3c476f42f330212a99baa1e26'
        r = requests.post(API_URL, data = {
        'apiKey': API_KEY,
        'currency':'usd',
        'amount': str(transaction_total()) ,
        'type': cc_type,
        'number': cc_number,
        'exp_month': cc_exp_month,
        'exp_year': cc_exp_year,
        'cvc': str(cc_cvc),
        'name': cc_name,
        'description': 'Charge of ' + transaction_total() + 'to ' + cc_name +'.',
        })

        print(r.text)

        resp = r.json()

        if 'error' in resp:
            print( 'ERROR: ', resp['error'] )
            return False
        else:
            print(resp.keys())
            print(resp['ID'])
            self.cc_charge_id = resp['ID']
            self.date_charged = str(datetime.now())
        return True

    #def convert_cart(self, cart)
    #pass the cart to this function, and it'll convert it to the transaction

class CustomTransaction(Transaction):
    '''
        transaction details for custom orders.
    '''
    date_paid = models.DateTimeField()
class LineItem(models.Model):
    '''
        Abstract base class for line items in a transaction.  A line item can be one
        of sale item, fee, rental item, or service item.
    '''
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    transaction = models.ForeignKey(Transaction, null=True)

    class Meta:
        abstract = True

class Category(models.Model):
    '''
        Category within the product catalog.
    '''
    name = models.TextField(max_length=200)

class SubCategory(models.Model):
    '''

    '''
    name = models.TextField(max_length=200)
    category = models.ForeignKey(Category, related_name='+', null=True)

class ProductSpecification(PolymorphicModel):
    '''
        The specification of a product that is in our catalog.
    '''
    name = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    manufacturer = models.TextField(max_length=80, null=True)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sku = models.TextField(max_length=20, null=True)
    order_form_name = models.TextField(max_length=200, null=True)
    production_time = models.TextField(max_length=200, null=True)
    subcategory = models.ForeignKey(SubCategory, related_name='+', null=True)
    category = models.ForeignKey(Category, related_name='+', null=True)
    owner = models.ForeignKey(User, null=True)
    photo = models.ForeignKey(Photograph, null=True)
    quantity_on_hand = models.IntegerField(null=True)
    shelf_location = models.TextField(max_length=40, null=True)
    product_order_file = models.TextField(null=True)

class SerializedProduct(ProductSpecification):
    '''
        A specific item in our inventory.
    '''
    serial_number = models.TextField(max_length=100, unique=True, null=True)
    date_acquired = models.DateField(auto_now_add=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    for_sale = models.BooleanField(default=True)
    notes = models.TextField(null=True)

class RentalProduct(SerializedProduct):
    '''
        A specific item in our inventory that we are willing to rent.
    '''
    times_rented = models.IntegerField(default=0)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    @property
    def is_rented(self):#returns the date it is due if it is still out because it is rented, false if otherwise
        not_available = chfmod.RentalItem.objects.filter(rental_product = self.id, date_in = None)
        if not_available.exists():
            print('This Item is currently rented by someone else, Sorry. The expected return date is ' + not_available.date_due )
            return not_available.date_due
        return False

    def add_to_transaction(self, due_date, discount, amount, transaction): #rent the actual item. Returns new rental
        if not self.is_rented():
            self.times_rented += 1
            new_rental = chfmod.RentalItem()
            new_rental.date_due = due_date
            new_rental.discount_percent = discount
            new_rental.rental_product = self
            new_rental.transaction = transaction
            new_rental.amount = self.price_per_day * .01 * discount_percent * new_rental.days_late()
            new_rental.save()
        return new_rental

class WardrobeItem(RentalProduct):
    '''
        A wardrobe item in our inventory.
    '''
    size = models.TextField(max_length=40)
    size_modifier =models.TextField(max_length=40)
    gender = models.TextField(max_length=40)
    color = models.TextField(max_length=40)
    pattern = models.TextField(max_length=40)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    note = models.TextField()

class RentalItem(LineItem):
    '''

    '''
    date_out = models.DateTimeField(auto_now_add=True)
    date_in = models.DateTimeField(null=True)
    date_due = models.DateTimeField(null=True)
    discount_percent = models.FloatField(null=True)
    rental_product = models.ForeignKey(RentalProduct, related_name='+')

    @property
    def days_late(self):
        return abs(self.date_due.days - datetime.now()).days > 0

    def return_item(self, damage_fee = None, damage_description = None, damage_waived = False, late_waived = False, late_fee = None): #returns the number of days late if any, else returns 0
        date_in = datetime.now()
        if self.days_late() > 0 and late_fee:
            late_fee = chfmod.LateFee()
            late_fee.days_late = self.days_late()
            late_fee.rental_item = self
            late_fee.waived = late_waived
            late_fee.save()
        if damage_fee.exists():
            dmg_fee = chfmod.DamageFee()
            dmg_fee.waived = damage_waived
            dmg_fee.rental_item = self
            dmg_fee.description = damage_description
            dmg_fee.save()
        if dmg_fee.exists() or late_fee.exists():
            trans = chfmod.Transaction()
            if dmg_fee.exists():
                trans.add_item(dmg_fee)
            if late_fee.exists():
                trans.add_item(late_fee)
            trans.save()
        return True

class Fee(LineItem):
    '''
        Abstract base class for the various fee types.
    '''
    waived = models.BooleanField(default=False)
    rental_item = models.ForeignKey(RentalItem, related_name='+')

    class Meta:
        abstract = True

class LateFee(Fee):
    '''
        A late fee for an item rental.
    '''
    days_late = models.PositiveIntegerField()

class DamageFee(Fee):
    '''
        A damage fee for an item rental.
    '''
    description = models.TextField()

class SaleItem(LineItem):
    '''
        A sale item for either a bulk or a serialized product.
    '''
    quantity = models.IntegerField()
    product = models.ForeignKey(ProductSpecification, related_name='+')
