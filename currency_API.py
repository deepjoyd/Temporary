import requests

response=requests.get("https://currencyapi.net/api/v1/rates?key=E8hXc64oI1nYsQJEmKWrCHErreNXpjAyBP6v&base=USD")
data=response.json()
print(data)
rates=data['rates']

def arbtusd(x,s):
    return float(x/s)

def usdtarb(x,s):
    return float(x*s)

def USDTR(x):
    return x*float(rates['INR'])


def RTUSD(x):
    return x/float(rates['INR'])


def ETR(x):
    y=arbtusd(x,rates['EUR'])
    return USDTR(y)


def RTE(x):
    y=RTUSD(x)
    return usdtarb(y,rates['EUR'])


def PTR(x):
    y=arbtusd(x,rates['GBP'])
    return USDTR(y)


def RTP(x):
    y=RTUSD(x)
    return usdtarb(y,rates['GBP'])

def AUDTR(x):
    y=arbtusd(x,rates['AUD'])
    return USDTR(y)


def RTAUD(x):
    y=RTUSD(x)
    return usdtarb(y,rates['AUD'])


print("Operations available:", "1.US Dollars to Rupees", "2.Rupees to US Dollars", "3.Euros to Rupees", "4.Rupees to Euros",
          "5.Pound Sterling to Ruppees", "6.Rupees to Pound Sterling", "7.Australian Dollars to Rupees", "8.Rupees to Australian Dollars", sep="\n")
x=float(input("Operation to perform: "))
if(x<1 or x>8):
    print("ERROR")
else:
    y=float(input("Enter Amount: "))
    
if x==1:
    print(USDTR(y),"INR", sep=" ")
elif x==2:
    print(RTUSD(y),"USD", sep=" ")
elif x==3:
    print(ETR(y),"INR", sep=" ")
elif x==4:
    print(RTE(y),"EUR", sep=" ")
elif x==5:
    print(PTR(y),"INR", sep=" ")
elif x==6:
    print(RTP(y),"GBP", sep=" ")
elif x==7:
    print(AUDTR(y),"INR", sep=" ")
elif x==8:
    print(RTAUD(y),"AUD", sep=" ")







