
class Tekst():
    def __init__(self, tekstStr):
        self.plaintekst = tekstStr
        self.len = len(tekstStr)



def split_into_words(text: str) -> list[str]:
    sentences = text.split(" ")
    sentences = [s.strip() for s in sentences]
    if sentences and not sentences[-1]: sentences = sentences[:-1]
    return sentences

inp : str = input("tekst: ")

tekstObjekt = Tekst(inp)

sleepInterval = input("how many seconds wait? (e.g. 0.2)")

if sleepInterval.isnumeric:
    sleepInterval = float(sleepInterval)
    
else:
    print("you have to write a number, desimalcs are with '.' not ',' and text may not be included")


words : list = split_into_words(inp)

from time import sleep

def printOneAtATime(theList : list):
    
    #aesthetics
    print()
    print("----") 
    print()
    
    #prints each element in a list
    for each in theList:
        print(each)
        print()
        sleep(sleepInterval)
        
printOneAtATime(words)