
## Soudage des composants traversant sur le <a href="https://github.com/sunsharebox/sunshield_linky/tree/master/Fichiers%20Creation%20PCB" target="_blank" >PCB</a>

<p align="center"> <img width="400" alt="Diagramme" src="https://user-images.githubusercontent.com/39769580/76102969-1e565780-5fd1-11ea-8ef2-b0dace72756c.png"> </p>

L'ensemble des composants utiles à la création de ce PCB sont référencés <a href="https://www.mouser.fr/ProjectManager/ProjectDetail.aspx?AccessID=4c69358422" target="_blank">ICI</a>

Afin d’avoir le moins de difficultés possible, nous vous conseillons de souder les composants dans l’ordre suivant :
- Les résistances : R1, R2, R3, R4, R5, R6
- U4 (optocoupleur)
- U1 (Comparateur)
- Borniers à vis
- Header femmelle raspberry **ATTENTION : ce composant se soude sur l'autre face (cf image ci-après)**

Merci de se référer au <a href="https://easyeda.com/amguine1/sunshield_final_copy" target="_blank">Schéma</a> électronique pour souder les composants adéquats aux bons emplacements.
 

Après soudage des composants, la carte devrait se présenter comme suit : 

<p align="center"> <img width="400" alt="Diagramme" src="https://user-images.githubusercontent.com/39769580/76019076-7897df80-5f21-11ea-9535-1b0dbdda3ec3.jpeg"> </p>


## Branchement du shield sur le raspberry
Le shield utilise les 12 premières broches du rasperry; 

<p align="center"> <img width="400" alt="Diagramme" src="https://user-images.githubusercontent.com/39769580/76015897-328c4d00-5f1c-11ea-9de5-c1fc46b414e7.png"> </p>

Il suffit alors de la brancher sur les 6 premiers pin du raspberry, comme présenté ci-dessous; 

<p align="center"> <img width="400" alt="Diagramme" src="https://user-images.githubusercontent.com/39769580/76018951-41293300-5f21-11ea-9645-6601f511ff1f.png"> </p>

ATTENTION à bien respecter la polarité pour les borniers des compteurs à impulsions

**Vous devez activer le port série UART sur le raspberry pi 3 :**
<code> sudo raspi-config </code>
et Interfacing Options / Serial
 “Would you like a login shell to be accessible over serial?” Choisir **NO**
 “Would you like the serial port hardware to be enabled?” Choisir **YES**
 
 ***important** : note à propos du bluetooth et du port série du raspberry pi :
 https://www.framboise314.fr/le-port-serie-du-raspberry-pi-3-pas-simple/
 
 
## Récupération de la TIC

Pour information, le bornier correspondant à la TIC est physiquement routé sur la broche 8 du raspberry (UART0 TX).

Pour récuperer l'information de la TIC, après avoir installé Picocom dans le terminal, il suffit d’entrer les commandes suivantes ; 

- `picocom -b 9600 -d 7 -p e -f n /dev/ttyS0`  Pour compteur en mode standard 
- `picocom -b 1200 -d 7 -p e -f n /dev/ttyS0`  Pour compteur en mode historique

Les résulats normalement attendus sont présentés ci-dessous; 

<p align="center"> <img width="400" alt="Diagramme" src="https://user-images.githubusercontent.com/39769580/76019730-75e9ba00-5f22-11ea-980c-cfb8cacd7eb9.png"> </p>

On peut remarquer que les étiquettes des données restituées sont conformes à la documentation <a href="https://www.enedis.fr/sites/default/files/Enedis-NOI-CPT_54E.pdf" target="_blank" >ENEDIS</a> (page 18) 

<p align="center"> <img width="400" alt="Diagramme" src="https://user-images.githubusercontent.com/39769580/76018539-7e40f580-5f20-11ea-8d4a-857c920ca5a5.png"> </p>

 ## Récupération des impulsions. 

 <a href="https://github.com/sunsharebox/sunshield_linky/tree/master/Code%20Recuperation%20infos%20compteur%20impulsion" target="_blank" >1 programme</a> est disponible afin d’interagir avec les compteurs à impulsions branchés sur le shield.
 
Copier le programme sur le raspberry, se rendre sur le terminal dans le dossier où se trouve le programme. Lancer le programme avec la commande :

```bash
sudo python gpio-counterPort.py NUMERO_PIN
# avec NUMERO_PIN = 4 ou 17 selon le bornier du shield utilisé
```

Pour rappel : 

<p align="center"> <img width="400" alt="image" src="https://user-images.githubusercontent.com/39769580/76018951-41293300-5f21-11ea-9645-6601f511ff1f.png"> </p>


Ainsi pour récupérer l'information du compteur à impulsion 1 il suffit de lancer le programme avec la commande :

```bash
sudo python gpio-counterPort.py NUMERO_PIN
# avec NUMERO_PIN = 17 
```

De même pour le compteur à impulsion 2 : 

```bash
sudo python gpio-counterPort.py NUMERO_PIN
# avec NUMERO_PIN = 4 
```

Voici le résultat attendu :

<p align="center"> <img width="400" alt="Diagramme" src="https://user-images.githubusercontent.com/39769580/76019459-0a075180-5f22-11ea-91ad-e65626841355.png"> </p>

_________________________________________________________________________________________________________________________
**Ce shield à été testé et fonctionne avec des compteurs LINKY de différentes marques qu'ils soient en mode historique ou standard**


*Pour toute question, écrire à <a href="mailto:boxenergie@sunshare.fr/">boxenergie@sunshare.fr</a>*



*Ce shield est sous la licence libre openhardware LGPL*

