# you must install
# pip install geocoder
# pip install phonenumbers      
import phonenumbers
from phonenumbers import geocoder
#forexample +90598569845
phone_number1 = phonenumbers.parse("+phonenumber") 


print(geocoder.description_for_number(phone_number1,"tr")) #TR in Turkey users default "en"
