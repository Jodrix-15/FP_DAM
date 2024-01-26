 Implementa un menu que tindrà 4 opcions
 	A - posar un numero inicial (entre el 0 i el 10), que l'usuari introduirà per 
	teclat
	B - posar un numero final (entre el 0 i el 10), que l'usuari introduirà per 
	teclat
 	C - imprimir una compta entre el numero inicial i el final, amb un nombre 
	per línea, incloent els dos. Si l'usuari no ha posat numero inicial o final, 
	escriure ERROR. si el numero final es mes petit que l'inicial, escriure ERROR
	 D - sortir del programa. En aquest cas, el programa dira "BYE" i acabara 
	l'execució
	No posis cap altre print més enllà dels necessaris en el punt C i D.

Entrada
Cada cas són una combinació d'instruccions de l'usuari, que s'assegura que 
acaben en D. L'usuari és intel·ligent, i sempre posarà els seus números 
entre 0 i 10, i posarà números quan li toca posar números i lletres quan li 
toca posar lletres.

Sortida
La sortida del programa.

Exemple entrada 1:
A
4
C
B
6
C
D

Exemple sortida 1:
ERROR
4
5
6
BYE

Explicació Exemple 1: L'usuari posa A i introdueix nombre inicial. Aleshores 
posa C i dona error perquè no hi ha número final. Posa B i un numero final, 
C que imprimeix correctament de 4 a 6, i D per marxar.

Exemple entrada 2:
A
4
B
3
C
B
4
C
C
B
5
C
D

Exemple sortida 2:
ERROR
4
4
4
5
BYE

Explicació Exemple 2: 
L'usuari posa A i introdueix nombre inicial. Després B i posa nombre final. 
Aleshores posa C i dona error perquè final es més petit que inicial. Posa B i 
un numero final, que és el mateix que inicial. Per això les dues vegades que 
indica C imprimeix només 4. Després posa un numero final 5, compta de 4 
a 5, i marxa
