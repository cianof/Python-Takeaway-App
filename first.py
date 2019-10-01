from lxml import html
import requests


print("Enter Your Location: \n")
a = input()

if a == "Dublin":
    print("You're eating Domino's tonight buddy")

page = requests.get('https://www.apache.ie/order/pizza')
tree = html.fromstring(page.content)


menu = tree.xpath('//div[@title="buyer-name"]/text()')
print("What would you like to order? \nChoose from: ")
print("menu", menu)


b = input()

if b == "Moe Tell":
    print("sorry bud, sold out")