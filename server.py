from flask import Flask, render_template, Response
import socket
import io

import pyfirmata
import time

#import pygame
#pygame.mixer.init()

board = pyfirmata.Arduino('/dev/ttyACM0')
servo = board.get_pin('d:5:s')

app = Flask(__name__)

@app.route('/')
def index():
    #return 'emergency drone control penal'
    return render_template("index.html",status="Statusanzeige")

@app.route('/open')
def open():
    #TODO greifer öffnen
    print("öffne greifer")
    #return 'greifer geöffnet'

    #servo.write() #TODO geöffneten wert eintragen
    
    return render_template("index.html",status="Greifer geöffnet")

@app.route('/close')
def close():
    #TODO greifer schliessen
    print("schliesse greifer")
    #return 'greifer geschlossen'

    #servo.write() #TODO geschlossenen wert eintragen

    return render_template("index.html",status="Greifer geschlossen")

#@app.route('/sound')
#def sound():
    #TODO greifer schliessen
    #print("spiele sound")
    #return 'greifer geschlossen'

    #servo.write() #TODO geschlossenen wert eintragen
    

    #pygame.mixer.music.load("rickroll.wav")
    #pygame.mixer.music.play()



    #return render_template("index.html",status="Sound abgespielt")

app.run(host='0.0.0.0', port=8081)

