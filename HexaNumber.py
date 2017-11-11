#!/usr/bin/env python
# Importation de toutes les bibliotheques utilisees
from tkinter import *
from random import *
from math import *
from time import *

        ##############################################
def Verif_hexagone(X,Y):
    # Variables globales
    global Liste_global
    global valeur_Clic
    global cases_totale
    global L
    global h
    global decal_droite
    global decal_bas  
    
    valeur_Clic = 0
    # Equation pour chaques droites #
    droite_1 = (h/L)* X
    droite_2 = -(h/L)* X + 2*h
    droite_3 = (h/L)* X - 4*h
    droite_4 = -(h/L)* X - 2*h
    
    # Verifie pour les 19 hexagones les 6 conditions pour savoir lequel des hexagones est selectionne #
    for i in range (0,cases_totale):
        
        valeur_droites_1_3 = 3*h*int(Liste_global[i][1]) - h*int(Liste_global[i][2]) - decal_droite*(h/L) + decal_bas
        valeur_droites_2_4 = 3*h*int(Liste_global[i][1]) + h*int(Liste_global[i][2]) + decal_droite*(h/L) + decal_bas

        if int(Liste_global[i][2])*L + decal_droite < X < (int(Liste_global[i][2])+2)*L + decal_droite and Y < droite_1 + valeur_droites_1_3 and Y < droite_2 + valeur_droites_2_4 and Y > droite_3 + valeur_droites_1_3 and Y > droite_4 + valeur_droites_2_4 :
            valeur_Clic = i+1


        ##############################################
# Detecte l'hexagone que l'on clique #
def Clic_1(event):
    # Variables globales
    global Liste_global
    global valeur_Clic_1
    global Main_Canvas
    
    X = event.x
    Y = event.y    

    valeur_Clic_1 = 0
    Verif_hexagone(X,Y)
    valeur_Clic_1 = valeur_Clic
    
    #Verifie qu'il s'agit d'une case pleine, donc avec une valeur #              
    if valeur_Clic_1 != 0:
        if Liste_global[valeur_Clic_1-1][3] != 0 :
            Main_Canvas.bind("<Button-1>",Clic_2) # Permet de definir le bouton 1 de la souris sur la procedure Clic_2

        ##############################################
