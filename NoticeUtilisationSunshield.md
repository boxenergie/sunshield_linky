
## Soudage des composants traversant sur le PCB

Afin d’avoir le moins de difficultés possible nous vous conseillons de souder les composants dans l’ordre suivant :
- Les résistances : R1, R2, R3, R4, R5, 56
- U4 (optocoupleur)
- U1 (Comparateur)
- Borniers à vis
- Header femmelle raspberry

Après soudage des composants, la carte devrait se présenter comme suit : 

![Image description](https://user-images.githubusercontent.com/39769580/76011441-e2f65300-5f14-11ea-81f8-4a562ae1b018.jpeg)

## Branchement du shield sur le raspberry
Le shield utilise les 12 premieres broches du rasperry; 

![Image description](https://user-images.githubusercontent.com/39769580/76015897-328c4d00-5f1c-11ea-9de5-c1fc46b414e7.png)

Il suffit alors de la pluger sur les 6 premiers pin du raspberry, comme présenté ci-dessous; 

![image](https://user-images.githubusercontent.com/39769580/76016226-c100ce80-5f1c-11ea-9c1e-674d1846aaba.png)

ATTENTION à bien respecter la polarité pour les borniers des compteurs à impulsion

## Récupération de la TIC

Pour la TIC après avoir installer Picocom dans le terminal, il suffit d’entrer les commandes suivantes ; 

- **picocom -b 9600 -d 7 -p e -f n/dev/ttyS0**  Pour compteur en mode standard 
- **picocom -b 1200 -d 7 -p e -f n/dev/ttyS0**  Pour compteur en mode historique

Les résulats normalent attendus sont présenté ci-dessous; 

![image](https://user-images.githubusercontent.com/39769580/76018539-7e40f580-5f20-11ea-8d4a-857c920ca5a5.png)

On peut remarquer que les étiquettes des données restituées sont conforme à la documentation <a href="https://www.enedis.fr/sites/default/files/Enedis-NOI-CPT_54E.pdf" target="_blank" >ENEDIS</a>. 

![image](https://user-images.githubusercontent.com/39769580/76018529-7b460500-5f20-11ea-8d89-33839cad184e.png)

 ## Récupération des impulsions. 

2 programmes sont disponibles afin d’interagir soit avec le compteur correspondant à la pin 17 ou 4 du raspberry. 

Ce shield est sous la licence libre LGPL (licence libre ouverte avec citation des sources)

