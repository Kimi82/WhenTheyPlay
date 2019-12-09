import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

@app.route('/test')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')





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
