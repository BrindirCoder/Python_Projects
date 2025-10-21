import requests

url = input("Enter Image URL: ")
r = requests.get(url)
x = url.split("/")[-1]  #// Splite The Link and Return The Name of Image 

with open(x, "wb") as file:
    file.write(r.content)   
