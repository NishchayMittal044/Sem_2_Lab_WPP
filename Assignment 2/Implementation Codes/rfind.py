string = "My name is Nishchay"
substring = "is"
    
len_string = len(string)

len_substring = len(substring)


ans = -1

for i in range(len_string - len_substring, -1, -1):
    flag = True
        
    for j in range(len_substring):
        if string[i + j] != substring[j]:
            flag = False
            break
    if flag:
        ans =  i
        break
print("The implementation of rfind gives :",ans)


