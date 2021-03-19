# Lightweight MSISDN representation as a Python class

Use it in Python code like below:

from simplemsisdn import SimpleMSISDN

newnumber = SimpleMSISDN(country_code={some country code}, 
                         national_destination_code={some national destination code}, 
                         subscriber_number={some subscriber number})
