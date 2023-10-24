
class Tekst():
    def __init__(self, tekstStr):
        self.plaintekst = tekstStr
        self.len = len(tekstStr)



def split_into_sentences(text: str) -> list[str]:
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
    print("you have to write a number, desimalcs are with '.' not ',' and no text")


sentences : list = split_into_sentences(inp)

from time import sleep

print()
print("----")
print()
# for sentence in sentences:
#     print(sentence)
#     print()
#     sleep(sleepInterval)