import locale
import pickle

from operator import itemgetter

from textblob import TextBlob
from flask_basicauth import BasicAuth
from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

LR = pickle.load(open('models/house-pricing-lr.sav', 'rb'))

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'lemsantos'
app.config['BASIC_AUTH_PASSWORD'] = '9Z1&2VZwK6wS'

auth = BasicAuth(app)


@app.route('/')
def home():
    return 'Não é minha primeira API'


@app.route('/sentiment/<phrase>')
@auth.required
def sentiment(phrase):
    tb = TextBlob(phrase).translate(from_lang='pt', to='en')
    polarity = tb.sentiment.polarity

    return f'frase: {phrase}<br>polaridade: {polarity}'


@app.route('/quotation', methods=['POST'])
@auth.required
def quotation():
    payload = request.get_json()
    size, year, garage = itemgetter('size', 'year', 'garage')(payload)

    price = LR.predict([[size, year, garage]])[0]
    price_fancy = locale.currency(price, grouping=True, symbol=None)

    return jsonify({
        'price': price,
        'price_fancy': f'R$ {price_fancy}'
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
