Users = {
    "id" :1,
    "name":"Leanne Graham",
    "Username":"Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
print(Users)
print(Users["id"])
print(Users["name"])
print(Users["Username"])
print(Users["email"])
print(Users["address"]["street"])
print(Users["address"]["geo"]["lat"])

print(Users)
print(type(Users))
print("\nUbah dict ke json")
import json
result = json .dumps(Users)
print(type(result))
print(result)

with open('result.json', 'w' ) as file:
    json.dump(Users, file)
