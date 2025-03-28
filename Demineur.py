import random
import pygame
import time

def demineur (largeur, hauteur):

    nbr_mine = largeur * hauteur // 5

    def creation_grille(largeur, hauteur) :

        # Création grille
        grille = [0] * hauteur
        for i in range (hauteur):
            grille[i] = [0] * largeur
        for ligne in range (hauteur):
            for colonne in range (largeur):
                grille[ligne][colonne] = [0] * 4

        # Remplissage des coordonnées des cases
        for ligne in range (hauteur):
            for colonne in range (largeur):
                grille[ligne][colonne][2] = [0] * 2
                grille[ligne][colonne][2][0] = ligne
                grille[ligne][colonne][2][1] = colonne

        # Remplissage des coordonnées des cases se trouvant autour des cases
        for ligne in range (hauteur):
            for colonne in range (largeur):
                if ligne == 0 and colonne == 0 :
                    grille[ligne][colonne][3] = [[grille[ligne  ][colonne+1][2][0],grille[ligne  ][colonne+1][2][1]],
                                                 [grille[ligne+1][colonne  ][2][0],grille[ligne+1][colonne  ][2][1]],
                                                 [grille[ligne+1][colonne+1][2][0],grille[ligne+1][colonne+1][2][1]]]
                elif ligne == 0 and colonne == largeur - 1 :
                    grille[ligne][colonne][3] = [[grille[ligne  ][colonne-1][2][0],grille[ligne  ][colonne-1][2][1]],
                                                 [grille[ligne+1][colonne-1][2][0],grille[ligne+1][colonne-1][2][1]],
                                                 [grille[ligne+1][colonne  ][2][0],grille[ligne+1][colonne  ][2][1]]]
                elif ligne == hauteur - 1 and colonne == 0 :
                    grille[ligne][colonne][3] = [[grille[ligne-1][colonne  ][2][0],grille[ligne-1][colonne  ][2][1]],
                                                 [grille[ligne-1][colonne+1][2][0],grille[ligne-1][colonne+1][2][1]],
                                                 [grille[ligne  ][colonne+1][2][0],grille[ligne  ][colonne+1][2][1]]]
                elif ligne == hauteur - 1 and colonne == largeur - 1 :
                    grille[ligne][colonne][3] = [[grille[ligne-1][colonne-1][2][0],grille[ligne-1][colonne-1][2][1]],
                                                 [grille[ligne-1][colonne  ][2][0],grille[ligne-1][colonne  ][2][1]],
                                                 [grille[ligne  ][colonne-1][2][0],grille[ligne  ][colonne-1][2][1]]]
                elif ligne == 0 :
                    grille[ligne][colonne][3] = [[grille[ligne  ][colonne-1][2][0],grille[ligne  ][colonne-1][2][1]],
                                                 [grille[ligne  ][colonne+1][2][0],grille[ligne  ][colonne+1][2][1]],
                                                 [grille[ligne+1][colonne-1][2][0],grille[ligne+1][colonne-1][2][1]],
                                                 [grille[ligne+1][colonne  ][2][0],grille[ligne+1][colonne  ][2][1]],
                                                 [grille[ligne+1][colonne+1][2][0],grille[ligne+1][colonne+1][2][1]]]
                elif ligne == hauteur - 1 :
                    grille[ligne][colonne][3] = [[grille[ligne-1][colonne-1][2][0],grille[ligne-1][colonne-1][2][1]],
                                                 [grille[ligne-1][colonne  ][2][0],grille[ligne-1][colonne  ][2][1]],
                                                 [grille[ligne-1][colonne+1][2][0],grille[ligne-1][colonne+1][2][1]],
                                                 [grille[ligne  ][colonne-1][2][0],grille[ligne  ][colonne-1][2][1]],
                                                 [grille[ligne  ][colonne+1][2][0],grille[ligne  ][colonne+1][2][1]]]
                elif colonne == 0 :
                    grille[ligne][colonne][3] = [[grille[ligne-1][colonne  ][2][0],grille[ligne-1][colonne  ][2][1]],
                                                 [grille[ligne-1][colonne+1][2][0],grille[ligne-1][colonne+1][2][1]],
                                                 [grille[ligne  ][colonne+1][2][0],grille[ligne  ][colonne+1][2][1]],
                                                 [grille[ligne+1][colonne  ][2][0],grille[ligne+1][colonne  ][2][1]],
                                                 [grille[ligne+1][colonne+1][2][0],grille[ligne+1][colonne+1][2][1]]]
                elif colonne == largeur - 1 :
                    grille[ligne][colonne][3] = [[grille[ligne-1][colonne-1][2][0],grille[ligne-1][colonne-1][2][1]],
                                                 [grille[ligne-1][colonne  ][2][0],grille[ligne-1][colonne  ][2][1]],
                                                 [grille[ligne  ][colonne-1][2][0],grille[ligne  ][colonne-1][2][1]],
                                                 [grille[ligne+1][colonne-1][2][0],grille[ligne+1][colonne-1][2][1]],
                                                 [grille[ligne+1][colonne  ][2][0],grille[ligne+1][colonne  ][2][1]]]
                else :
                    grille[ligne][colonne][3] = [[grille[ligne-1][colonne-1][2][0],grille[ligne-1][colonne-1][2][1]],
                                                 [grille[ligne-1][colonne  ][2][0],grille[ligne-1][colonne  ][2][1]],
                                                 [grille[ligne-1][colonne+1][2][0],grille[ligne-1][colonne+1][2][1]],
                                                 [grille[ligne  ][colonne-1][2][0],grille[ligne  ][colonne-1][2][1]],
                                                 [grille[ligne  ][colonne+1][2][0],grille[ligne  ][colonne+1][2][1]],
                                                 [grille[ligne+1][colonne-1][2][0],grille[ligne+1][colonne-1][2][1]],
                                                 [grille[ligne+1][colonne  ][2][0],grille[ligne+1][colonne  ][2][1]],
                                                 [grille[ligne+1][colonne+1][2][0],grille[ligne+1][colonne+1][2][1]]]

        # Remplissage des bombes
        nbr_mine = largeur * hauteur // 5
        mine = nbr_mine
        vide = largeur * hauteur - nbr_mine
        for ligne in range (hauteur):
            for colonne in range (largeur):
                remplissage = [0] * (mine + vide)
                for i in range (mine):
                    remplissage[i] = "b"
                nbr_selectionne = random.choice(remplissage)
                grille[ligne][colonne][0] = nbr_selectionne
                if nbr_selectionne == "b" :
                    mine -= 1
                else :
                    vide -= 1

        # Remplissage des cases prévenant des bombes
        compteur = 0
        for ligne in range (hauteur):
            for colonne in range (largeur):
                if grille[ligne][colonne][0] == 0 :
                    for i in range (len(grille[ligne][colonne][3])):
                        if grille[grille[ligne][colonne][3][i][0]][grille[ligne][colonne][3][i][1]][0] == 'b' :
                            compteur += 1
                    grille[ligne][colonne][0] = compteur
                    compteur = 0

        return grille

    grille = creation_grille(largeur, hauteur)

    def cases_autour_des_cases_vides(grille) :

        continuer = 1
        while continuer == 1 :
            continuer = 0
            for ligne1 in range (len(grille)) :
                for colonne1 in range (len(grille[0])) :
                    if grille[ligne1][colonne1][0] == 0 and grille[ligne1][colonne1][1] == 1 :
                        for i in range (len(grille[ligne1][colonne1][3])) :
                            if grille[grille[ligne1][colonne1][3][i][0]][grille[ligne1][colonne1][3][i][1]][1] == 0 :

                                continuer = 1

                                case = grille[grille[ligne1][colonne1][3][i][0]][grille[ligne1][colonne1][3][i][1]][0]

                                couleur_ecriture = (0,0,0)
                                if case == 0 :
                                    couleur = (150,150,150)
                                    couleur_ecriture = (150,150,150)
                                elif case == 1 :
                                    couleur = (255,255,0)
                                elif case == 2 :
                                    couleur = (255,170,0)
                                elif case == 3 :
                                    couleur = (255,85,0)
                                elif case == 4 :
                                    couleur = (255,0,0)
                                elif case == 5 :
                                    couleur = (255,0,170)
                                elif case == 6 :
                                    couleur = (128,0,255)
                                elif case == 7 :
                                    couleur = (0,0,255)
                                elif case == 8 :
                                    couleur = (0,255,0)

                                pygame.draw.rect(plateau, couleur, (grille[ligne1][colonne1][3][i][1] * taille_cases + 250, grille[ligne1][colonne1][3][i][0] * taille_cases, taille_cases, taille_cases))

                                a = pygame.font.SysFont('Arial', int(taille_cases))
                                a = a.render(str(case), 1, couleur_ecriture)
                                plateau.blit(a, (grille[ligne1][colonne1][3][i][1] * taille_cases + taille_cases // 3 + 250, grille[ligne1][colonne1][3][i][0] * taille_cases - taille_cases // 10))

                                grille[grille[ligne1][colonne1][3][i][0]][grille[ligne1][colonne1][3][i][1]][1] = 1

    def solution(grille, taille_cases) :
        for i in range (len(grille)) :
            for j in range (len(grille[0])) :
                if grille[i][j][1] == 0 :
                    if grille[i][j][0] == "b" :
                        button = 3
                    else :
                        button = 1
                    cliquee(grille, button, (j*taille_cases,i*taille_cases), taille_cases)
                    grille[i][j][1] = 0
                    if grille[i][j][0] == "b" :
                        grille[i][j][1] = 1

    def cliquee(grille, event_button, event_pos, taille_cases) :

        ligne_c = event_pos[1] // taille_cases
        colonne_c = event_pos[0] // taille_cases
        case = grille[ligne_c][colonne_c][0]

        # Permet de mettre ou d'enlever des bombes avec le clic droit
        if event_button == 3 :

            if grille[ligne_c][colonne_c][1] == 0 :

                a = pygame.font.SysFont('Arial', int(taille_cases))
                a = a.render("b", 1, (255,0,0))
                plateau.blit(a, (colonne_c * taille_cases + taille_cases // 3 + 250, ligne_c * taille_cases - taille_cases // 10))

                if grille[ligne_c][colonne_c][0] == "b" :
                    grille[ligne_c][colonne_c][1] = 1
                else :
                    grille[ligne_c][colonne_c][1] = -1

            elif grille[ligne_c][colonne_c][1] == -1 or (grille[ligne_c][colonne_c][1] == 1 and grille[ligne_c][colonne_c][0] == "b") :

                pygame.draw.rect(plateau, (250,250,250), (colonne_c * taille_cases + 250, ligne_c * taille_cases, taille_cases, taille_cases))

                grille[ligne_c][colonne_c][1] = 0

        # Dévoile la case avec le clic gauche
        elif event_button == 1 :

            # Dévoile toutes les cases se trouvant autour lorsque la case est déja révélé
            if time.time() - coup_precedent[1] < 0.3 and coup_precedent[0] == [colonne_c,ligne_c] and grille[ligne_c][colonne_c][1] == 1 :
                for i in range (len(grille[ligne_c][colonne_c][3])) :
                    if grille[grille[ligne_c][colonne_c][3][i][0]][grille[ligne_c][colonne_c][3][i][1]][1] == 0 :
                        cliquee(grille, 1, (grille[ligne_c][colonne_c][3][i][1] * taille_cases, grille[ligne_c][colonne_c][3][i][0] * taille_cases), taille_cases)
                        grille[grille[ligne_c][colonne_c][3][i][0]][grille[ligne_c][colonne_c][3][i][1]][1] = 1

            couleur_ecriture = (0,0,0)
            grille[ligne_c][colonne_c][1] = 1
            if case == "b" :
                grille[ligne_c][colonne_c][1] = 0
                couleur = (255,0,0)
                a = pygame.font.SysFont('Arial', int(taille_cases))
                a = a.render("b", 1, (255,0,0))
                plateau.blit(a, (colonne_c * taille_cases + taille_cases // 3 + 250, ligne_c * taille_cases - taille_cases // 10))
                a = pygame.font.SysFont('Arial', 150)
                a = a.render("Dommage...", 5, (255,0,0))
                plateau.blit(a, (340,200))
                return

            elif case == 0 :
                couleur = (150,150,150)
                couleur_ecriture = (150,150,150)

                cases_autour_des_cases_vides(grille)

            elif case == 1 :
                couleur = (255,255,0)
            elif case == 2 :
                couleur = (255,170,0)
            elif case == 3 :
                couleur = (255,85,0)
            elif case == 4 :
                couleur = (255,0,0)
            elif case == 5 :
                couleur = (255,0,170)
            elif case == 6 :
                couleur = (128,0,255)
            elif case == 7 :
                couleur = (0,0,255)
            elif case == 8 :
                couleur = (0,255,0)

            pygame.draw.rect(plateau, couleur, (colonne_c * taille_cases + 250, ligne_c * taille_cases, taille_cases, taille_cases))

            a = pygame.font.SysFont('Arial', int(taille_cases))
            a = a.render(str(case), 1, couleur_ecriture)
            plateau.blit(a, (colonne_c * taille_cases + taille_cases // 3 + 250, ligne_c * taille_cases - taille_cases // 10))


    # Création de la scène de jeu
    pygame.init()

    taille_cases = 400
    while taille_cases * largeur > 900 :
        taille_cases -= 1
    while taille_cases * hauteur > 700 :
        taille_cases -= 1
    largeur_plateau = taille_cases * largeur
    hauteur_plateau = taille_cases * hauteur
    plateau = pygame.display.set_mode((largeur_plateau + 250, hauteur_plateau))
    plateau.fill((250,250,250))
    pygame.display.flip()

    pygame.display.set_caption("Démineur")

    bon_debut = 0
    coup_precedent = [[0,0],0]

    # Début du jeu
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:

                # Pour les boutons "recommencer"
                if event.pos[0] > 80 and event.pos[1] > 25 and event.pos[0] < 170 and event.pos[1] < 75 :
                    if hauteur > 2 :
                        hauteur -= 1
                    demineur(largeur, hauteur)
                elif event.pos[0] > 30 and event.pos[1] > 75 and event.pos[0] < 80 and event.pos[1] < 165 :
                    if largeur > 2 :
                        largeur -= 1
                    demineur(largeur, hauteur)
                elif event.pos[0] > 80 and event.pos[1] > 75 and event.pos[0] < 170 and event.pos[1] < 165 :
                    demineur(largeur, hauteur)
                elif event.pos[0] > 170 and event.pos[1] > 75 and event.pos[0] < 220 and event.pos[1] < 165 :
                    largeur += 1
                    demineur(largeur, hauteur)
                elif event.pos[0] > 80 and event.pos[1] > 165 and event.pos[0] < 170 and event.pos[1] < 215 :
                    hauteur +=1
                    demineur(largeur, hauteur)
                # Pour le bouton solution
                elif event.pos[0] > 50 and event.pos[1] > 250 and event.pos[0] < 200 and event.pos[1] < 310 :
                    solution(grille, taille_cases)
                # Pour que le premier coup soit sur une case vide
                elif bon_debut == 0 and event.pos[0] > 250 :
                    compteur = 0
                    while grille[event.pos[1] // taille_cases][(event.pos[0] - 250) // taille_cases][0] != 0 and compteur < 100 :
                        grille = creation_grille(largeur, hauteur)
                        compteur += 1
                    bon_debut = 1
                    cliquee(grille, event.button, (event.pos[0] - 250, event.pos[1]), taille_cases)

                elif event.pos[0] > 250 :
                    cliquee(grille, event.button, (event.pos[0] - 250, event.pos[1]), taille_cases)

                coup_precedent = [[(event.pos[0] - 250) // taille_cases, event.pos[1] // taille_cases], time.time()]

                # Indique le nombre de bombes placées
                mine_place = 0
                for i in range (len(grille)) :
                    for j in range (len(grille[0])) :
                        if grille[i][j][0] == "b" and grille[i][j][1] == 1 :
                            mine_place += 1
                pygame.draw.rect(plateau, (250, 250, 250), (0, 325, 250, 70))
                a = pygame.font.SysFont('Arial', 75)
                a = a.render(str(mine_place)+"/" + str(nbr_mine), 5, (0,0,0))
                plateau.blit(a, (55, 315))

                # Test si c'est gagné
                compteur = 0
                for ligne1 in range (len(grille)) :
                    for colonne1 in range (len(grille[0])) :
                        if grille[ligne1][colonne1][1] == 1 :
                            compteur += 1
                if compteur == hauteur * largeur :
                    a = pygame.font.SysFont('Arial', 150)
                    a = a.render("Bien joué !", 5, (0,255,0))
                    plateau.blit(a, (340,60))

        # Trace le quadrillage
        for i in range (largeur) :
            pygame.draw.line(plateau, (0,0,0), (i * taille_cases + 250, 0), (i * taille_cases  + 250, hauteur_plateau), 2)
        for i in range (hauteur) :
            pygame.draw.line(plateau, (0,0,0), (250, (i + 1) * taille_cases), (largeur_plateau + 250, (i + 1) * taille_cases), 2)

        # Affiche les boutons pour recommencer
        pygame.draw.rect(plateau, (100,255,100), (80, 25, 90, 50))
        a = pygame.font.SysFont('Arial', 50)
        a = a.render("-1", 5, (0,0,0))
        plateau.blit(a, (105, 20))

        pygame.draw.rect(plateau, (100,255,100), (30, 75, 50, 90))
        a = pygame.font.SysFont('Arial', 50)
        a = a.render("-1", 5, (0,0,0))
        plateau.blit(a, (36, 90))

        pygame.draw.rect(plateau, (0,255,0), (80, 75, 90, 90))
        a = pygame.font.SysFont('Arial', 15)
        a = a.render("Recommencer", 5, (0,0,0))
        plateau.blit(a, (82, 110))

        pygame.draw.rect(plateau, (0,155,0), (170, 75, 50, 90))
        a = pygame.font.SysFont('Arial', 50)
        a = a.render("+1", 5, (0,0,0))
        plateau.blit(a, (172, 90))

        pygame.draw.rect(plateau, (0,155,0), (80, 165, 90, 50))
        a = pygame.font.SysFont('Arial', 50)
        a = a.render("+1", 5, (0,0,0))
        plateau.blit(a, (102, 160))

        # Affiche le bouton solution
        pygame.draw.rect(plateau, (255, 157, 0), (50, 245, 150, 65))
        a = pygame.font.SysFont('Arial', 48)
        a = a.render("Solution", 5, (0,0,0))
        plateau.blit(a, (53, 249))

        pygame.display.update()

    pygame.quit()
    quit()

demineur(14,12)
