# Lightweight MSISDN representation as a Python class and fake MSISDN generator

## SimpleMSISDN
This package was started as apart of testing CDR (Call Detail Record) files generation and later I decided to make 
a separate repository for MSISDNs only.

Use it in Python code like below:
```
from simplemsisdn import SimpleMSISDN

newnumber = SimpleMSISDN(country_code='some country code', 
                         national_destination_code='some national destination code', 
                         subscriber_number='some subscriber number')
```

## FakeMSISDNGenerator
The repository also includes Fake MSISDN generator class which is of general purpose and 
configurable with the parameters passed to the constructor. The class is for creating the simulation data in various test cases

**Fake MSISDN** generator imports national destination codes from the ```ua_ndc``` module which 
contains two lists for the valid Ukrainian landline and mobile ndcs gathered from Wikipedia. To replace it with 
different references just prepare another destination codes module and replace the import
 in fake_msisdn_generator module. 
 Currently I am not going to cover all the countries' destination codes. 
 If you want to include anything for extension into this repo please send me a note (nomadrain@gmail.com)


FakeMSISDNGenerator makes use of SimpleMSISDN and can be invoked as below:
```
anumber = FakeMsisdnGenerator(allowed_country_codes=('380',),
                              allowed_national_destination_codes=mobile_ndc,
                              subscriber_number_length=7)
for numcount in range(10):
    print(str(anumber.get()))

print()

for numcount in range(10):
    print(repr(anumber.get()))
```

Each time when called ```FakeMsisdnGenerator.get()``` method will produce 
a new fake number basing on the provided constructor parameters.

For the invocation with the parameters listed above the output will be like below 

**all coincidences with real numbers are artificial and non-intended**
```
+380-63-1093245
+380-39-8501255
+380-94-8001598
+380-39-1977503
+380-66-3426067
+380-97-5192392
+380-96-1159778
+380-95-8216678
+380-63-7074756
+380-98-2686848

380941347925
380394049112
380667919089
380390100878
380676478840
380959549396
380509295168
380503150128
380952222830
380948711415
```

## Tests

* Tests require unittest Python lib installed. 
Just run it to make sure nothing is broken during the latest commits.
* Tests cover both SimpleMSISDN and FakeMsisdnGenerator classes

## Installation
I did not create a PyPi package for this repository because currently FakeMsisdnGenerator uses local data for sampling. Nevertheless, this behavior can be easily changed using
the class parameters.

In the meantime please install the provided libraries using 'git clone':                     
```
git clone https://github.com/nomadrain/simple_msisdn_python.git
```
or download the whole zip package and extract to the desirable destination
