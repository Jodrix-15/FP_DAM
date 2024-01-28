# Exercici 1

Crea un fitxer anomenat user.py. Has d’afegir les següents funcions:

### a) demanarEdat
aquesta funció ha de demanar a l’usuari una edat i ha de
validar que sigui correcte. L’edat ha d’estar entre 0 i 130 anys. Si el
número no és correcte tornarà a demanar l’edat fins que sigui correcte.
Retorna el valor de l’edat.

### b) validarUsuari
La funció rep dos paràmetres, usuari i clau i ha de validar
que siguin correctes. Un usuari és correcte si té almenys 4 caràcters i la
clau és correcte si té 6 caràcters i té al menys una vocal. Retorna un
booleà indicant si l’usuari i la clau compleix el requisit.

### c) demanarNaixament
aquesta funció ha de demanar a l’usuari la data de
naixement demanant tres dades:
- dia: ha de ser un número entre 1 i 31.
- mes: ha de ser un número entre 1 i 12.
- any: ha de ser un número entre 1900 i 2021.
La funció retornarà una cadena amb el format “dia/mes/any”. Per
simplificar només es faran les comprovacions que indica l’enunciat.
d) login: La funció rep una diccionari amb dades d’usuaris, un usuari i una
clau. Retorna un booleà que indica si l’usuari i la clau passada correspon a
un usuari del diccionari.

# Exercici 2

Crea un fitxer anomenat dates.py. Has d’afegir les següents funcions:
### a) avui
aquesta funció ha de retornar una cadena amb la data d’avui amb el
següent format:
### b) properAniversari
aquesta funció rep la data de naixement en una cadena
amb format “dia/mes/any” i retorna la data del proper aniversari.
### c) quantFalta
aquesta funció rep una data, del futur, i ha de retornar quants
dies falten per a que arribi la data.
### d) aniversari
aquesta funció rep una cadena amb format “dia/mes/any” i ha
de retornar un booleà indicant si el mes que s’ha donat com argument
coincideix amb el mes actual.

# Exercici 3

Crea un fitxer anomenat main.py, que serà el programa principal. Aquest fitxer
farà servir les funcions dels mòduls que heu creat en els exercicis anteriors, així
que els haureu d’importar.
L’aplicació a l’iniciar ha de mostrar el següent menú:
1. Registrar usuari
2. Login
3. Mostrar dades d’un usuari
4. Sortir
El menú es mostrarà cada cop que s’acabi el codi de l’opció escollida per l’usuari
fins que l’usuari indiqui l’opció de sortir. En cas de que l’usuari demani una
opció que no està al menú s’haurà de mostrar el missatge “Opció incorrecta” i
es tornarà a mostrar el menú.
1. Registrar usuari: demanarà a les següents dades:
Usuari i paraula de pas. S’haurà de validar que són correctes fent servir la
funció corresponent de l’exercici 1. A més s’haurà de validar que no hi ha
registrat un usuari amb el mateix nom d’usuari.
Edat: demanarà una edat tal fent servir el codi que ja heu fet anteriorment.
Data de naixement: demanarà la data de naixement de l’usuari validant que és
correcte.
Un cop totes les dades siguin correctes es guardaran a un diccionari i es donarà
el missatge “Usuari registrat”
2. Login: es demanarà usuari i clau i si és correcte s’indicarà el següent
missatge:
Segons les dades de l’usuari.
Si no és correcte s’indicarà: “Usuari o paraula de pas incorrectes”.
3. Mostrar dades d’un usuari: Demanarà el nom d’un usuari i, si existeix,
mostrarà totes les seves dades (excepte la clau, és clar!). Si no existeix donarà
el corresponent missatge d’error.