# Detecte l'hexagone ou l'on clique #
def Clic_2(event):
    # Variables globales
    global Liste_global
    global valeur_Clic_2
    global nbr_groupe_avant
    global L
    global h
    global decal_droite
    global decal_bas
    global Main_Canvas
    
    X = event.x
    Y = event.y
    
    valeur_Clic_2 = 0
    Verif_hexagone(X,Y)
    valeur_Clic_2 = valeur_Clic
    
    # Verifie qu'il s'agit d'une case vide donc sans valeur #
    if valeur_Clic_2 != 0:
        if Liste_global[(valeur_Clic_2) -1][3]== 0 :
            Main_Canvas.bind("<Button-1>",Clic_1)  # Permet de definir le bouton 1 de la souris sur la procedure Clic_1 

            # Supprime les objets textes et les cases
            Main_Canvas.delete(Liste_global[valeur_Clic_1-1][4]) 
            Main_Canvas.delete(Liste_global[valeur_Clic_1-1][5])
            # Changer les valeurs dans Liste_valeur #
            val_couleur_Clic_1 = Liste_global[valeur_Clic_1-1][6]
            val_couleur_Clic_2 = Liste_global[valeur_Clic_2-1][6]
            val_Clic_1 = Liste_global[valeur_Clic_1-1][3]
            val_Clic_2 = Liste_global[valeur_Clic_2-1][3]
            Liste_global[valeur_Clic_1-1][6] = val_couleur_Clic_2
            Liste_global[valeur_Clic_2-1][6] = val_couleur_Clic_1
            Liste_global[valeur_Clic_1-1][3] = val_Clic_2
            Liste_global[valeur_Clic_2-1][3] = val_Clic_1
            # Creer les nouveaux objets avec les nouvelles valeurs
            Colonne = int(Liste_global[valeur_Clic_1-1][2])
            Ligne = int(Liste_global[valeur_Clic_1-1][1])-1
            Liste_global[valeur_Clic_1-1][5]= Main_Canvas.create_polygon(decal_droite+Colonne*L,decal_bas+h+Ligne*(3*h), decal_droite+L+Colonne*L,decal_bas+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+h+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+3*h+Ligne*(3*h) , decal_droite+L+Colonne*L,decal_bas+4*h+Ligne*(3*h) , decal_droite+Colonne*L,decal_bas+3*h+Ligne*(3*h) , fill=Couleur[Liste_global[valeur_Clic_1-1][6]],outline='black',width=2)
            Colonne = int(Liste_global[valeur_Clic_2-1][2])
            Ligne = int(Liste_global[valeur_Clic_2-1][1])-1
            Liste_global[valeur_Clic_2-1][5]= Main_Canvas.create_polygon(decal_droite+Colonne*L,decal_bas+h+Ligne*(3*h), decal_droite+L+Colonne*L,decal_bas+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+h+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+3*h+Ligne*(3*h) , decal_droite+L+Colonne*L,decal_bas+4*h+Ligne*(3*h) , decal_droite+Colonne*L,decal_bas+3*h+Ligne*(3*h) , fill=Couleur[Liste_global[valeur_Clic_2-1][6]],outline='black',width=2)
            Liste_global[valeur_Clic_2-1][4] = Main_Canvas.create_text(decal_droite+L*(Colonne+1),decal_bas+3*h*(Ligne+1)-h,text = Liste_global[valeur_Clic_2-1][3],font = "Arial 16 bold",fill = "black")
            # Actualisation du Main_Canvas
            Main_Canvas.update()
            sleep(0.3)
            nbr_groupe_avant = 0
            # Execute la procedure
            Reperage_et_fusion()
            # Relance la procedure aleatoire lorsqu'il y a pas de groupe formes
            if nbr_groupe_avant == 0:
                Main_Canvas.update()
                sleep(0.3)
                Aleatoire()

        ##############################################
# Creation d'un hexagone #
def Hexagone(x,y):
    # Variables globales
    global Couleur
    global L
    global h
    global Main_Canvas
    Liste_global[j][5]= Main_Canvas.create_polygon(x,h+y , L+x,y , 2*L+x,h+y , 2*L+x,3*h+y , L+x,4*h+y , x,3*h+y , fill=Couleur[(Liste_global[j][6])],outline='black',width=2)
    
        ##############################################
# Permet de faire apparaitre aleatoirement des 1 et 2 sur la grille #
def Aleatoire():
    # Variables globales
    global Liste_global
    global valeur_Clic_2
    global nbr_case_vide
    global cases_totale
    global L
    global h
    global decal_droite
    global decal_bas
    global Couleur
    global nbr_case_vide
    global Largeur
    global Hauteur
    global Main_Canvas

    Main_Canvas.unbind_all('<Button-1>')
    
    nbr_case_vide=0
    for i in range (0,cases_totale):  # Compte le nombre de case vide
        if Liste_global[i][3]==0:
            nbr_case_vide = nbr_case_vide + 1
    nbr_case = ceil(nbr_case_vide*0.35)     # 35% des cases vides arrondi a l'entier superieur
    k=0
    while k <= nbr_case-1:      
        Case_choisi = randint(1,19)     # Choisi aleatoirement une case entre 1 et 19
        
        if Liste_global[Case_choisi-1][3] == 0:        # Si le numero de la case choisi est une case vide alors on remplace par un 1 ou 2
            Liste_global[Case_choisi-1][3] = randint(1,2)# Choisi aleatoirement un 1 ou 2
            Main_Canvas.delete(Liste_global[Case_choisi-1][5])
            Liste_global[Case_choisi-1][6]= Liste_global[Case_choisi-1][3]
            Colonne = int(Liste_global[int(Case_choisi-1)][2])
            Ligne = int(Liste_global[int(Case_choisi-1)][1])-1
            Liste_global[Case_choisi-1][5]= Main_Canvas.create_polygon(decal_droite+Colonne*L,decal_bas+h+Ligne*(3*h), decal_droite+L+Colonne*L,decal_bas+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+h+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+3*h+Ligne*(3*h) , decal_droite+L+Colonne*L,decal_bas+4*h+Ligne*(3*h) , decal_droite+Colonne*L,decal_bas+3*h+Ligne*(3*h) , fill=Couleur[Liste_global[Case_choisi-1][6]],outline='black',width=2)
            Liste_global[Case_choisi-1][4] = Main_Canvas.create_text(decal_droite+L*(Colonne+1),decal_bas+3*h*(Ligne+1)-h,text = Liste_global[Case_choisi-1][3],font = "Arial 16 bold",fill = "black")   # Placement du chiffre sur la grille
            k=k+1
    valeur_Clic_2=0
    
    nbr_groupe_avant = 0
    Main_Canvas.update()
    sleep(0.3)
    Reperage_et_fusion()
    Main_Canvas.bind('<Button-1>',Clic_1)
    if nbr_case_vide == 0:
        Main_Canvas.create_text(Largeur/2,Hauteur*(5/6),text = 'GAMEOVER',font = "Arial 72 bold",fill = "black") 
    
        ##############################################
