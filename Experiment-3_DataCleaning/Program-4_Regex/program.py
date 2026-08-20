import re
text="This is\t a \n test"
split_text=re.split(r'\s+',text)
print(split_text)