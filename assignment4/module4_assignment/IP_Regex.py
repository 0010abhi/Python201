import re
data="my system ip address is 103.23.32.241 and my friend's system ip address is 98.103.12.190"
matches=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',data)
for match in matches:
    print match