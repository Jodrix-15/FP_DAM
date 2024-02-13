#PRÁCTICA
##Descripción
L’hotel CalaGava necessita una aplicació per a poder gestionar les reserves de les 
seves habitacions i la gestió de les mateixes. 
De cada habitació s’ha de guardar el nº d’habitació (que és l’identificador), 
capacitat màxima (nº de persones que es poden allotjar), estat de l’habitació 
(disponible, bruta, ocupada) i el preu per dia. El número d’habitació no pot ser 
menor a 1.
Quan un client reserva una habitació, s’ha de registrar les següents dades del 
client: nom, cognom, dni i telèfon. 
L’aplicació ha de ser persistent. És a dir, les dades han de quedar guardades en 
fitxers de manera que quan es tanqui l’aplicació no es perdin totes les dades 
registrades i es puguin carregar a la següent execució. Les dades s’han de guardar 
a una carpeta anomenada dades. Dins ha d’haver dos fitxers, un amb les dades 
de les habitacions i un altre amb les dades de les reserves. S’ha de guardar amb 
el mateix format del dos fitxers d’exemple que s’adjunten amb l’enunciat d’aquesta 
pràctica.
Per comoditat d’execució de l’aplicació, el propietari de l’hotel demana que no hagi 
menú i l’aplicació funcioni per línia de comandes. És a dir, a l’executar-se l’script 
se li passarà un nom de comanda i els paràmetres necessaris per a executar-se. 
El programa farà les operacions corresponent i donarà el corresponent missatge 
de feedback a l’usuari, tant si tot va bé com si hi ha error. Es demana que els 
missatges d’error siguin clars i concisos.
