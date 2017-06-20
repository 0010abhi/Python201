import re
data="my social security number is 123-92-1924 and my friend ssn number is 000-00-0000 and son ssn number is 104-12-4235"
#regex to find valid ssn...
matches=re.findall(r"(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}",data)
#printing all matches in an expression
for match in matches:
    print match