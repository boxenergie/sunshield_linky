Pour faciliter l’accès des usagers à leur consommation / production d’électricité, SunShare réalise une box énergie libre à partir d’un mini-ordinateur  Raspberry Pi 3. En pratique le système reçoit les informations de 3 sources différentes (Linky, Onduleur, Compteur PV) 
	Le but de la carte à concevoir est d’adapter les signaux pour pouvoir les lire sur la carte RaspberryPi3, protéger électriquement le raspberry et de permettre un raccordement physique des câbles. La technologie à utiliser est à déterminer.


La méthodologie utilisée afin d’élaborer les spécifications de la carte électronique à réaliser est la méthode de conception de système électronique ou bien MCSE. Cette méthode intègre la compréhension des étapes de réalisation d’un circuit.
	Dans un premier temps, il est nécessaire d’exprimer les propriétés et contraintes du circuit d’un point de vue externe. La seconde démarche après la définition du besoin du client est celle des spécifications fonctionnelles et non fonctionnelles. Cette étape est un travail d’analyse détaillée. Afin de réaliser cette phase, on distingue trois étapes : analyse de l’environnement, définition des entrées/sorties du circuit et définition des spécifications.

	
# Spécification
## Analyse de l'environnement

En premier lieu, il est nécessaire de définir les entités qui interagissent avec le shield. Sachant que le ports de communication des onduleurs photovoltaïques ont de nombreux standard, la première étape est d’utiliser un capteur à impulsion pour contourner le problème. Soit le cahier des charges spécifie que le circuit communique avec trois entités : le raspberry avec son GPIO, le compteur à impulsion et le compteur Linky.


