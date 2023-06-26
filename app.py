from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'c270a102606f75062d3d88b2bd5b4d5d'  
        # Make a GET request to the OpenWeather API
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        data = response.json()

        if data['cod'] == '404':
            error_msg = 'Pilsēta nav atrasta. Lūdzu ievadi korektu pilsētas nosaukumu.'
            return render_template('weather.html', error_msg=error_msg)

        # Extract relevant weather information
        weather = {
            'city': data['name'],
            'temperature': round(data['main']['temp'] - 273.15, 2),
            'feels_like': round (data ['main']['feels_like']- 273.15, 2),
            'description': data['weather'][0]['description'],
            'winds_peed' : data["wind"]["speed"],
            'icon': data['weather'][0]['icon']
        }

        return render_template('weather.html', weather=weather)

    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)
