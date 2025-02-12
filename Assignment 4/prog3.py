def panagram(sen):
    sentence=sen
    char='a'
    sentence=sentence.lower()#all characters lower cased
    sentence=sentence.replace(" ", "")#removed spaces
    sentence=set(sentence)#remove duplicates
    sentence=sorted(sentence)#sort the set
    sentence=''.join(sentence)#convert to string
    if len(sentence)<26:
        return False
    else:
        for letter in sentence:
            if letter.isdigit():
                continue
            if letter==char:
                char=chr(ord(char)+1)
                continue
            else:
                return False
        
        
    
    return True
        
        
def main():
    sen=input("Enter a sentence to check if panagram or not")
    sen.split()
    result=panagram(sen)
    if result==False:
        print("Not a panagram")
    elif result==True:
        print("Panagram")
if __name__=='__main__':
    main()
    