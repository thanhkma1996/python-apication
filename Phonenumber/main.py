import phonenumbers

from test import number
#kiem tra so dien thoai thuoc nuoc nao
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number,"vn")
print(geocoder.description_for_number(ch_nmber,"en"))

# kiem tra nha mang
from phonenumbers import carrier
service_number = phonenumbers.parse(number,"vn")
print(carrier.name_for_number(service_number,"en"))