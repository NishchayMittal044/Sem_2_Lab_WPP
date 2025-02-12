def palindrome(sentence):
    count = 0
    n = len(sentence)
    for i in range (n//2):
        count += abs(ord(sentence[i])-ord(sentence[n-i-1]))

    return count

def main():
    test = int(input("Enter the number of test cases :"))
    result = []
    for i in range (test):
        sentence = input("Enter the sentence :")
        result.append(palindrome(sentence))
    
    print("\n".join(map(str,result)))

if __name__ == "__main__":
    main()