# Procedure permettant de reperer les cases voisines ainsi que de les fusioner en une valeur qui est le somme des trois #            
def Reperage_et_fusion():

    # Variables globales
    global Liste_global
    global nbr_groupe
    global nbr_groupe_avant
    global cases_totale
    global L
    global h
    global decal_droite
    global decal_bas
    global valeur_score
    global nbr_case_vide
    global Main_Canvas
    
    # Liste permettant de connaitre facilement les cases voisines #
    Liste_Coordonnees = [] # Creation de la liste
    for i in range (0,cases_totale):
        Liste_Coordonnees.append(str(Liste_global[i][1])+str(Liste_global[i][2]))
    liste_reperage = [] # Liste contenant les numeros des cases identiques collees
    for i in range (0,cases_totale):
        # Recuperation des coordonnees de la case principale et initialisation de variables
        nbr_case_voisine=0
        Ligne = Liste_global[i][1]
        Colonne = Liste_global[i][2]
        Liste_case_voisine = []
        
        # Les 6 cases autour de la case centrale #
        Coordonnees_1 = str(int(Ligne)-1)+str(int(Colonne)-1)
        Coordonnees_2 = str(int(Ligne)-1)+str(int(Colonne)+1)
        Coordonnees_3 = str(int(Ligne))+str(int(Colonne)+2)
        Coordonnees_4 = str(int(Ligne)+1)+str(int(Colonne)+1)
        Coordonnees_5 = str(int(Ligne)+1)+str(int(Colonne)-1)
        Coordonnees_6 = str(int(Ligne))+str(int(Colonne)-2)
        
        Liste_nom = [Coordonnees_1,Coordonnees_2,Coordonnees_3,Coordonnees_4,Coordonnees_5,Coordonnees_6]
        # Boucle permettant de verifier les 6 cases differentes #
        for j in range (0,len(Liste_nom)):
            if Liste_global[i][3]!=0: # Verifie si c'est un case  centrale avec une valeur differente de 0
            
                if (Liste_nom[j] in Liste_Coordonnees) == True : # Verifie si la case voisine est dans la grille
                    case_voisine = Liste_Coordonnees.index(Liste_nom[j]) # Recupere le numero de la case
                
                    if Liste_global[int(case_voisine)][3]==Liste_global[i][3]: # Verifie si la case voisine a la meme valeur que la case centrale
                        Liste_case_voisine.append(case_voisine+1) # Liste contenant les numeros des cases identiques a la case principale
        Liste_case_voisine.append(i+1) # Ajoute la valeur centrale
        if len(Liste_case_voisine)> 1: # Verifie si il y a au moins une case identique a celle du milieu
            for k in range(0,len(Liste_case_voisine)): # Pour chaques cases identiques 
                for i in range(0,len(liste_reperage)): # Pour chaques groupes de cases de meme valeur 
                    if (Liste_case_voisine[k]in liste_reperage[i])==True: # Verifie si la case appartient deja a un groupe
                        for j in range(0,len(liste_reperage[i])): # Pour chaque case appartenant a un groupe
                            if liste_reperage[i][j]==Liste_case_voisine[k]: # Si la case repere est deja dans un groupe
                                liste_reperage[i].remove(Liste_case_voisine[k]) # Supprime du groupe la case repere
                                for l in range (0,len(Liste_case_voisine)): # Ajoute les numeros des cases reperer dans le groupe
                                    liste_reperage[i].append(Liste_case_voisine[l])
            nbr=0
            # Si il n'est pas rajoute dans un groupe, on l'ajoute a la liste #
            if (Liste_case_voisine in liste_reperage)==False:
                liste_reperage.append(Liste_case_voisine)
            # Compte le nombre d'occurence de la premiere valeur
            for i in range(0,len(liste_reperage)):
                nbr=nbr+liste_reperage[i].count(Liste_case_voisine[0])
            if nbr > 1: # Si elle est plusieurs fois on supprime celle qu'on a rajoute
                del(liste_reperage[len(liste_reperage)-1])
            # Si dans la liste, le numero est plusieurs fois, on le supprime pour qui reste une fois
            for i in range(0,len(Liste_case_voisine)):
                for j in range(0,len(liste_reperage)):
                    while liste_reperage[j].count(Liste_case_voisine[i])>1:
                        liste_reperage[j].remove(Liste_case_voisine[i])
    # Trie la liste case voisine par taille de liste de la plus petite a la plus grande
    # Initialise les listes
    liste = []
    liste_nbr = []
    taille = []
    # Recupere la taille de chaque liste de liste
    for i in range (0,len(liste_reperage)):
        taille.append(len(liste_reperage[i]))
    # Trie les nombres de la liste du plus petit au plus grand
    taille.sort()
    # On copie la liste reperage
    for i in range (0,len(taille)):
        liste.insert(taille.index(len(liste_reperage[i])),liste_reperage[i])
    # Initialise la liste nbr
    liste_nbr = [0]* len(liste_reperage) 
    for i in range(0,len(taille)):
        liste_nbr[i] = [0]*taille[i]
    # Rempli la liste nbr par le nombre de fois qu'est present le nombre et si il est 2 la premiere fois qu'il le rencontre il met un 2 et la deuxieme un 1
    n=-1
    for i in range(0,len(liste_nbr)):
        n=n+1
        for j in range(0,len(liste_nbr[i])):
            nbr = 0
            for k in range(n,len(liste_nbr)):
                nbr+=liste[k].count(liste[i][j])
            liste_nbr[i][j]=(nbr)
    # Supprime la liste de liste ou il y a un autre chiffre que 1
    for i in range (0,len(liste_nbr)):
        if liste_nbr[i].count(1)!= taille[i]:
            del liste[i][0:taille[i]]
    liste_reperage = liste

    # Placement de la nouvelle case #
    nbr_groupe = 0
    for i in range(0,len(liste_reperage)):
        if len(liste_reperage[i]) > 2:
            # Donne le nombre de groupe forme au total
            nbr_groupe = nbr_groupe+1
            # Augmente le score
            valeur_score = valeur_score + ((Liste_global[valeur_Clic_2-1][3])*(len(liste_reperage[i])))
            Score.config(text='SCORE: %.0f'%(valeur_score))
            # Choix de la case de fusion
            if (valeur_Clic_2 in liste_reperage[i])==True:
                # Lorsqu'il s'agit d'une case deplacee
                valeur_case_principale = (Liste_global[valeur_Clic_2-1][3])*3
                valeur_couleur = (Liste_global[valeur_Clic_2-1][6])+2
                # Change les valeurs des cases et supprime les objets
                for j in range (0,len(liste_reperage[i])):
                    Main_Canvas.delete(Liste_global[int(liste_reperage[i][j])-1][4])
                    Main_Canvas.delete(Liste_global[int(liste_reperage[i][j])-1][5])
                    Liste_global[int(liste_reperage[i][j])-1][3]=0 
                    Liste_global[int(liste_reperage[i][j])-1][6]=0
                    Ligne = Liste_global[int(liste_reperage[i][j])-1][1]-1
                    Colonne = Liste_global[int(liste_reperage[i][j])-1][2]
                    Liste_global[int(liste_reperage[i][j])-1][5]= Main_Canvas.create_polygon(decal_droite+Colonne*L,decal_bas+h+Ligne*(3*h), decal_droite+L+Colonne*L,decal_bas+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+h+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+3*h+Ligne*(3*h) , decal_droite+L+Colonne*L,decal_bas+4*h+Ligne*(3*h) , decal_droite+Colonne*L,decal_bas+3*h+Ligne*(3*h) , fill=Couleur[Liste_global[int(liste_reperage[i][j])-1][6]],outline='black',width=2)
                # Change les valeurs de la nouvelle case et creer la nouvelle case
                Ligne = Liste_global[valeur_Clic_2-1][1]-1
                Colonne = Liste_global[valeur_Clic_2-1][2]
                Liste_global[valeur_Clic_2-1][3] = valeur_case_principale
                Liste_global[valeur_Clic_2-1][6] = valeur_couleur
                Liste_global[valeur_Clic_2-1][5]= Main_Canvas.create_polygon(decal_droite+Colonne*L,decal_bas+h+Ligne*(3*h), decal_droite+L+Colonne*L,decal_bas+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+h+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+3*h+Ligne*(3*h) , decal_droite+L+Colonne*L,decal_bas+4*h+Ligne*(3*h) , decal_droite+Colonne*L,decal_bas+3*h+Ligne*(3*h) , fill=Couleur[Liste_global[valeur_Clic_2-1][6]],outline='black',width=2)
                Liste_global[valeur_Clic_2-1][4] = Main_Canvas.create_text(decal_droite+L*Colonne+L,decal_bas+3*h*(Ligne+1)-h,text = Liste_global[valeur_Clic_2-1][3],font = "Arial 16 bold",fill = "black")   # Placement du chiffre sur la grille      
                
            else:
                # Lorsqu'il s'agit d'un groupe fait avec la procedure aleatoire
                case_aleatoire = choice(liste_reperage[i])-1
                valeur_case_principale = (Liste_global[case_aleatoire][3])*3
                valeur_couleur = (Liste_global[case_aleatoire][6])+2
                valeur_score = valeur_score + ((Liste_global[case_aleatoire][3])*(len(liste_reperage[i])))
                Score.config(text='SCORE: %.0f'%(valeur_score))
                # Change les valeurs des cases et supprime les objets
                for j in range (0,len(liste_reperage[i])):
                    Main_Canvas.delete(Liste_global[int(liste_reperage[i][j])-1][4])
                    Main_Canvas.delete(Liste_global[int(liste_reperage[i][j])-1][5])
                    Liste_global[int(liste_reperage[i][j])-1][3]=0
                    Liste_global[int(liste_reperage[i][j])-1][6]=0
                    Ligne = Liste_global[int(liste_reperage[i][j])-1][1]-1
                    Colonne = Liste_global[int(liste_reperage[i][j])-1][2]
                    Liste_global[int(liste_reperage[i][j])-1][5]= Main_Canvas.create_polygon(decal_droite+Colonne*L,decal_bas+h+Ligne*(3*h), decal_droite+L+Colonne*L,decal_bas+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+h+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+3*h+Ligne*(3*h) , decal_droite+L+Colonne*L,decal_bas+4*h+Ligne*(3*h) , decal_droite+Colonne*L,decal_bas+3*h+Ligne*(3*h) , fill=Couleur[Liste_global[int(liste_reperage[i][j])-1][6]],outline='black',width=2)
                # Change les valeurs de la nouvelle case et creer la nouvelle case
                Ligne = Liste_global[case_aleatoire][1]-1
                Colonne = Liste_global[case_aleatoire][2]
                Liste_global[case_aleatoire][3] = valeur_case_principale
                Liste_global[case_aleatoire][6] = valeur_couleur
                Liste_global[case_aleatoire][5]= Main_Canvas.create_polygon(decal_droite+Colonne*L,decal_bas+h+Ligne*(3*h), decal_droite+L+Colonne*L,decal_bas+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+h+Ligne*(3*h) , decal_droite+2*L+Colonne*L,decal_bas+3*h+Ligne*(3*h) , decal_droite+L+Colonne*L,decal_bas+4*h+Ligne*(3*h) , decal_droite+Colonne*L,decal_bas+3*h+Ligne*(3*h) , fill=Couleur[Liste_global[case_aleatoire][6]],outline='black',width=2)
                Liste_global[case_aleatoire][4] = Main_Canvas.create_text(decal_droite+L*Colonne+L,decal_bas+3*h*(Ligne+1)-h,text = Liste_global[case_aleatoire][3],font = "Arial 16 bold",fill = "black")   # Placement du chiffre sur la grille      
                
    # Repete la procedure jusqu'a qu'il n'y est plus de groupes possibles a fusionner
    while nbr_groupe != 0:
        nbr_groupe_avant = nbr_groupe
        Main_Canvas.update()
        sleep(0.3)
        Reperage_et_fusion()
    # Compte le nombre de cases vide pour afficher la fin du jeu
    nbr_case_vide=0
    for i in range (0,cases_totale):
        if Liste_global[i][3]==0:
            nbr_case_vide = nbr_case_vide + 1
    

        ##############################################
