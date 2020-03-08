Pour faciliter l’accès des usagers à leur consommation / production d’électricité, SunShare réalise une box énergie libre à partir d’un mini-ordinateur  Raspberry Pi 3. En pratique le système reçoit les informations de 3 sources différentes (Linky, Onduleur, Compteur PV) 
	Le but de la carte à concevoir est d’adapter les signaux pour pouvoir les lire sur la carte RaspberryPi3, protéger électriquement le raspberry et de permettre un raccordement physique des câbles. La technologie à utiliser est à déterminer.


La méthodologie utilisée afin d’élaborer les spécifications de la carte électronique à réaliser est la méthode de conception de système électronique ou bien MCSE. Cette méthode intègre la compréhension des étapes de réalisation d’un circuit.
	Dans un premier temps, il est nécessaire d’exprimer les propriétés et contraintes du circuit d’un point de vue externe. La seconde démarche après la définition du besoin du client est celle des spécifications fonctionnelles et non fonctionnelles. Cette étape est un travail d’analyse détaillée. Afin de réaliser cette phase, on distingue trois étapes : analyse de l’environnement, définition des entrées/sorties du circuit et définition des spécifications.

	
# I. Spécification
## I.1 Analyse de l'environnement

En premier lieu, il est nécessaire de définir les entités qui interagissent avec le shield. Sachant que le ports de communication des onduleurs photovoltaïques ont de nombreux standard, la première étape est d’utiliser un capteur à impulsion pour contourner le problème. Soit le cahier des charges spécifie que le circuit communique avec trois entités : le raspberry avec son GPIO, le compteur à impulsion et le compteur Linky.

<p align="center"> <img width="400" alt="Diagramme" src="https://user-images.githubusercontent.com/61844088/76099790-f0224900-5fcb-11ea-98c5-f421bd21bcc6.png"> </p>

En ce qui concerne le compteur Linky, il possède une sortie de télé-information nommée TIC qui permet à n’importe quelle fournisseur de se plugger dessus pour visualiser les informations en temps-réels de celui-ci. 
Quant à la troisième entité, le shield devra adapter les signaux du compteur à impulsion et du compteur Linky pour les fournir au raspberry.
## I.2 Spécifications fonctionnelles

Les spécifications fonctionnelles permettre de spécifier (eh oui), décrire et préciser les fonctionnalités du circuit à concevoir. Dans le cas du shield Sunshare, il est nécessaire de comprendre comment fonctionne chaque entité afin de comprendre le type de données reçus pour pouvoir les adapter et les décoder par la suite.

### I.2.1 Fonctionnement GPIO raspberry

Le raspberry est un indispensable, il va permettre de décoder les informations reçus pour les visualiser ensuite. Il dispose de broches GPIO (General Purpose Input Output) que l’on traduirait par entrées/sorties.

<p align="center"> <img width="300" alt="Capture d’écran 2020-03-06 à 17 04 27" src="https://user-images.githubusercontent.com/61844088/76100298-b0a82c80-5fcc-11ea-9f67-547957f2ca7f.png"> </p>

Chaque broche peut avoir une utilisation précise, par exemple les broches 3 et 5 vont permettre de s’interfacer avec une bus I2C. Il fournit aussi des sources d’alimentation (3,3V ou 5V). De plus les broches du GPIO sont en 3,3V mais avec du 5V toléré.

### I.2.2 Fonctionnement TIC du compteur Linky

Le compteur Linky développé par Enedis, une filiale d’EDF, est un compteur électrique communicant déployé en 2015. Il permet au groupe Enedis de connaître la consommation instantanée de tous les compteurs et d’améliorer ainsi l’efficacité de son réseau.Il est composé de bornes I1 et I2 qui permettent de récupérer les données du TIC.

