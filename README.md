# Lightweight mobile phone number (MSISDN) representation as a Python class and fake MSISDN generator

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
contains two lists for the valid Ukrainian landline and mobile NDCs gathered from Wikipedia. To replace it with 
different references just prepare another destination codes module and replace the import
 in fake_msisdn_generator module. 
 Currently I am not going to cover all the countries' destination codes. 
 If you want to include anything for extension into this repo please send me a note (nomadrain@gmail.com)


FakeMSISDNGenerator makes use of SimpleMSISDN and can be invoked as below:
```
anumber = FakeMsisdnGenerator(allowed_country_codes=('999',),
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
+999-68-2810437
+999-96-4388457
+999-67-9642448
+999-67-7530780
+999-97-6872919
+999-68-2857783
+999-50-9801429
+999-92-8556433
+999-93-0827561
+999-99-6211828

999986426306
999669327617
999998887083
999686668838
999927606255
999999837217
999508727895
999662919604
999987611076
999959028298

Process finished with exit code 0

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
