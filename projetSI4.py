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
	
@app.route( '/adherant/session/choisir' , methods = [ 'GET' ] )
def choisirSessionAdherant() :
	return render_template( 'AdherantConnexion.html' , echecConnexion = False , saisieIncomplete = False )


@app.route( '/adherant/connect/sucesser' , methods = [ 'GET' ] )
def adherantbenevole() :
	return render_template( 'open.html' )
	

@app.route( '/adherant/seConnecter' , methods = [ 'POST' ] )
def seConnecterAdherant() :
	email = request.form[ 'Email' ]
	mdp = request.form[ 'mdp' ]

	if email != '' and mdp != '' :
		adherant = modeleProjet.seConnecter( email , mdp )
		if len(adherant) != 0 :
			if adherant[ 'benevole' ] == True :
				return redirect( '/adherant/connect/sucesser' )
				
			else :
				return render_template('AdherantConnexion.html', benevole = True , echecConnexion = False , saisieIncomplete = False )
		else :
			return render_template('AdherantConnexion.html', benevole = False , echecConnexion = True , saisieIncomplete = False )
	else :
		return render_template('AdherantConnexion.html', benevole = False , echecConnexion = False , saisieIncomplete = True)

@app.route ( '/adherant/livraisons' , methods = [ 'GET' ] )
def livraison() :
	return render_template( 'livraison.html' )
	
@app.route ( '/adherant/producteur' , methods = [ 'GET' ] )
def producteur() :
	return render_template( 'producteur.html' )
	
@app.route ( '/adherant/livraisons/visualiser' , methods = [ 'GET' ] )
def visualiserLot() :
	lot = modeleProjet.livraisonLot()
	return render_template( 'visualiserLot.html' , lot = lot )
	
@app.route ( '/adherant/producteur/visualiser' , methods = [ 'GET' ] )
def visualiserProducteur() :
	producteur = modeleProjet.getproducteur()
	return render_template( 'visualiserProducteur.html' , producteur = producteur )
	
@app.route ( '/adherant/livraisons/Enregistrer' , methods = [ 'GET' ] )
def enregistrer() :
	producteur = modeleProjet.getproducteur()
	return render_template( 'enregistrerLot.html' , producteur = producteur)	
	
@app.route ( '/livraison/enregistrer/seEnregistre' , methods = [ 'POST'])
def seEnregistrerProduit():
	libelle = request.form[ 'libelle' ]
	unMesure = request.form[ 'UM' ]
	producteur = request.form[ 'producteur' ]
	dateLivraison = request.form[ 'dateLivraison' ]
	
	produitInsert = modeleProjet.insertproduit(libelle,unMesure)
	
	if produitInsert != None :
		idProduit = modeleProjet.getidProduit(libelle)
		lotInsert = modeleProjet.insertLot(dateLivraison,idProduit['idProduit'],producteur)
		lot = modeleProjet.livraisonLot()
		return render_template( 'visualiserLot.html' , lot = lot , enregistre = True , libelle = libelle )
	
	else :
		return redirect('/adherant/livraisons/Enregistrer' , probleme = True)
	

@app.route ('/adherant/producteur/visualiser/supprime/<nb>/<nom>' , methods =  [ 'POST' ] )
def supprimerProducteur(nb,nom):
	supprimeProducteur = modeleProjet.deleteProducteur(nb)
	producteur = modeleProjet.getproducteur()
	return render_template('visualiserProducteur.html', supprimer = True , nom=nom , producteur = producteur )


@app.route ('/adherant/producteur/visualiser/produit/<nb>/<nom>/<prenom>' , methods = ['POST'] )
def producteurDeProduit(nb,nom,prenom):
	lot = modeleProjet.getProduitdeProducteur(nb)
	return render_template('visualiserLesProduitsUnProducteur.html' , lot = lot , nom=nom , prenom=prenom)


	
@app.route ('/adherant/producteur/cree' , methods = ['GET'] )
def creeproducteur():
	return render_template('creeProducteur.html')
	
@app.route ('/producteur/cree/seEnregistre' , methods = ['POST'] )
def seEnregistrerProducteur():
	nom = request.form[ 'nom' ]
	prenom = request.form[ 'prenom' ]
	
	producteurInsert = modeleProjet.insertProducteur(nom,prenom)
	
	if producteurInsert != None :
		producteur = modeleProjet.getproducteur()
		return render_template( 'visualiserProducteur.html' , producteur = producteur , enregistre = True , nom = nom, prenom = prenom )
	
	else :
		return redirect('/producteur/cree/seEnregistre' , probleme = True)

@app.route ('/adherant/producteur/visualiser/modifier/<nb>/<nom>/<prenom>' , methods = ['POST'] )
def modifierProducteur(nb,nom,prenom):
	return render_template('producteurModifier.html' , nb = nb, nom = nom , prenom = prenom )	
	
	
@app.route ('/adherant/producteur/visualiser/modifier/seEnregistre/<nb>' , methods = ['POST'] )
def enregistrerModification(nb):
	nom = request.form[ 'nom' ]
	prenom = request.form[ 'prenom' ]
	
	if len(nom) == 0 and len(prenom) == 0:
		return redirect('/adherant/producteur/visualiser')
	
	else:
		producteurmodifier = modeleProjet.modifierProducteur(nom,prenom,nb)
		if producteurmodifier != None :
			producteur = modeleProjet.getproducteur()
			return render_template( 'visualiserProducteur.html' , producteur = producteur , enregistre = True , nom = nom, prenom = prenom )
		
		else :
			return redirect('/adherant/producteur/visualiser/modifier/<nb>/<nom>/<prenom>' , probleme = True)


if __name__ == '__main__' :
	app.run( debug = True , host = '0.0.0.0' , port = 5000 )

