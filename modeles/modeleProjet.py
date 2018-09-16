#!/usr/bin/python
# -*- coding: utf-8 -*-


import mysql.connector

connexionBD = None

def getConnexionBD() :
	global connexionBD
	try :
		if connexionBD == None :
			connexionBD = mysql.connector.connect(
					host = 'localhost' ,
					user = 'root' ,
					password = 'azerty' ,
					database = 'Projet'
				)
		return connexionBD
	except :
		return None

def getAdherant() :
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
					select idAdherant, Email, mdp
					from Adherant
				'''

		curseur.execute( requete , () )
		enregistrements = curseur.fetchall()
		personnels = []
		for unEnregistrement in enregistrements :
			unPersonnel = {}
			unPersonnel[ 'idAdherant' ] = unEnregistrement[ 0 ]
			unPersonnel[ 'Email' ] = unEnregistrement[ 1 ]
			unPersonnel[ 'mdp' ] = unEnregistrement[ 2 ]
			unPersonnel[ 'benevole' ] = unEnregistrement[ 3 ]

			personnels.append( unPersonnel )
		curseur.close()

		return personnels
		
	except :
		return None
		
		
		
def login() :
	try :
		curseur = getConnexionBD.cursor()
		r
