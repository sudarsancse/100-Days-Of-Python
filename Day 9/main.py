# dictinory 

""" programin_dictinory= {
    "name":"sudarsan sarkar",
    "age" : 21,
    "nic-name":"sarkar"
}

for word in programin_dictinory:
    print(programin_dictinory[word]) """

## nested list 
""" travel_log = {
    "France" :["paris" , "lille", "dijon"],
    "germany" : ["stutguart" , "berlin"]
}

print(travel_log["France"][1]) """

""" latt = ["a" , "b",["c" , ["d", "e"]]]

print(latt[2][1][0]) """


## nested dictonary
""" city_name = {
    "France" :{"key1":"paris" ,"key2": "lille","key3": "dijon"},
    "germany" : ["stutguart" , "berlin"]
}

print(city_name["France"]["key3"]) """


## bid genater game
import art
print(art.logo)
def for_hight_biding(biding_dic):
    win = ""
    highBid = 0
    for bidders in biding_dic:
        amount = biding_dic[bidders]
        if amount > highBid:
            highBid = amount
            win = bidders
    print(f"The winer is  {win} with bid of ${highBid}")

bid ={}
should_continue = str(input("Are there any other Biding? Type 'yes' or  'no'. \n")).lower()

continue_biding = True
while continue_biding :
    name = str(input("Enter your name: \n"))
    price = int(input("Enter your price : \n"))
    bid[name] = price
    should_continue = str(input("Are there any other Biding? Type 'yes' or  'no'. \n")).lower()
    if should_continue == "no":
        continue_biding = False
        for_hight_biding(bid)





