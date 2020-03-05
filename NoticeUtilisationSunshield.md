
## Soudage des composants traversant sur le PCB

Afin d’avoir le moins de difficultés possible nous vous conseillons de souder les composants dans l’ordre suivant :
- Les résistances : R1, R2, R3, R4, R5, 56
- U4 (optocoupleur)
- U1 (Comparateur)
- Borniers à vis
- Header femmelle raspberry

Après soudage des composants, la carte devrait se présenter comme suit : 


![2004C04D-BB02-4FB7-82B7-72F6062E4B26](https://user-images.githubusercontent.com/39769580/76019076-7897df80-5f21-11ea-9535-1b0dbdda3ec3.jpeg)

## Branchement du shield sur le raspberry
Le shield utilise les 12 premieres broches du rasperry; 

![Image description](https://user-images.githubusercontent.com/39769580/76015897-328c4d00-5f1c-11ea-9de5-c1fc46b414e7.png)

Il suffit alors de la pluger sur les 6 premiers pin du raspberry, comme présenté ci-dessous; 

![image](https://user-images.githubusercontent.com/39769580/76018951-41293300-5f21-11ea-9645-6601f511ff1f.png)


ATTENTION à bien respecter la polarité pour les borniers des compteurs à impulsion

## Récupération de la TIC

Pour la TIC après avoir installer Picocom dans le terminal, il suffit d’entrer les commandes suivantes ; 

- **picocom -b 9600 -d 7 -p e -f n/dev/ttyS0**  Pour compteur en mode standard 
- **picocom -b 1200 -d 7 -p e -f n/dev/ttyS0**  Pour compteur en mode historique

Les résulats normalent attendus sont présenté ci-dessous; 

![image](https://user-images.githubusercontent.com/39769580/76019730-75e9ba00-5f22-11ea-980c-cfb8cacd7eb9.png)

On peut remarquer que les étiquettes des données restituées sont conforme à la documentation <a href="https://www.enedis.fr/sites/default/files/Enedis-NOI-CPT_54E.pdf" target="_blank" >ENEDIS</a> (page 18) 

![image](https://user-images.githubusercontent.com/39769580/76018539-7e40f580-5f20-11ea-8d4a-857c920ca5a5.png)


 ## Récupération des impulsions. 

 <a href="https://github.com/sunsharebox/sunshield_linky/tree/master/Recuperation_Compteur_impulsion" target="_blank" >2 programmes</a> sont disponibles afin d’interagir soit avec le compteur correspondant à la pin 17 ou 4 du raspberry. 

Copier le programme sur le raspebbery, se rendre sur le terminal dans le dossier où se trouve les programmes. Lancer le programme avec la commande "

- **sudo python +NOM_PROGRAMME**

Voici le résultat attendu; 


![image](https://user-images.githubusercontent.com/39769580/76019459-0a075180-5f22-11ea-91ad-e65626841355.png)



 <p> Pour toute question, ecrire à <a href="mailto:contact@sunshare.fr/">contact@sunshare.fr</a><br><br>
</p>


*Ce shield est sous la licence libre*

