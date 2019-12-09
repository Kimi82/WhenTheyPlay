import requests
from bs4 import BeautifulSoup
from bottle import hook, response, route, run, static_file, request
import json
import socket
import sqlite3

#These lines are needed for avoiding the "Access-Control-Allow-Origin" errors
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

#Note that the text on the route decorator is the name of the resource
# and the name of the function which answers the request could have any name
@route('/examplePage')
def exPage():
    return "<h1>This is an example of web page</h1><hr/><h2>Hope you enjoy it!</h2>"

#If you want to return a JSON you can use a common dict of Python,
# the conversion to JSON is automatically done by the framework
@route('/sampleJSON', method='GET')
def mySample():
    return { "first": "This is the first", "second": "the second one here", "third": "and finally the third one!" }

#If you have to send parameters, the right sintax is as calling the resoure
# with a kind of path, with the parameters separed with slash ( / ) and they
# MUST to be written inside the lesser/greater than signs  ( <parameter_name> )
@route('/dataQuery/<name>/<age>')
def myQuery(name,age):
    connection= sqlite3.connect("C:/folder/data.db")
    mycursor = connection.cursor()
    mycursor.execute("select * from client where name = ? and age= ?",(name, age))
    results = mycursor.fetchall()
    theQuery = []
    for tuple in results:
        theQuery.append({"name":tuple[0],"age":tuple[1]})
    return json.dumps(theQuery)

#If you want to send images in jpg format you can use this below
@route('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root="C:/folder/images", mimetype="image/jpg")

#To send a favicon to a webpage use this below
@route('/favicon.ico')
def favicon():
    return static_file('windowIcon.ico', root="C:/folder/images", mimetype="image/ico")

#And the MOST important line to set this program as a web service provider is this
run(host=socket.gethostname(), port=8000)



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

def loadData():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="product_information_title___2rG9M product_title gl-heading gl-heading--m").get_text()
    price = soup.find(class_="gl-price__value").get_text()
    print(title,price)

def getData():
    URL = input("Take me url of website:")
    return URL




#URL = getData()
#loadData()
