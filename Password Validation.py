import re
password=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
s="Vikas@123"
match=re.search(password,s)
if match:
    print("valid password")