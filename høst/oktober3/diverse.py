'''
I dette programmet finnes
- if (eksisterer)
- if/else
- str metoden "".listHere.join()"
- str metoden rsplit 
- oversette ascii
'''


# '''
firstValue = None
secondValue = None
'''
firstValue = input("input a value: ")
secondValue = input("input another value: ")
'''

if firstValue:
    print(f"first value is exists. It is{firstValue}")
    if firstValue.isnumeric():
        print(f"the first value ({firstValue}) is a number")
    else:
        print(f"the first value - {firstValue} - is not a number")

if secondValue:
    print(f"second value exists. It is {secondValue}")
    

mydict = {
    "asdf": "asdf", "sadf":1, "namedItem":2, "sky-blue": 2
}



print(f'{" and ".join(mydict)} are in my dictionary')

dict2 = {
    "a2":2,"1":1
}
# join kan kun brukes med str som key

print(f'{" and ".join(dict2)} are in my dictionary')

filen = open('mylist.txt') #må åpnes fra oktober3
inptxt = filen.read()

string = "apple, banana, cherry"

# x = string.rsplit(", ")
x = inptxt.rsplit(", ")

print(x) 


#ascii 
ordbok = {80: 77, 81: 78,82 : 79 ,83:  80, 84:81, 97:108, 100:117, 116:101}

txt = "this is a dictionary"

print(txt.translate(ordbok))
