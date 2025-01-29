text = "hello , hello my name is Nishchay"
old= "hello"
new  = "hi"


result = ""
i = 0
old_len = len(old)

while i < len(text):
        # Check if the substring matches `old`
    if text[i:i+old_len] == old:
        result += new  # Append the replacement string
        i += old_len  # Move past the replaced part
    else:
        result += text[i]  # Append the current character
        i += 1  # Move to the next character
print(result)
    


