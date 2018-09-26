#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *
from modeles import modeleProjet
import requests

libelle ="gun"
unMesure = 254
producteur = 3
dateLivraison = '2018-09-29'


produit = modeleProjet.getidProduit(libelle)
print produit

lot = modeleProjet.insertLot(dateLivraison,produit['idProduit'],producteur)
print lot





