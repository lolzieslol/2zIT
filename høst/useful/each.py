'''
Programmet deler opp lister

bruksområde
- konvertere til excel/google sheets -vennlig format

'''


koffein : list = [266,287,307,276,293,298,281,285,262,228]

def printeach(mylist : list): 
    for number in mylist:
        print(number)
        
printeach(koffein)