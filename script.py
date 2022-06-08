# 1) Librairies
from PIL import Image
from os import *
from time import *

# 2) Variables Globales
Ext_Img = [".jpg", ".JPG", ".jpeg", ".png", ".PNG"]
Error_Files = []
Nb_Error = 0
List_entiers = [ str(x) for x in range(0, 101) ]
Convert = False
Compres = False

# 3) Main
print("###--- Script Convertisseur d'Images ---###")
print("#- Que souhaitez-vous faire ? ")
print("#- 1 -> Convertir images | 2 -> Compresser images | 3 -> Les deux ")
Choix = input("#- Choix: ")

# Vérification de la validité du choix
while( Choix not in ["1", "2", "3"]):
    print("#- Erreur: choix incorrect")
    Choix = input("#- Choix: ")

if  ( Choix == "1" ):
    Convert = True
elif( Choix == "2" ):
    Compres = True
elif( Choix == "3"):
    Convert = True
    Compres = True

# Extension Image
if(Convert):
    print("##- Conversion Image")
    print("#- Liste des extensions prises en charge:", Ext_Img)
    print("#- Vers quelle extension voulez-vous convertir vos fichiers ? ")
    Ext_cible = "." + input("#- Extension cible: ")

    # Vérification de la validité du format cible
    while( Ext_cible not in Ext_Img):
      print("#- Erreur: format cible non pris en charge")
      Ext_cible = "." + input("#- Extension cible: ")

# Redimensionnement Image
if(Compres):
    print("##- Compression Image")
    print("#- Veuillez saisir la qualité cible (0 à 100)")
    Com_cible = input("#- Compression cible: ")

    # Vérification de la validité du format cible
    while( Com_cible not in List_entiers ):
        print("#- Erreur: Compression cible non prise en charge")
        Com_cible = input("#- Compression cible: ")


# On liste tous les fichiers à convertir
Files = listdir("./avant")
N = len(Files)
count = 0
print( "#- Il y'a", N, "fichiers à modifier." )
sleep(3)

for k in Files:
    # Récupération du nom et de l'extension de chacun des fichiers
    name, extension = path.splitext(k)

    count += 1
    print(f'#- {count}/{N} {name}{extension} ')

    # Vérification de l'extension des fichiers
    if(extension in Ext_Img):
        print('#-- Extension prise en charge, modification en cours... ')

        # Ouverture image en cours
        im = Image.open("./avant/" + name + extension)
        # Conversion de l'image en RGB si elle ne l'est pas
        if not im.mode == 'RGB':
            im = im.convert('RGB')

        # Si on veut convertir l'image
        if(Convert and Compres):
            print("#--- Conversion et compression en cours...")
            im.save("./apres/" + name + Ext_cible, optimize=True, quality=int(Com_cible))
            print("#---- Fichier compressé et converti !")

        # Si on veut convertir l'image
        elif(Convert):
            # Sauvegarde du fichier avec la bonne extension
            print("#--- Conversion en cours...")
            im.save("./apres/" + name + Ext_cible)
            print('#---- Fichier converti !')

        # Si on veut compresser l'image
        elif (Compres):
            # Ouverture image en cours
            print("#--- Compression en cours...")
            im.save("./apres/" + name + extension, optimize=True, quality=int(Com_cible))
            print("#---- Fichier compressé !")

    else:
        Error_Files.append(k)
        Nb_Error += 1
        print("#-- Erreur: extension de fichier non pris en charge!")

tx = round( (1 - (Nb_Error / N)) * 100, 1)
print(f'\n#- Tâche terminée, taux de réussite: {tx}% soit {N-Nb_Error} sur {N} fichiers.')
print(f'#- Liste des fichiers non convertis: {Error_Files}')

#On laisse le terminal ouvert
input()