Le code intégral de la boxenergie est développé sous nodered et mis à disposition sur la page http://github.com/boxenergie.

Ce code python permet d'intéragir avec les pins du raspberry qui sont ainsi en relation avec les borniers du shield.

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

