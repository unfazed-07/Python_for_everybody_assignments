import json
data='''{
"name":"Divyansh",
"phone":{
"type":"intl",
"number":"+91 7876825980"
},
"email":{
"hide":"yes"
}
}'''

info=json.loads(data)
print('Name:', info['name'])
print('Hide:', info["email"]["hide"])