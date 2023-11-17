'''
viser frem en gitt tekst
'''

#retrieves text
text = input()

#divides the text into segments of five words

def main(text : str):
    textLenRemaining = len(text)
    while textLenRemaining > 4:
        text = text
        #read all characters, each time it encounters a space add to word count when reached 5 append those charcs
        # for word in text:
        #     if word =="":
        #         counter+=1
        
        
        textLenRemaining-1


#viser ord per (5) ord 

main(text)


###
#antall ord i teksten 
# antOrd = tekst.count(' ')