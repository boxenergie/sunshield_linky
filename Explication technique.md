
Ce document rend compte des choix techniques utilisés afin de réaliser la carte Sunshield. Il est apparu dans les spécifications techniques 3 blocs à réaliser qui sont : l’alimentation du shield, le décodage de la TIC du compteur Linky ainsi que le décodage du compteur à impulsion.
	
## Décodage de la TIC du compteur Linky 

la TIC est composé de deux sorties I1 et I2. En observant le signal aux bornes de ces deux sorties, nous obtenons le chronogramme suivant : 


IMAGE



Le signal obtenu est l’information de la TIC modulée, il est alors nécessaire de décoder cette trame pour quelle soit sous les caractéristiques exigées par le raspberry : 

- Pour un niveau logique 0, obtenir 0V 
- Un niveau logique 1, obtenir la tension d’alimentation 3,3V

On peut dès à présent remarquer que lorsqu’il y a des ondulations à fréquence élevé, cela correspond à un niveau logique. Au contraire, lorsque le signal décroît lentement cela correspond au niveau logique inverse. De plus, il est important de savoir que **le signal précédemment obtenu est inversé (voir doc Linky)**  et il est nécessaire de le renverser pour obtenir les informations correctes.

Pour demoduler le signal et isoler electriquement le raspberry du compteur le choix s’est porté sur un optocopleur comme présenté dans la solution du PitInfo (crédit: http://hallard.me/pitinfov12-light/).


## En sortie de l’optocoupleur

IMAGE
