
De vegades els programadors necessiten esvair-se una mica 
després d'una intensa sessió de treball. En aquesta ocasió us presentem 
una activitat idònia per deixar descansar la ment mentre disfrutem d'un 
magnífic esport com és el basquet i que consisteix en enregistrar cada 
cistella d'un partit de la següent manera:

	- Primer s'indica si la cistella l'ha puntuat l'equip local o el visitant amb 
	una lletra (L o V)
	- A continuació s'indica el nombre de punts aconseguits per la cistella 
	(1, 2 o 3)

Després d’haver enregistrat totes les cistelles del partit d'avui, la nostra 
ment s'ha quedat tan relaxada que no hem copsat quin equip ha guanyat 
el partit. Per tal d'esbrinar-ho (i degut a que som una mica sadodevmassoquistes) desenvoluparem un programa per a que calculi el 
guanyador.

Entrada
L’entrada comença amb un número que indica el nombre de línies que 
venen a continuació. Cada línia reflexa el flux d’anotació de cistelles d’un 
partit, segons l’explicació anterior, on cada cistella es representa per un 
parell de valors, el primer per indicar quin equip anota (L o V) i el segon el 
valor de la cistella (1, 2 o 3).

Sortida
Com a sortida, per a cada cas de prova, s’escriurà, en una sola línia:
 L’equip guanyador del partit (L o V). Cas d’empat, escriurà E
 Els punts de l’equip local
 Els punts de l’equip visitant

Exemple d'execució 1:

ENTRADA
4
V
2
V
2
L
1
L
3

SALIDA
E 4 4

Exemple d'execució 2:

ENTRADA
5
L
2
V
3
V
2
V
1
V
1

SALIDA
V 2 7