def Modif_select():
    # Supprime toute les actions liees a Bouton 1
    Main_Canvas.unbind_all('<Button-1>')
    # Redefini le lien avec la fonction
    Main_Canvas.bind("<Button-1>",Clic_1)
    
        ##############################################
def Regles():
    # Variables globales
    global Largeur
    global Hauteur
    Fenetre_rgl = Toplevel()
    Fenetre_rgl.attributes('-fullscreen',1)
    Fenetre_rgl.title("HexaNumber")


    Image_rgl=PhotoImage(file='Image_rgl.gif')

    Canvas_rgl = Canvas(Fenetre_rgl,width=Largeur,height=Hauteur,bg = "black")
    Canvas_rgl.pack()
    imagefond = Canvas_rgl.create_image(Largeur/2,Hauteur/2,image=Image_rgl)

    bou_Quitter = Button(Fenetre_rgl, text='        QUITTER        ', command=Fenetre_rgl.destroy, relief='flat', bg = 'black', fg = 'white')
    bou_Quitter.place(height=50, width=150, x=Largeur/2-75,y=Hauteur-100)
    
    Fenetre.mainloop()
        
        ##############################################
def Jeu():
    # Creation de la fenetre principale #
    Fenetre_Jeu = Tk()
    Fenetre_Jeu.attributes('-fullscreen',1)
    Fenetre_Jeu.title("HexaNumber")

    # Variables globales
    global Largeur
    global Hauteur
    global valeur_score
    global Score
    global Couleur
    global Main_Canvas
    
    
    # Creation du canvas pour le fond gris #
    Largeur = Fenetre.winfo_screenwidth()
    Hauteur = Fenetre.winfo_screenheight()

    # Variables globales
    global Liste_global
    global cases_totale
    global L
    global h
    global decal_droite
    global decal_bas
    global j
    
    Main_Canvas = Canvas(Fenetre_Jeu,width=Largeur,height=Hauteur,bg='grey')
    Main_Canvas.place(x=0,y=0)

    valeur_score = 0
    Score=Label(Fenetre_Jeu,text='SCORE:%.0f'%(valeur_score),font="Arial 16 bold")
    Score.place(height=50, width=200, x=(Largeur-200)/2,y=30)
    
    bou_Quitter = Button(Fenetre_Jeu, text='QUITTER',font="Arial 10 bold", command=Fenetre_Jeu.destroy)
    bou_Quitter.place(height=90, width=130, x=Largeur-160, y=30)
    bou_retour_select = Button(Fenetre_Jeu, text='ANNULE SELECTION',font="Arial 10 bold",command = Modif_select)
    bou_retour_select.place(height=50, width=180, x=Largeur-210,y=Hauteur/2-50)

    # Initialisation des variables #
    cases_totale = 19       # nombre de cases totales
    h = 20                  # hauteur/4
    L = 34                  # longueur/2
    decal_droite = (Largeur/2)-5*L     # Decalage vers la droite de toute la grille
    decal_bas = (Hauteur/2)-8*h        # Decalage vers le bas de toute la grille

    # Liste global qui contient le numero de la case,la ligne, la colonne, valeur de la case et l'objet qui est dans la case #
    Liste_global = [0]*cases_totale
    for i in range (0,cases_totale):
        Liste_global[i] = [0]*7

    # Creation de la grille #
    j=-1
    for i in range(0,3):
        x=decal_droite+2*L+2*L*i
        y=decal_bas
        j=j+1
        Liste_global[j][0]=j+1
        ligne=1
        Liste_global[j][1]=ligne
        colonne=2*i+2
        Liste_global[j][2]=colonne
        Hexagone(x,y)

    for i in range(0,4):
        x=decal_droite+L+2*L*i
        y=decal_bas+3*h
        j=j+1
        Liste_global[j][0]=j+1
        ligne=2
        Liste_global[j][1]=ligne
        colonne=2*i+1
        Liste_global[j][2]=colonne
        Hexagone(x,y)
    
    for i in range(0,5):
        x=decal_droite+2*L*i
        y=decal_bas+6*h
        j=j+1
        Liste_global[j][0]=j+1
        ligne=3
        Liste_global[j][1]=ligne
        colonne=2*i
        Liste_global[j][2]=colonne
        Hexagone(x,y)

    for i in range(0,4):
        x=decal_droite+L+2*L*i
        y=decal_bas+9*h
        j=j+1
        Liste_global[j][0]=j+1
        ligne=4
        Liste_global[j][1]=ligne
        colonne=2*i+1
        Liste_global[j][2]=colonne
        Hexagone(x,y)
    
    for i in range(0,3):
        x=decal_droite+2*L+2*L*i
        y=decal_bas+12*h
        j=j+1
        Liste_global[j][0]=j+1    
        ligne=5
        Liste_global[j][1]=ligne
        colonne=2*i+2
        Liste_global[j][2]=colonne
        Hexagone(x,y)

    Aleatoire()                      
    
    Fenetre_Jeu.mainloop()    
        #############################################
