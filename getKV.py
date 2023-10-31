import json




with open('cookies.txt','r') as f:
    cookieslist = json.load(f)
    
print(cookieslist)