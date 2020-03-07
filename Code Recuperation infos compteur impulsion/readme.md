Le code intégral de la boxenergie est développé sous nodered et mis à disposition sur la page http://github.com/boxenergie.

Ces 2 codes python permettent d'intéragir avec les pins du raspberry qui sont ainsi en relation avec les borniers des compteurs à impulsions. 

Pour rappel : 

<p align="center"> <img width="400" alt="image" src="https://user-images.githubusercontent.com/39769580/76018951-41293300-5f21-11ea-9645-6601f511ff1f.png"> </p>

La première partie du code (ligne 1 à 17) importe les librairies nécessaires à l’acquisition du signal et initialise la variable d’itération i et la variable du nombre d’impulsions counter.  
Dans le programme principal (ligne 18 à 30), la première étape est d’attendre que le signal sur la broche du GPIO passe à l’état bas (ligne 20). Ensuite, la boucle (ligne 21 à 23) permet de vérifier que l’impulsion acquise en est bien une. En effet, lors des tests sur le compteur il s’est avéré qu’il y ai de fausses impulsions liées aux pics de courant. Pour résoudre ce problème, la boucle valide l’impulsion si l’impulsion fait au moins 10ms.
Ensuite, si l’impulsion est validée elle est affichée sur le terminal du Raspberry avec l’heure et la date (ligne 24 à 29).