# Fenetre d'acceuil #
Fenetre = Tk()

Fenetre.attributes('-fullscreen',1)
Fenetre.title("HexaNumber")

Largeur = Fenetre.winfo_screenwidth()
Hauteur = Fenetre.winfo_screenheight()

Image_Accueil=PhotoImage(file='Image_Accueil.gif')

Canvas_principale = Canvas(Fenetre,width=Largeur,height=Hauteur,bg = "black")
Canvas_principale.pack()
imagefond=Canvas_principale.create_image(Largeur/2,Hauteur/2,image=Image_Accueil)
Canvas_principale.create_text(Largeur/2,(Hauteur)*(1/3),text = "HEXANUMBER", font = "Arial 72 bold", fill = "white")

bou_Quitter = Button(Fenetre, text='        QUITTER        ', command=Fenetre.destroy, relief='flat', bg = 'black', fg = 'white')
bou_Quitter.place(height=50, width=150, x=Largeur/2-75,y=Hauteur-150)

bou_Regles = Button(Fenetre, text='         REGLES        ',command= Regles, relief='flat', bg = 'black', fg = 'white')
bou_Regles.place(height=50, width=150, x=Largeur/2-75,y=Hauteur-220)

bou_Jouer = Button(Fenetre, text='         JOUER         ', command=Jeu, relief='flat', bg = 'black', fg = 'white')
bou_Jouer.place(height=50, width=150, x=Largeur/2-75,y=Hauteur-290)
# Liste contenant toute les couleurs des cases
Couleur = ['white','khaki','yellow','darkorange','red','Crimson','pink','hotpink','mediumvioletred','mediumblue','dodgerblue','skyblue','turquoise','darkcyan','olivedrab','yellowgreen','green','chocolate','saddlebrown','dimgray']

Fenetre.mainloop()
