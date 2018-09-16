#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *
from modeles import modeleProjet
import requests

app = Flask( __name__ )


@app.route( '/' , methods = [ 'GET' ] )
def index() :
	Adherant = modeleProjet.getAdherant()
	return render_template( 'index.html', Adherant = Adherant )


if __name__ == '__main__' :
	app.run( debug = True , host = '0.0.0.0' , port = 5000 )

