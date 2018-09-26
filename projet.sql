drop database if exists Projet ;
create database Projet;

use Projet;



create table Adherant(idAdherant int unsigned not null auto_increment,
Email varchar(30) not null ,
mdp varchar (10) not null,
benevole bool,
constraint pk_ad primary key (idAdherant));

create table Facture(numFacture int(5) not null auto_increment, 
dateHeure date,
idAdherant int unsigned,
constraint pk_fact primary key(numFacture),
constraint fk_ad foreign key (idAdherant) references Adherant(idAdherant));

create table Producteur(idProducteur int unsigned not null auto_increment,
nom varchar(20),
prenom varchar(20),
constraint pk_Prod primary key(idProducteur));

create table Produit(idProduit int unsigned not null auto_increment,
libelle varchar(20),
uniteMesure numeric(10.2),
constraint pk_Produit primary key(idProduit));

create table Lot(idLot int unsigned not null auto_increment,
dateLivraison date,
idProduit int unsigned,
idProducteur int unsigned,
constraint pk_Lot primary key(idLot),
constraint fk_Lot2 foreign key(idProducteur) references Producteur (idProducteur),
constraint fk_Lot3 foreign key(idProduit) references Produit (idProduit));

create table Ligne(numLigne int unsigned not null auto_increment,
prixvente numeric(5.2),
quantite numeric(10),
numFacture int(5),
idProduit int unsigned,
idLot int unsigned,
constraint pk_Lig primary key(numLigne),
constraint fk_Lig1 foreign key(numFacture) references Facture (numFacture),
constraint fk_Lig2 foreign key(idProduit) references Produit (idProduit),
constraint fk_Lig3 foreign key(idLot) references Lot (idLot));

create table Couter(idProduit int unsigned,
dateTarif date,
prix numeric(5.2),
constraint fk_Couter foreign key(idProduit) references Produit(idProduit));



insert into Adherant(Email,mdp,benevole) values("nitharsan21@gmail.com","2109nith",true);
insert into Adherant(Email,mdp,benevole) values("paul45@gmail.com","azerty",false);
insert into Adherant(Email,mdp,benevole) values("ninjapanda94@gmail.com","7e8455d5z",false);
insert into Adherant(Email,mdp,benevole) values("dragonkignt78@gmail.com","4d4z4dz88",false);
insert into Adherant(Email,mdp,benevole) values("villan99@gmail.com","kl5ihu2k",false);
insert into Adherant(Email,mdp,benevole) values("hellfire5455@gmail.com","azerty",false);
insert into Adherant(Email,mdp,benevole) values("lusifer2109@gmail.com","21091998",true);
insert into Adherant(Email,mdp,benevole) values("siolla@gmail.com","azerty",true);


insert into Producteur(nom,prenom) values("MICKEl","Jackson");
insert into Producteur(nom,prenom) values("JACKIE","Chan");
insert into Producteur(nom,prenom) values("HARRY","Potter");
insert into Producteur(nom,prenom) values("WALT","Disney");
insert into Producteur(nom,prenom) values("DARK","Rider");

insert into Produit(libelle,uniteMesure) values("sniper",52);
insert into Produit(libelle,uniteMesure) values("teddy",42);
insert into Produit(libelle,uniteMesure) values("candy",14);
insert into Produit(libelle,uniteMesure) values("space ship",15);
insert into Produit(libelle,uniteMesure) values("sword",42);


insert into Lot(dateLivraison,idProduit,idProducteur) values("2018-09-21",1,3);
insert into Lot(dateLivraison,idProduit,idProducteur) values("2018-10-11",2,4);
insert into Lot(dateLivraison,idProduit,idProducteur) values("2018-11-15",3,2);
insert into Lot(dateLivraison,idProduit,idProducteur) values("2018-12-25",4,5);

