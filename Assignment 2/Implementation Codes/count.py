string = "Hello world, Hello India "
search = "Hello"

len_string = len(string)
len_search = len(search)

count = 0
i=0

while i < len_string:
    if string[i:len_search+i] == search:
        count +=1
        i = i+ len_search
    else:
        i +=1
print(count)