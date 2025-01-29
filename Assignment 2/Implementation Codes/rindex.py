string = "Hello my name is Nishchay"
substring = "is"

len_string = 0
len_substring = 0

for char in string:
    len_string += 1

for char in substring:
    len_substring += 1

if len_substring == 0:
    print("Empty substring")
    exit()
if len_substring > len_string:
    print("Substring not found")
    exit()

ans = -1

for i in range(len_string - len_substring, -1, -1):
    flag = True
    for j in range(len_substring):
        if string[i + j] != substring[j]:
            flag = False
            break
    if flag:
        ans = i
        break

if ans != -1:
    print(ans)
else:
    print("Substring not found")


