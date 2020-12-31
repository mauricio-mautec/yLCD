#!/usr/bin/env python
"""
THIS IS THE MAIN ENTRY POINT FOR yLCD
CREATE YOUR APPS AND DISPATCH THEM USING THIS FILE
"""
from   flask                      import Flask, request, render_template
from   dsp.weather.displayweather import DisplayWeather
import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.debug = True # Make this False if you are no longer debugging
@app.route ('/', methods=['GET'])
def mainApp():
    cidade    = request.args.get ('cidade', 'GYN')
    display   = DisplayWeather()
    logging.debug('yLCD Request tipoDisplay: bulma' + ' cidade: ' + cidade)
    return main.renderDisplay('bulma', cidade)

@app.route ("/weather", methods=['GET'])
def weatherApp():
    tipoDisplay  = request.args.get ('tipo', 'main')
    codigo       = request.args.get ('codigo', 'GYN')
    logging.debug('yLCD Request tipoDisplay:' + tipoDisplay + ' codigo: ' + codigo)
    display      = DisplayWeather()
    return display.renderDisplay(tipoDisplay, codigo)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
