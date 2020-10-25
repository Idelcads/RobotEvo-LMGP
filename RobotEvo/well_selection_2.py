import renommer_puits as rp

def well_selection(file):
    list_wells = ""
    # dans cette liste on trouvera à la suite toutes les infos pour (1ere colonne du premier bloc a remplir)(1ere colonne du 2eme bloc a remplir)etc
    with open(file, 'r') as fp:
        liste_puits = []
        line1=fp.readline()
        while line1!='Emplacements Puits\n':
            line1=fp.readline()
        nombre_puits=fp.readline()
        nombre_puits=int(nombre_puits)
        with open('fichier_provisoir.txt','w') as f:
            f.write('puits\n')
        for i in range(nombre_puits):
            line1=fp.readline()
            with open('fichier_provisoir.txt','a') as f:
                f.write(line1)
    with open('fichier_provisoir.txt','r') as f:
        contenu = f.read()
        L1 = len(contenu)
        # les 5 premières lettres sont 'puits'
        # chaque retour à la ligne compte comme un caractere
        # les lettres des puits sont contenus dans les 6+3*i pour i allant de 1 à la fin
        i = 0
        lettres = []
        while 6 + 3 * i < L1:
            indice = 6 + 3 * i
            # on récupere la lettre du puits selectionné dans la string lettres
            lettres += contenu[indice]
            i += 1

        # a ce stade, lettres contient toutes les lettres des puits sélectionnés précédemment

        # on récupère ensuite les numéros de chaque puits
        i = 0
        nb_lignes=0
        numeros = ''
        while 7 + 3 * i <= L1:
            nb_lignes+=1
            #nb_lignes calcule le nombre de lignes du fichier de données
            indice = 7 + 3 * i
            numeros += (contenu[indice])
            i += 1
        #numeros est une string qui contient tous les numéros de colonnes des puits selectionnés

        #on parcourt le liste des numéros pour les traduire pour le robot. On met le tout dans une liste appelée 'colonne'
        colonnes=[]
        for i in range(nb_lignes):
            num = int(''.join(map(str, numeros[i])))
             # num est un entier; il contient le numéro 'numéro[j]'
            numero = (num - 1) * 3 + 2
            colonnes.append(numero)

        # on va maintenant determiner si pour chaque colonne les lettres sélectionnées font parties du bloc 1 ou du bloc 2.
        #une liste 'bloc' est crée. bloc[0] informe si lettres[0] est dans le bloc 1 ou 2 et ainsi de suite jusqu'a bloc[nb_lignes]
        bloc=[]
        for i in range (nb_lignes):
            l=lettres[i]
            if l=='A' or l=='B' or l=='C' or l=='D':
                bloc.append('0108?0')
            else:
                bloc.append('0108 1')
        #on va maintenant déterminer si c'est le bras 1,2,3 ou 4 qui va remplir.
        #on crée une liste bras; si le bras à utliser est le bras 1, on rentre dans la liste volume 1
        bras=[]
        for i in range(nb_lignes):
            l=lettres[i]
            [num_bloc,num_bras]=rp.lien_lettre_nombre(l)
            bras.append(num_bras)
    print(bras,bloc,colonnes)
    return bras,bloc,colonnes



