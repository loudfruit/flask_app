from flask import Flask, render_template, request
app = Flask(__name__)
import get_weather

# app.run(debug=True)

@app.route("/")
def index():
    name = request.values.get('name')
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    name = request.values.get('name')
    return render_template('about.html', name=name)

@app.route('/weather')
def weather():
    address = request.values.get('address')
    forecast = None
    if address:
        forecast = get_weather.weather(address)
    return render_template('weather.html', forecast=forecast)

if __name__ == "__main__":
    app.run()
