
## Soudage des composants traversant sur le <a href="https://github.com/sunsharebox/sunshield_linky/tree/master/Fichiers%20Creation%20PCB" target="_blank" >PCB</a>

![Image description](https://user-images.githubusercontent.com/39769580/76102969-1e565780-5fd1-11ea-8ef2-b0dace72756c.png)

L'ensemble des composants utiles à la création de ce PCB sont référencés <a href="https://www.mouser.fr/ProjectManager/ProjectDetail.aspx?AccessID=4c69358422" target="_blank">ICI</a>

Afin d’avoir le moins de difficultés possibles, nous vous conseillons de souder les composants dans l’ordre suivant :
- Les résistances : R1, R2, R3, R4, R5, 56
- U4 (optocoupleur)
- U1 (Comparateur)
- Borniers à vis
- Header femmelle raspberry ATTENTION, ce composant se soude sur l'autre face (cf image ci-après)

Merci de se référer au <a href="https://easyeda.com/amguine1/sunshield_final_copy" target="_blank">Schéma</a> électronique pour souder les composants adéquats aux bons emplacements.
 

Après soudage des composants, la carte devrait se présenter comme suie : 


![2004C04D-BB02-4FB7-82B7-72F6062E4B26](https://user-images.githubusercontent.com/39769580/76019076-7897df80-5f21-11ea-9535-1b0dbdda3ec3.jpeg)

## Branchement du shield sur le raspberry
Le shield utilise les 12 premières broches du rasperry; 

![Image description](https://user-images.githubusercontent.com/39769580/76015897-328c4d00-5f1c-11ea-9de5-c1fc46b414e7.png)

Il suffit alors de la pluger sur les 6 premiers pin du raspberry, comme présenté ci-dessous; 

![image](https://user-images.githubusercontent.com/39769580/76018951-41293300-5f21-11ea-9645-6601f511ff1f.png)


ATTENTION à bien respecter la polarité pour les borniers des compteurs à impulsion

## Récupération de la TIC

Pour la TIC après avoir installé Picocom dans le terminal, il suffit d’entrer les commandes suivantes ; 

- **picocom -b 9600 -d 7 -p e -f n/dev/ttyS0**  Pour compteur en mode standard 
- **picocom -b 1200 -d 7 -p e -f n/dev/ttyS0**  Pour compteur en mode historique

Les résulats normalement attendus sont présenté ci-dessous; 

![image](https://user-images.githubusercontent.com/39769580/76019730-75e9ba00-5f22-11ea-980c-cfb8cacd7eb9.png)

On peut remarquer que les étiquettes des données restituées sont conforme à la documentation <a href="https://www.enedis.fr/sites/default/files/Enedis-NOI-CPT_54E.pdf" target="_blank" >ENEDIS</a> (page 18) 

![image](https://user-images.githubusercontent.com/39769580/76018539-7e40f580-5f20-11ea-8d4a-857c920ca5a5.png)


 ## Récupération des impulsions. 

 <a href="https://github.com/sunsharebox/sunshield_linky/tree/master/Code%20Recuperation%20infos%20compteur%20impulsion" target="_blank" >2 programmes</a> sont disponibles afin d’interagir soit avec le compteur correspondant à la pin 17 ou 4 du raspberry. 

Copier le programme sur le raspberry, se rendre sur le terminal dans le dossier où se trouvent les programmes. Lancer le programme avec la commande "

- **sudo python +NOM_PROGRAMME**

Voici le résultat attendu; 


![image](https://user-images.githubusercontent.com/39769580/76019459-0a075180-5f22-11ea-91ad-e65626841355.png)


_________________________________________________________________________________________________________________________
**Ce shield à été testé et fonctionne avec des compteurs LINKY de différentes marques qu'ils soient en mode historique ou standard**


*Pour toute question, écrire à <a href="mailto:contact@sunshare.fr/">contact@sunshare.fr</a>*



*Ce shield est sous la licence libre*

