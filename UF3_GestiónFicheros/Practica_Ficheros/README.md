# PRÁCTICA DE FICHEROS

## Descripción

L’hotel CalaGava necessita una aplicació per a poder gestionar les reserves de les 
seves habitacions i la gestió de les mateixes. <br><br>
De cada habitació s’ha de guardar el nº d’habitació (que és l’identificador), 
capacitat màxima (nº de persones que es poden allotjar), estat de l’habitació 
(disponible, bruta, ocupada) i el preu per dia. El número d’habitació no pot ser 
menor a 1.<br><br>
Quan un client reserva una habitació, s’ha de registrar les següents dades del 
client: nom, cognom, dni i telèfon. <br><br>
L’aplicació ha de ser persistent. És a dir, les dades han de quedar guardades en 
fitxers de manera que quan es tanqui l’aplicació no es perdin totes les dades 
registrades i es puguin carregar a la següent execució. Les dades s’han de guardar 
a una carpeta anomenada dades. Dins ha d’haver dos fitxers, un amb les dades 
de les habitacions i un altre amb les dades de les reserves. S’ha de guardar amb 
el mateix format del dos fitxers d’exemple que s’adjunten amb l’enunciat d’aquesta 
pràctica.<br><br>
Per comoditat d’execució de l’aplicació, el propietari de l’hotel demana que no hagi 
menú i l’aplicació funcioni per línia de comandes. És a dir, a l’executar-se l’script 
se li passarà un nom de comanda i els paràmetres necessaris per a executar-se. 
El programa farà les operacions corresponent i donarà el corresponent missatge 
de feedback a l’usuari, tant si tot va bé com si hi ha error. Es demana que els 
missatges d’error siguin clars i concisos.

## COMANDOS
### a) afegir habitacio num capacitat preu
On num és el número d’habitació. La capacitat és el nº de persones màxim que 
caben i el preu és el preu en € per dia de l’habitació. Per defecte quan es registra 
una habitació el seu estat és disponible. Si tot ha anat bé, es registrarà l’habitació 
i es guardarà les dades de l’habitació en el fitxer habitacions.txt amb totes les 
dades de l’habitació separades per ‘,’.

### b) afegir reserva habitacio nom cognom dni telefon
Si l’habitació existeix i està disponible quedarà reservada i es registraran les dades 
del client. S’haurà de donar feedback a l’usuari sobre el resultat de l’execució de 
la comanda. El dni ha de tenir longitud 9 i el telèfon a més de la longitud no pot 
tenir cap caràcter que no sigui numèric.

### c) finalitzar habitacio num_dies
Quan un client deixa l’hotel es finalitza la serva reserva. S’ha d’indicar el nº 
d’habitació i la quantitat de dies que ha tingut la reserva. L’aplicació calcularà el 
preu total que ha de pagar el client mostrant-lo i deixarà l’habitació en estat 
“BRUTA”. Cal que el servei de la neteja arregli l’habitació abans de que torni a 
estar disponible per a un altre client. Si el nº de dies és 0, s’anul·larà la reserva 
sense cost i l’habitació passarà a estar neta ja que el client no ha arribat a fer-la 
servir. S’entén que el client vol canviar la reserva o que el recepcionista ha comés 
alguna errada.

### d) netejar habitacio
Si la habitació estava BRUTA quedarà disponible per a un client. S’ha de 
comprovar i informar, com sempre, de tots els possibles errors

### e) list
Mostrarà tota la informació de totes les habitacions de l’hotel de la següent 
manera:

```
===============        INFO HOTEL        ===============
HAB		CAP		ESTADO
--------------------------------------------------------
104		4		OCUPADA		=> Cliente: Cabra Loca
105		2		DISPONIBLE	
========================================================
Total habitaciones: 2
Disponibles: 1	Ocupadas: 1	Sucias: 0
-------------------------------------------------------

```

### f) info dni
Mostrarà l’habitació (o habitacions) que tingui reservada el client indicat, si 
és que té alguna reserva. 
En cas contrari mostrarà un missatge indicant que l’hotel no té cap reserva 
amb el dni indicat. 
La informació s’ha de mostrar de la següent manera
```
Datos del Cliente:	Loca , Cabra - Tfn: 123456789
Habitación:  104
```

### g) reserves
Mostrarà tota la informació de les reserves de l’hotel de la següent manera:
```
===========      RESERVAS      ===========
104 : 12345678Z - Cabra Loca - 123456789
==========================================
```


