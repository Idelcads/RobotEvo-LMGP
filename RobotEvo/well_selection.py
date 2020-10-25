import renommer_puits as rp

def well_selection(volume,file):
    list_wells=""
    #dans cette liste on trouvera à la suite toutes les infos pour (1ere colonne du premier bloc a remplir)(1ere colonne du 2eme bloc a remplir)etc
    with open(file,'r') as f:
        liste_puits=[]
        contenu=f.read()
        L1=len(contenu)
        #les 5 premières lettres sont 'puits'
        #chaque retour à la ligne conte comme un caractere
        #les lettres des puits sont contenus dans les 6+3*i pour i allant de 1 à la fin
        i=0
        lettres=[]
        while 6+3*i<L1:
            indice=6+3*i
            #on récupere la lettre du puits selectionné dans la string lettres
            lettres+=contenu[indice]
            i+=1

        #a ce stade, lettres contient toutes les lettres des puits sélectionnés précédemment

        #on récupère ensuite les numéros de chaque puits
        i=0
        numeros=''
        while 7+3*i<=L1:
            indice=7+3*i
            numeros+=(contenu[indice])
            i+=1

        #on va maintenant determiner si pour chaque colonne les lettres sélectionnées sont A,B,C ou D
        L2 = len(lettres)
        k,l,m=0,0,0
        if L2>0:
            for j in range(L2):
                if L2>1:
                    for k in range(1,L2):
                        if 2<L2:
                            for l in range(2,L2):
                                if L2>3:
                                    for m in range(2,L2):
                                        print(positionner_volume(lettres,numeros,volume,j,k,l,m, L2))
                                else:
                                    print(positionner_volume(lettres, numeros, volume, j, k, l, m, L2))
                        else:
                            liste,L2=positionner_volume(lettres,numeros,volume,j,k,l,m,L2)
        else:
            print(liste)







