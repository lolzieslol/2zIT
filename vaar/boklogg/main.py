'''
Dette er et bokloggføringsprogram.

Mål:
essensielt:
- lage et lokalt kjørt program som kan føre logg av bøker lest av en bruker
- føre bøker som objekter med Tittel (konstant), Forfatter (konstant), Sidetall (konstant), Fremgang (variabel)

evt
- føre statistikk på hvor mye som blir lest og når 
- kommenterar/notat (variabel) til bøkene
- hente bøker fra en ekstern database
- forord som seperat (mtp. seperat sidetellingssystem)


'''

class Book:
    def __init__(self, title: str, author : str, totalPageCount : int):
        
        self.title = title
        self.author = author
        self.totalPageCount = totalPageCount
        self.currentPage = 0

def findbook():
    bookName = input("which book? ")
    
    book = None
    for listedBook in bookList:
        if listedBook.title == bookName:
            book = listedBook
            return book
    else:
        print("It couldn't be found, try adding it!")
        return

def updateProgress():
    anyProgress : bool = input("have you progressed? (True/False) ")
    #Later: add other ways to answer (yes, no, yeah, yup, oui, nah)

    if not anyProgress:
        print("Ok!")
        return
    
    book = findbook()
    
    def askWhatPage() -> None:
        currentpage = int(input(f"Which page are you on now? Last time you were on {book.currentPage} and the book is {book.totalPageCount} pages long. "))
        return currentpage
    
    def validPage(currentpage):
        if currentpage <= book.totalPageCount and currentpage > book.currentPage:
            book.currentPage =currentpage
            return True
        else: 
            print("update unsuccessful, that didn't seem right")
            return False
        
    
    if not validPage(askWhatPage()):
        if not validPage(askWhatPage()):
            if not validPage(askWhatPage()):
                return
        

    print(f"update successful! You are now listed as being on page {book.currentPage} in {book.title}")
    
def checkProgress():
    for listedbook in bookList:
        print(f"In {listedbook.title} you are on page {listedbook.currentPage} of {listedbook.totalPageCount}")

def makeNewBook():
    print("Making new book")
    input()
        

bok1 = Book("Hør her'a", "Gulraiz Sharif", 174)

bookList = [bok1]

# updateProgress()

checkProgress()

