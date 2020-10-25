## RobotEvo-LMGP

I'm using `numpy 1.19.1`, in `Python 3.7`.

---
# Utilisation du code
Ce code a été dévellopé dans le cadre d'un projet de pilotage d'un robot à l'aide d'une interface Python pour le laboratoire LMGP.\
Dévellopeur : Marie Dutoit et Samy Idelcadi

Le fichier `GUI.py` permet de récupérer les paramètres que souhaite appliquer l'utilisateur. Ce programme va générer les fichier `donnees.txt`, `donnees_puit.txt`, `Protein_n_{}.txt` et `variables.txt`. Le fichier `main.py` permet de générer des worlists `worklist_name.gwl` à partir des fichiers .txt générer par le GUI. Ces Worklists sont ensuite lisible par la machine.

Le rapport développeur à développeur pour la partie GUI est disponible en pdf.

1. Exécuter le fichier `GUI.py`. Afin de valider les paramètres et avant de sélectionner "next" l'utilisateur doit appuyer sur "Validate". Les noms possibles pour les protéines sont : 'streptavidin', 'SAV', 'RGD, 'RAD', 'bBMP', 'aBMP'.

2. Exécuter le fichier `main.py`. 