Enedis a mis à disposition un document de spécification détaillant les caractéristiques techniques et fonctionnelles des sorties de télé-information client des compteurs (https://www.enedis.fr/sites/default/files/Enedis-NOI-CPT_54E.pdf).
<p align="center"> <img width="168" alt="Capture d’écran 2020-03-06 à 17 14 38" src="https://user-images.githubusercontent.com/61844088/76101029-0204eb80-5fce-11ea-90d2-e70df60c30f8.png">
</p>

Le compteur est paramétrable en deux modes différents:<br><br>
	- <b>historique</b> : dans ce mode, le compteur Linky permet de restituer des trames d’information équivalentes à celles des anciens compteurs électroniques résidentiels, toutefois, pour obtenir les informations optimales dans ce mode d’information, la configuration tarifaire du compteur doit être réalisée dans la même logique des contrats historiques.<br><br>
	- <b>standard</b> : ce nouveau mode, est apparu avec les compteurs Linky. Il est plus rapide que le mode historique, et comporte des informations différentes, avec un formatage spécifique.
	
<br>Le compteur linky communique par défaut la TIC en mode HISTORIQUE, sans l’ensemble des paramètres. Pour passer en mode STANDARD, il faut contacter son fournisseur, qui informe ENEDIS (3j de délai chez ENEDIS).La trame de télé-information du mode standard est décrite dans le document fourni par Enedis paragraphe 6.2 (p17).
Le shield devra adapter les signaux du TIC et protéger électriquement le raspberry Pi 3.

### I.2.3 Fonctionnement du compteur à impulsion

La première phase consiste à utiliser un compteur à impulsion permettant de mesurer l’énergie produite par les panneaux photovoltaïques. Le compteur utilisé par Sunshare pour le moment est le Ketler 3201. Le branchement est donné ci-dessous (selon la fiche technique du produit).

<p align="center"> <img width="500" alt="Capture d’écran 2020-03-06 à 17 19 15" src="https://user-images.githubusercontent.com/61844088/76101386-a38c3d00-5fce-11ea-8efd-dc0bc5611fab.png">
</p>

Le shield devra se connecter aux entrées 20 et 21 afin de télé-relever le compteur. Les caractéristiques électriques et fonctionnelles de ces sorties ne sont pour le moment pas connu.

### I.2.4 Délimitation des entrées/sorties

En décrivant le fonctionnement de chaque entité, il est possible de réaliser une délimitation des entrées et sorties du shield à concevoir. Les données de télé-information décodées par le shield sont reliés directement à la liaison série du Raspberry.

<p align="center"><img width="300" alt="Capture d’écran 2020-03-06 à 17 22 57" src="https://user-images.githubusercontent.com/61844088/76101703-2614fc80-5fcf-11ea-818d-cdf3d8ff32a9.png">
</p>
La figure ci-dessus montre les relations mises en évidences lors des précédentes parties.

### I.2.5 Raffinement fonctionnel

Le raffinement fonctionnelle du shield montre les différentes fonctions dont il devra disposer. 

<p align="center"><img width="300" alt="Diagramme-Page-2" src="https://user-images.githubusercontent.com/61844088/76099799-f44e6680-5fcb-11ea-95e3-886d0e8e008f.png">
</p>

Il est aussi composé d’une alimentation qui provient directement du raspberry, celle-ci va permettre d’alimenter les composants actifs tels que les circuits.

## I.3 Spécifications opératoires & technologiques
<ul>
<li>        Raccordement des câbles par borniers à vis( ou autre solution simple pour un particulier).</li>
<li>         Doublage des entrées pour les compteurs à impulsions (6 borniers).</li>  
<li>          Le circuit doit être protégé et protéger le raspberry (suggestion d’utilisation d’optocoupleurs dans la documentation shield_polytech_v5)</li>
<li>         Laisser accessible les broches GPIO du raspberry non utilisées à disposition afin de pouvoir  raccorder une autre carte d’extension par-dessus (contacteurs pour délestage).</li>
	<li>          Coût unitaire de fabrication de la carte fini inférieur à 20€ </li>
</ul>


