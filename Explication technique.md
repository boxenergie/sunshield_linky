
	Ce document rend compte des choix techniques utilisés afin de réaliser la carte Sunshield. Il est apparu dans les spécifications techniques 3 blocs à réaliser qui sont : l’alimentation du shield, le décodage de la TIC du compteur Linky ainsi que le décodage du compteur à impulsion.
	
# Décodage de la TIC du compteur Linky 

la TIC est composé de deux sorties I1 et I2. En observant le signal aux bornes de ces deux sorties, nous obtenons le chronogramme suivant : 


IMAGE



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


IMAGE

# Décodage du compteur à impulsions

