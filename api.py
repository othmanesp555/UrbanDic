import json
import requests


#  User Input

print("Type a word to define")
word = input().title()

#  api script
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
querystring = {"term":word}
headers = {
	"X-RapidAPI-Key": "4363fa37femsh1b5f75f95103855p143fb5jsn1a185a1dc488",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)

#  parse json Data

u = response.json()
definition = u['list'][1]['definition']

#  Print result

print(definition)