# REQUESTS LIBRARY : HTTP for humans
# it's really good at getting information from websites
# but not good at PARSING THEM
# use beautifulsoup or Request-html

import requests

# r = requests.get("https://xkcd.com/353/")
# # returns the HTML of that page (unicode text) = SOURCE
# # print(r.text)
#
# # img = requests.get("https://imgs.xkcd.com/comics/python.png")
# # # this returns the bytes of an image
# # with open('comic.png', 'wb') as f:
# #     f.write(img.content)
#
#
# # HTTP Status
# # 200=success , 300=redirect , 400=client errors (no permission), 500=server errors
# print(r.status_code)
# # any response that is less than 400 (which is okay for us) = True
# print(r.ok)
# # return all the headers of the request
# # Example : the Server, content-type, ....
# print(r.headers)

# this add parameters as a dict to your url to prevent fails
# payload = {"page": 2, "count": 25}
# r = requests.get('https://httpbin.org/get', params=payload)
# # returns : https://httpbin.org/get?page=2&count=25
# print(r.url)

# POST DATA TO URL
# payload = {"username": "corey", "password": "testing"}
# r = requests.post('https://httpbin.org/post', data=payload)
# # print(r.text)
# """
# In the Json file
# "form": {
#     "password": "testing",
#     "username": "corey"
# }
# this is the data that we had set before in payload
# """
# # this creates a python dictionary from the JSON response
# # very convenient when working with json responses
# r_dict = r.json()
# print(r_dict['form'])

# PASSING AUTHENTIFICATION

# you need to add the correct username AND password in a tuple
# don't forget to set a timeour for every request (so that the script don't hang forever)
# you can also add delay (in seconds) in the URL /delay/1
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'), timeout=3)
print(r.text)
print(r) # RESPONSE 200
