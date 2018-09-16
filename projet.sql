drop database if exists Projet ;
create database Projet;

use Projet;



create table Adherant(idAdherant numeric(5) not null,
Email varchar(30) not null ,
mdp varchar (10) not null,
benevole bool,
constraint pk_ad primary key (idAdherant));

create table Facture(numFacture numeric(10) not null, 
dateHeure date,
idAdherant numeric(10),
constraint pk_fact primary key(numFacture),
constraint fk_ad foreign key (idAdherant) references Adherant (idAdherant));

create table Producteur(idProducteur numeric(10) unique,
nom varchar(20),
prenom varchar(20),
constraint pk_Prod primary key(idProducteur));

create table Produit(idProduit numeric(10) unique,
libelle varchar(20),
uniteMesure numeric(10.2),
constraint pk_Produit primary key(idProduit));

create table Lot(idLot numeric(10) unique,
dateLivraison date,
idProduit numeric(10),
idProducteur numeric(10),
constraint pk_Lot primary key(idLot),
constraint fk_Lot2 foreign key(idProducteur) references Producteur (idProducteur),
constraint fk_Lot3 foreign key(idProduit) references Produit (idProduit));

create table Ligne(numLigne numeric(10) unique,
prixvente numeric(5.2),
quantite numeric(10),
numFacture numeric(10),
idProduit numeric(10),
idLot numeric(10),
constraint pk_Lig primary key(numLigne),
constraint fk_Lig1 foreign key(numFacture) references Facture (numFacture),
constraint fk_Lig2 foreign key(idProduit) references Produit (idProduit),
constraint fk_Lig3 foreign key(idLot) references Lot (idLot));

create table Couter(idProduit numeric(10),
dateTarif date,
prix numeric(5.2),
constraint fk_Couter foreign key(idProduit) references Produit(idProduit));



insert into Adherant values(1,"nitharsan21@gmail.com","2109nith",true);
insert into Adherant values(2,"paul45@gmail.com","azerty",false);
insert into Adherant values(3,"ninjapanda94@gmail.com","7e8455d5z",false);
insert into Adherant values(4,"dragonkignt78@gmail.com","4d4z4dz88",false);
insert into Adherant values(5,"villan99@gmail.com","kl5ihu2k",false);
insert into Adherant values(6,"hellfire5455@gmail.com","azerty",false);
insert into Adherant values(7,"lusifer2109@gmail.com","21091998",true);
insert into Adherant values(8,"siolla@gmail.com","azerty",true);



