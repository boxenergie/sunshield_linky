
Ce document rend compte des choix techniques utilisés afin de réaliser la carte Sunshield. Il est apparu dans les spécifications techniques 3 blocs à réaliser qui sont : l’alimentation du shield, le décodage de la TIC du compteur Linky ainsi que le décodage du compteur à impulsion.
	
# Décodage de la TIC du compteur Linky 

La TIC est composé de deux sorties I1 et I2. En observant le signal aux bornes de ces deux sorties, nous obtenons le chronogramme suivant : 

<p align="center"> <img width="400" alt="image" src="https://user-images.githubusercontent.com/39769580/76022283-1c37be80-5f27-11ea-87b9-9a302b3298c3.png"> </p>




Le signal obtenu est l’information de la TIC modulée, il est alors nécessaire de décoder cette trame pour quelle soit sous les caractéristiques exigées par le raspberry : 

- Pour un niveau logique 0, obtenir 0V 
- Un niveau logique 1, obtenir la tension d’alimentation 3,3V

On peut dès à présent remarquer que lorsqu’il y a des ondulations à fréquence élevé, cela correspond à un niveau logique. Au contraire, lorsque le signal décroît lentement cela correspond au niveau logique inverse. De plus, il est important de savoir que **le signal précédemment obtenu est inversé (voir doc Linky)**  et il est nécessaire de le renverser pour obtenir les informations correctes.

Pour démoduler le signal et isoler electriquement le raspberry du compteur le choix s’est porté sur un optocopleur comme présenté dans la solution du PitInfo (crédit: http://hallard.me/pitinfov12-light/).


## En sortie de l’optocoupleur

En sortie de l’optocoupleur nous obtenons l’oscillogramme suivant:

IMAGE


Le signal obtenu est bien carré mais il comporte beaucoup de bruit. Pour avoir le moins d’erreurs possibles lors de la lecture de la TIC par le raspberry, nous avons décidé d’utiliser un comparateur pour effectuer un seuillage. 

Le comparateur est composé de deux entrées, - et +. 

- Sur l’entrée +, nous mettons le seuil qui est le plus cohérent compte tenu des informations. Sachant que le signal a une amplitude d’environ **1,5V** sans les pics de tension, le seuil est fixé à la moitié soit **0,75V**. Pour cela un simple pont diviseur a été effectué (cf schéma).

IMAGE



- Sur l’entrée  - se trouvera le signal en sortie de l’émetteur. Ainsi avec cette disposition, notre info linky est bien inversée et est parfaitement exploitable compte tenue du signal carré propre comme on peut le voir ci-dessous.

<p align="center"> <img width="400" alt="image" src="https://user-images.githubusercontent.com/39769580/76022301-23f76300-5f27-11ea-8169-4b6f7e63b8d0.png"> </p>

# Décodage du compteur à impulsions



Le compteur à impulsions permet d’informer l’utilisateur sur l’énergie produite par ses panneaux solaires. La plupart de ces capteurs sont équipés d’écran LCD affichant l’énergie produite. Ils sont aussi équipés de deux sorties d’impulsions (impuls+, impuls-) produisant 1000 impulsions pour un kWh produit. Pour une impulsion du capteur, l’énergie produite par les panneaux est de 1Wh.

De ce fait, le but ici est de capter ces impulsions pour qu’elles puissent être traitées par le raspberry. Comme énoncé dans les spécifications, les impulsions de ces capteurs répondent à la norme  EN 62 053-31 (Tension 12-27V DC/ courant <27mA). Cela ne répondant pas aux critères électriques du GPIO, il faut adapter cette impulsion pour qu’elle soit comprise entre 0V et 3,3V. 

Le moyen le plus simple est d’ajouter une charge résistive avec une résistance de pull up. Le schéma se présente comme suit:

## test du compteur à impulsion

<p align="center"> <img width="400"  src="https://user-images.githubusercontent.com/39769580/76022320-2f4a8e80-5f27-11ea-80b0-5182b2699b8a.png"> </p>
