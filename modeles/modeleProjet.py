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
					select idAdherant, Email, mdp ,benevole
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
		
		
def seConnecter( email , mdp ) :
	try :
		curseur = getConnexionBD().cursor()
		
		requete = '''
				select idAdherant, Email, mdp ,benevole
				from Adherant
				where Email = %s
				and mdp = %s
				'''
		curseur.execute( requete , ( email , mdp ) )
		
		enregistrement = curseur.fetchone()
		Personnel = {}
		
		if enregistrement != None :
			Personnel[ 'idAdherant' ] = enregistrement[ 0 ]
			Personnel[ 'Email' ] = enregistrement[ 1 ]
			Personnel[ 'mdp' ] = enregistrement[ 2 ]
			Personnel[ 'benevole' ] = enregistrement[ 3 ]
		
		curseur.close()
		
		return Personnel
		
	except :
		return None
		
def livraisonLot() :
	try:
		curseur = getConnexionBD().cursor()
		
		requete = '''
				select idLot,Lot.idProduit,Produit.libelle,Produit.uniteMesure,Lot.idProducteur,Producteur.nom,Producteur.prenom,dateLivraison
				from Lot 
				inner join Produit 
				on Lot.idProduit = Produit.idProduit
				inner join Producteur
				on Lot.idProducteur = Producteur.idProducteur
				'''
		
		curseur.execute( requete , () )
		
		enregistrement = curseur.fetchall()
		Personnel = {}
		
		personnels = []
	
		for unEnregistrement in enregistrement :
			unPersonnel = {}
			unPersonnel[ 'idLot' ] = unEnregistrement[ 0 ]
			unPersonnel[ 'idProduit' ] = unEnregistrement[ 1 ]
			unPersonnel[ 'libelle' ] = unEnregistrement[ 2 ]
			unPersonnel[ 'uniteMesure' ] = unEnregistrement[ 3 ]
			unPersonnel[ 'idProducteur' ] = unEnregistrement[ 4 ]
			unPersonnel[ 'nom' ] = unEnregistrement[ 5 ]
			unPersonnel[ 'prenom' ] = unEnregistrement[ 6 ]
			unPersonnel[ 'dateLiv' ] = unEnregistrement[ 7 ]

			personnels.append( unPersonnel )
		
		curseur.close()
		
		return personnels
		
	except :
		return None
		
		
def getproducteur() :
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
				select idProducteur,nom,prenom
				from Producteur
			'''

		curseur.execute( requete , () )
		enregistrements = curseur.fetchall()
		personnels = []
		for unEnregistrement in enregistrements :
			unPersonnel = {}
			unPersonnel[ 'idProducteur' ] = unEnregistrement[ 0 ]
			unPersonnel[ 'nom' ] = unEnregistrement[ 1 ]
			unPersonnel[ 'prenom' ] = unEnregistrement[ 2 ]

			personnels.append( unPersonnel )
		curseur.close()

		return personnels
	
	except :
		return None
	
	
def getidProduit(libelle) :
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
					select idProduit,libelle,uniteMesure
					from Produit
					where libelle = %s
				'''
		curseur.execute( requete , (libelle, ) )
		enregistrement = curseur.fetchone()
		produit = {}
		if enregistrement != None :
			produit[ 'idProduit' ] = enregistrement[ 0 ]
			produit[ 'libelle' ] = enregistrement[ 1 ]
			produit[ 'uniteMesure' ] = enregistrement[ 2 ]
			
		
		curseur.close()
		return produit
		
	except :
		return None
		
		
		

def insertproduit(libelle,unMesure) :
	try:
		curseur = getConnexionBD().cursor()
		
		requete = '''
				insert into Produit(libelle,uniteMesure) values(%s,%s);
			
			'''
	
		curseur.execute( requete , (libelle,unMesure) )
		connexionBD.commit()
		nbTuplesTraites = curseur.rowcount
		curseur.close()

		return nbTuplesTraites
	
	except :
		
		return None

def insertLot(dateLivraison,idProduit,producteur) :
	try:
		curseur = getConnexionBD().cursor()
		
		requete = '''
				insert into Lot(dateLivraison,idProduit,idProducteur) values(%s,%s,%s);
			
			'''
		
		curseur.execute( requete , (dateLivraison,idProduit,producteur) )
		connexionBD.commit()
		nbTuplesTraites = curseur.rowcount
		curseur.close()

		return nbTuplesTraites
	
	except :
		
		return None
		
		
def deleteProducteur(nb) :
	try:
		curseur = getConnexionBD().cursor()
		
		requete = '''
				delete from Producteur where idProducteur = %s ;
				'''
				
		curseur.execute( requete , (nb,))
		connexionBD.commit()
		nbTuplesTraites = curseur.rowcount
		curseur.close()

		return nbTuplesTraites
	
	except :
		
		return None
		
def getProduitdeProducteur(nb) : 	
	try:
		curseur = getConnexionBD().cursor()
		
		requete = '''
				select idLot,Lot.idProduit,Produit.libelle,Produit.uniteMesure,Lot.idProducteur,Producteur.nom,Producteur.prenom,dateLivraison
				from Lot 
				inner join Produit 
				on Lot.idProduit = Produit.idProduit
				inner join Producteur
				on Lot.idProducteur = Producteur.idProducteur
				where Producteur.idProducteur = %s 
				'''
		
		curseur.execute( requete , (nb, ) )
		
		enregistrement = curseur.fetchall()
		Personnel = {}
		
		personnels = []
	
		for unEnregistrement in enregistrement :
			unPersonnel = {}
			unPersonnel[ 'idLot' ] = unEnregistrement[ 0 ]
			unPersonnel[ 'idProduit' ] = unEnregistrement[ 1 ]
			unPersonnel[ 'libelle' ] = unEnregistrement[ 2 ]
			unPersonnel[ 'uniteMesure' ] = unEnregistrement[ 3 ]
			unPersonnel[ 'idProducteur' ] = unEnregistrement[ 4 ]
			unPersonnel[ 'nom' ] = unEnregistrement[ 5 ]
			unPersonnel[ 'prenom' ] = unEnregistrement[ 6 ]
			unPersonnel[ 'dateLiv' ] = unEnregistrement[ 7 ]

			personnels.append( unPersonnel )
		
		curseur.close()
		
		return personnels
		
	except :
		return None
		
		
def modifierProducteur(nom,prenom,idProducteur):
	try:
		curseur = getConnexionBD().cursor()
		
		requete ='''
				update Producteur
				set nom = %s ,prenom = %s
				where idProducteur = %s
				'''
		curseur.execute( requete ,(nom,prenom,idProducteur))
		connexionBD.commit()
		nbTuplesTraites = curseur.rowcount
		curseur.close()

		return nbTuplesTraites
	
	except :
		
		return None
		
		

		
		
		


