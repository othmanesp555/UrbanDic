import json
import requests


#  User Input

print("Type a word to define")
word = input().title()

#  api script
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
querystring = {"term":word}
headers = {
	"X-RapidAPI-Key": "Your_RAPIDAPI_key",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)

#  parse json Data

u = response.json()
definition = u['list'][1]['definition']

#  Print result

print(definition)
