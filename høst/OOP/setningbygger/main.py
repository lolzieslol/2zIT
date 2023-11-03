'''
program som bygger setninger.
- for norsk, funker IKKE i alle språk 

'''

# from ordklasse import *
import ordklasse as o

#definerer
jeg = o.DetPersonligePronomenet("jeg",1,"SubJekt")
er = o.Verbet("er", "presens")
ikke = o.Ordet("ikke")
deg = o.DetPersonligePronomenet("deg",1,"akkusativ")

#skriver ut

print(jeg(), er(), jeg.form)

if jeg() == deg():
    print("hæ")
else: 
    print(jeg(),er(),ikke(), deg())