def positionner_volume(lettres,numeros,volume,j,k,l,m,L2):
    list_wells=''
    num = int(''.join(map(str, numeros[j])))
    numero = (num - 1) * 3 + 2
    if L2>3:
        bloc1,nombre_corres1 = rp.lien_lettre_nombre(lettres[j])
        bloc2,nombre_corres2 = rp.lien_lettre_nombre(lettres[k])
        bloc3,nombre_corres3 = rp.lien_lettre_nombre(lettres[l])
        bloc4,nombre_corres4 = rp.lien_lettre_nombre(lettres[m])


        # si on a les puits Ax et (Bx/Cx/Dx) selectionnes

        if bloc1==bloc2:
            # cas AxBx
            if nombre_corres1 == 1 and nombre_corres2 == 2 and nombre_corres3 != 3 and nombre_corres4 != 4 and numeros[j] == numeros[k] :
                # la colonne 1 est en fait la 2 pour le robot, la 2 est la 5, la 3 est la 8 etc
                list_wells += "{0}".format(volume) + "{0}".format(volume) + "0" + "0" + "12" + "{0}".format(numero) + "0108?0"
                # on a d'abord les 4 volumes dans les 4 puits du bloc puis l'emplacement de la plaque sur le robot (12) puis la colonne et enfin le bloc du haut ou bloc du bas
                lettres.pop(j)
                lettres.pop(j)
                L2=len(lettres)
                # cas AxCx
            elif nombre_corres1 == 1 and nombre_corres2 == 3 and nombre_corres3 != 2 and nombre_corres4 != 4 and numeros[j] == \
                    numeros[k]:
                list_wells += "{0}".format(volume) + "0" + "{0}".format(volume) + "0" + "12" + "{0}".format(numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(j)
                L2 = len(lettres)
                # cas AxDx
            elif nombre_corres1 == 1 and nombre_corres2 == 4 and nombre_corres3 != 2 and nombre_corres4 != 3 and nombre_corres3 != 2 and nombre_corres4 != 3 and \
                    numeros[j] == numeros[k]:
                list_wells += "{0}".format(volume) + "0" + "0" + "{0}".format(volume) + "12" + "{0}".format(numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(j)
                L2 = len(lettres)
                # cas CD
            elif nombre_corres1 == 3 and nombre_corres2 == 4 and nombre_corres3 != 1 and nombre_corres4 != 2 and numeros[j] == \
                    numeros[k]:
                list_wells += "0" + "0" + "{0}".format(volume) + "{0}".format(volume) + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)
                # cas BC
            elif nombre_corres1 == 3 and nombre_corres2 == 2 and nombre_corres3 != 1 and nombre_corres4 != 4 and numeros[j] == \
                    numeros[k]:
                list_wells += "0" + "{0}".format(volume) + "{0}".format(volume) + "0" + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)

            elif bloc2==bloc3:
                # cas ABC
                if nombre_corres1==1 and nombre_corres2 == 2 and nombre_corres3 == 3 and nombre_corres4 != 4 and numeros[j] == numeros[k]:
                    list_wells += "{0}".format(volume) + "{0}".format(volume) + "{0}".format(volume) + "0" + "12" + "{0}".format(
                        numero) + "0108?0"
                    lettres.pop(j)
                    lettres.pop(k)
                    lettres.pop(l)
                    L2 = len(lettres)
                    # cas BCD
                elif nombre_corres1 == 4 and nombre_corres2 == 2 and nombre_corres3 == 3 and nombre_corres4 != 1 and numeros[j] == \
                        numeros[k]:
                    list_wells += "0" + "{0}".format(volume) + "{0}".format(volume) + "{0}".format(volume) + "12" + "{0}".format(
                        numero) + "0108?0"
                    lettres.pop(j)
                    lettres.pop(k)
                    lettres.pop(l)
                    L2 = len(lettres)
                    # casABD
                elif nombre_corres1 == 4 and nombre_corres2 == 2 and nombre_corres3 == 1 and nombre_corres4 != 3 and numeros[j] == \
                        numeros[k]:
                    list_wells += "{0}".format(volume) + "{0}".format(volume) + "{0}".format(
                        volume) + "0" + "12" + "{0}".format(
                        numero) + "0108?0"
                    lettres.pop(j)
                    lettres.pop(k)
                    lettres.pop(l)
                    L2 = len(lettres)
                elif bloc3==bloc4:
                        # cas ABCD
                    if nombre_corres1 == 4 and nombre_corres2 == 2 and nombre_corres3 == 1 and nombre_corres4 == 3 and numeros[j] == \
                        numeros[k]:
                        list_wells += "{0}".format(volume) + "{0}".format(volume) + "{0}".format(
                        volume) + "{0}".format(volume) + "12" + "{0}".format(
                        numero) + "0108?0"
                        lettres.pop(j)
                        lettres.pop(k)
                        lettres.pop(l)
                        lettres.pop(m)
                        L2 = len(lettres)
    if L2==3:
        bloc1, nombre_corres1 = rp.lien_lettre_nombre(lettres[j])
        bloc2, nombre_corres2 = rp.lien_lettre_nombre(lettres[k])
        bloc3, nombre_corres3 = rp.lien_lettre_nombre(lettres[l])

        if bloc1 == bloc2:
            # cas AxBx
            if nombre_corres1 == 1 and nombre_corres2 == 2 and nombre_corres3!=3 and numeros[j] == numeros[k]:
                # la colonne 1 est en fait la 2 pour le robot, la 2 est la 5, la 3 est la 8 etc
                num = int(''.join(map(str, numeros[j])))
                numero = (num - 1) * 3 + 2
                list_wells += "{0}".format(volume) + "{0}".format(volume) + "0" + "0" + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)
                # on a d'abord les 4 volumes dans les 4 puits du bloc puis l'emplacement de la plaque sur le robot (12) puis la colonne et enfin le bloc du haut ou bloc du bas

                # cas AxCx
            elif nombre_corres1 == 1 and nombre_corres2 == 3 and nombre_corres3 != 2 and \
                    numeros[j] == \
                    numeros[k]:
                list_wells += "{0}".format(volume) + "0" + "{0}".format(volume) + "0" + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)
                # cas AxDx
            elif nombre_corres1 == 1 and nombre_corres2 == 4 and nombre_corres3 != 2 and \
                    numeros[j] == numeros[k]:
                list_wells += "{0}".format(volume) + "0" + "0" + "{0}".format(volume) + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)
                # cas CD
            elif nombre_corres1 == 3 and nombre_corres2 == 4 and nombre_corres3 != 1 and \
                    numeros[j] == \
                    numeros[k]:
                list_wells += "0" + "0" + "{0}".format(volume) + "{0}".format(volume) + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)
                # cas BC
            elif nombre_corres1 == 3 and nombre_corres2 == 2 and nombre_corres3 != 1 and \
                    numeros[j] == \
                    numeros[k]:
                list_wells += "0" + "{0}".format(volume) + "{0}".format(volume) + "0" + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)

            elif bloc2 == bloc3:
                # cas ABC
                if nombre_corres1 == 1 and nombre_corres2 == 2 and nombre_corres3 == 3  and \
                        numeros[j] == numeros[k]:
                    list_wells += "{0}".format(volume) + "{0}".format(volume) + "{0}".format(
                        volume) + "0" + "12" + "{0}".format(
                        numero) + "0108?0"
                    lettres.pop(j)
                    lettres.pop(j)
                    lettres.pop(j)
                    L2 = len(lettres)
                    # cas BCD
                elif nombre_corres1 == 4 and nombre_corres2 == 2 and nombre_corres3 == 3  and \
                        numeros[j] == \
                        numeros[k]:
                    list_wells += "0" + "{0}".format(volume) + "{0}".format(volume) + "{0}".format(
                        volume) + "12" + "{0}".format(
                        numero) + "0108?0"
                    lettres.pop(j)
                    lettres.pop(k)
                    lettres.pop(l)
                    L2 = len(lettres)
                    # casABD
                elif nombre_corres1 == 4 and nombre_corres2 == 2 and nombre_corres3 == 1 and \
                        numeros[j] == \
                        numeros[k]:
                    list_wells += "{0}".format(volume) + "{0}".format(volume) + "{0}".format(
                        volume) + "0" + "12" + "{0}".format(
                        numero) + "0108?0"
                    lettres.pop(j)
                    lettres.pop(k)
                    lettres.pop(l)
                    L2 = len(lettres)

    if L2==2:
        bloc1, nombre_corres1 = rp.lien_lettre_nombre(lettres[j])
        bloc2, nombre_corres2 = rp.lien_lettre_nombre(lettres[k])
        #si les puits sélectionnés font partis du bloc du haut ou font partis du bloc du bas
        if bloc1 == bloc2:
            # cas AxBx
            if nombre_corres1 == 1 and nombre_corres2 == 2 and numeros[j] == numeros[k]:
                # la colonne 1 est en fait la 2 pour le robot, la 2 est la 5, la 3 est la 8 etc
                num = int(''.join(map(str, numeros[j])))
                numero = (num - 1) * 3 + 2
                list_wells += "{0}".format(volume) + "{0}".format(volume) + "0" + "0" + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)
                # on a d'abord les 4 volumes dans les 4 puits du bloc puis l'emplacement de la plaque sur le robot (12) puis la colonne et enfin le bloc du haut ou bloc du bas

                # cas AxCx
            elif nombre_corres1 == 1 and nombre_corres2 == 3 and \
                    numeros[j] == \
                    numeros[k]:
                list_wells += "{0}".format(volume) + "0" + "{0}".format(volume) + "0" + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)
                # cas AxDx
            elif nombre_corres1 == 1 and nombre_corres2 == 4 and \
                    numeros[j] == numeros[k]:
                list_wells += "{0}".format(volume) + "0" + "0" + "{0}".format(volume) + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)
                # cas CD
            elif nombre_corres1 == 3 and nombre_corres2 == 4 and \
                    numeros[j] == \
                    numeros[k]:
                list_wells += "0" + "0" + "{0}".format(volume) + "{0}".format(volume) + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)
                # cas BC
            elif nombre_corres1 == 3 and nombre_corres2 == 2 and \
                    numeros[j] == \
                    numeros[k]:
                list_wells += "0" + "{0}".format(volume) + "{0}".format(volume) + "0" + "12" + "{0}".format(
                    numero) + "0108?0"
                lettres.pop(j)
                lettres.pop(k)
                L2 = len(lettres)


    return(list_wells,L2)






#si c'est A et B
#"volume","volume","0","0","0108?0"
#si c'est B et C
#"0","0","volume","volume","0108?0"

if __name__ == '__main__':
   well_selection(10, 'donnees.txt')


