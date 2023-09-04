import fonctions

with open('Donnees_Projet_Python_DataC5.csv' , 'r') as f:  
        eleves=f.read().split("\n")
        del eleves[0]
Tab_eleve=[]
for eleve in eleves :
        
        e=eleve.split(",")
        try:
                dic_eleves={
                        "Code":e[0],
                        "Numero" :e[1],
                        "Nom":e[2],
                        "Prenom":e[3],
                        "Date_nais":e[4],
                        "Classe":e[5],
                        "Note":e[6]

                }
                Tab_eleve.append(dic_eleves)
        except IndexError:
                ""   
           
#suppression des lignes vides
t=[]
for eleves in Tab_eleve :
       if not eleves['Nom']==''  :
          t.append(eleves)  

#Changer format date 
for i in range(len(t)) :
        t[i]["Date_nais"]=t[i]["Date_nais"].lstrip()
        for char in t[i]["Date_nais"] :
                if char in ['-',',',':','_','|','.',' '] :
                        t[i]['Date_nais']=t[i]['Date_nais'].replace(char,"/")
                        
        #print(t[i]["Date_nais"])
#Changer format Classe
for i in range(len(t)):        
        t[i]["Classe"]=t[i]["Classe"].replace(' ','')
        t[i]["Classe"]=t[i]["Classe"][0]+ "em" +t[i]["Classe"][-1].capitalize() 
             

#Recuperation des notes dans un dictionnnaire      
for i in range(len(t)) :
        m=t[i]["Note"].split("#")
        del t[i]["Note"]
        dic_matieres={}
        t[i]["matieres"]={}
        for j in  m :
                j=j.replace("[","-").replace("|","-").replace(":","-").replace("]","-").split("-")
                try:
                       dic_matieres[j[0]]={
                        "Devoir":j[1:-2],
                        "Examen":j[-2]
                       }
                       #print(dic_matieres) 
                       t[i]["matieres"].update(dic_matieres)
                       #print(t[i])       
                        #T.append(dic_matieres)
                       
                except IndexError:
                 ""  

tableau_valide = []
tableau_invalide = []

#Boucle à travers chaque ligne d'élève
for eleve in t:
    numero = eleve['Numero']
    nom=eleve['Nom']
    prenom=eleve['Prenom']
    date_nais=eleve['Date_nais']
    classe=eleve['Classe']
    est_valide = True
    erreur={}

    # Vérifie si le code est valide
    if not fonctions.est_numero_valide(numero):
        #print(f"Le code {code} est invalide car il ne commence pas par un chiffre")
        erreur['numero']= f"Le numero {numero} est invalide "
        est_valide = False

    # Vérifie si le numéro est valide
    if not fonctions.est_prenom_valide(prenom):
        erreur['prenom']= f"Le prenom {prenom} est invalide "
        est_valide = False
    if not fonctions.est_nom_valide(nom):
        erreur['nom']= f"Le nom {nom} est invalide "
        est_valide = False  
    if not fonctions.est_date_valide(date_nais):
        erreur['date_nais']= f"La date {date_nais} est invalide "
        est_valide = False 
    if not fonctions.est_classe_valide(classe):
        erreur['classe']= f"La classe {classe} est invalide "
        est_valide = False  
    for mat in eleve['matieres'] :
          devoir=eleve['matieres'][str(mat)]['Devoir']
          examen=eleve['matieres'][str(mat)]['Examen']
          if not fonctions.notes_devoir_valides(devoir) :
                erreur['devoir']= f"La note de devoir {devoir} est invalide "
                est_valide = False 
          if not fonctions.note_examen_valide(examen) :
                erreur['examen']= f"La note d'examen {examen} est invalide "
                est_valide = False       

    eleve["erreur"]=erreur
    # Ajoute la ligne d'élève au tableau valide ou invalide
    if est_valide:
        tableau_valide.append(eleve)
    else:
        tableau_invalide.append(eleve)

#################################################
#Calcul de la moyenne par matiere 
for eleve in tableau_valide :
        for matiere, notes in eleve['matieres'].items():
                moyenne_matiere = (sum(int(note) for note in notes['Devoir'])/len(notes['Devoir']) + 2*int(notes['Examen']))/3
                moyenne_matiere=round(moyenne_matiere,2)
                eleve['matieres'][matiere]['Moyenne_matieres'] = moyenne_matiere
# Calcul de la moyenne générale
        moyenne_generale = sum([matiere['Moyenne_matieres'] for matiere in eleve['matieres'].values()])/len(eleve['matieres'])
        moyenne_generale=round(moyenne_generale,2)
# Ajout de la moyenne générale dans le dictionnaire
        eleve['Moyenne_generale'] = moyenne_generale

def afficher_info(tableau_valide):
    if tableau_valide:
        
        print("| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |".format("Numero", "Nom", "Prenom", "Date_nais", "Classe"))
        for eleve in tableau_valide :
                # Affichage de la deuxième ligne du tableau
                print("| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |".format(eleve['Numero'], eleve['Nom'], eleve['Prenom'], eleve['Date_nais'], eleve['Classe']))

    else:
        print("|  {:^10}  |  {:^10}  |  {:^10}  |  {:^10}  |  {:^10}  |".format("Numero", "Nom", "Prenom", "Date_nais", "Classe"))

        for e in tableau_invalide :
                
                # Affichage de la deuxième ligne du tableau
                print("|  {:^10}  |  {:^10}  |  {:^10}  |  {:^10}  |  {:^10}  |".format(e['Numero'], e['Nom'], e['Prenom'], e['Date_nais'], e['Classe']))

        
        
def afficher_cinq_premiers(tableau_valide):
    print("Cinq premiers élèves :")
    print("| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |".format("Numero", "Nom", "Prenom", "Date_nais", "Classe"))
    for eleve in tableau_valide[:5]:
        print("| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |".format(eleve['Numero'], eleve['Nom'], eleve['Prenom'], eleve['Date_nais'], eleve['Classe']))
 ################################################
def afficher_par_numero(tableau_valide,numero) :   
    #T=[{'nom':'CISSE','prenom':'ABDOU'},{'nom':'DIOP','prenom':'ISSA'}]
    #nom_recherche = input("Entrez le nom à rechercher : ")
    print("| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |".format("Numero", "Nom", "Prenom", "Date_nais", "Classe"))
    for eleve in tableau_valide:
        if eleve['Numero'] == numero :
            print("| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |".format(eleve['Numero'], eleve['Nom'], eleve['Prenom'], eleve['Date_nais'], eleve['Classe']))
            break
    else:
        print(f"Le numéro {numero} n'a pas été trouvé.")

 ###########################################                   
        
def ajouter_infos(tableau_valide,numero, nom, prenom,date_nais,classe):    
    #Ajoute un nouvel élément à la liste sous la forme d'un dictionnaire contenant un nom et un prénom.
    nouvel_element = {'Numero':numero,'Nom': nom, 'Prenom': prenom,'Date_nais':date_nais,'Classe':classe}
    if fonctions.est_numero_valide(numero) and fonctions.est_prenom_valide(prenom) and fonctions.est_date_valide(date_nais) and fonctions.est_classe_valide(classe):
        tableau_valide.append(nouvel_element)
        print("Les informations ont été ajoutées avec succès.")
    else :
         print("Veuillez donner des informations exactes")   

    
def modifier_info_invalide(numero, nouvelles_infos, tableau_valide, tableau_invalide):
    if tableau_invalide and tableau_invalide['Numero'] == numero:
        # TODO : Vérifier la validité des nouvelles informations
        tableau_invalide.update(nouvelles_infos)
        tableau_valide.append(tableau_invalide)
        print("Les informations ont été mises à jour et déplacées dans les informations valides.")
    elif tableau_valide and tableau_valide['Numero'] == numero:
        print("Les informations pour ce numéro sont valides. Utilisez l'option 'Ajouter' pour ajouter des informations supplémentaires.")
    else:
        print(f"Le numéro {numero} n'a pas été trouvé.")
        
def paginate(data, page_size):
    # Divise les données en pages de la taille spécifiée
    return [data[i:i+page_size] for i in range(0, len(data), page_size)]
def paginate_par_5(data, page_size=5):
    # Divise les données en pages de la taille spécifiée
    return [data[i:i+ page_size] for i in range(0, len(data), page_size)]
while True:
    print("Menu :")
    print("1. Afficher les informations")
    print("2. Afficher une information par son numéro")
    print("3. Afficher les cinq premiers")
    print("4. Ajouter une information")
    print("5. Modifier une information invalide")
    print("6. Paginer par 5 lignes")
    print("7. Choisir le nombre de ligne a paginer")
    print("8. Quitter")
    
    choix = str(input("Entrez votre choix : "))
    
    if choix == '1':
        vi=input("Veuillez saisir a pour les infos valides et b pour les infos invalides : ")
        if vi=='a':
                afficher_info(tableau_valide)
        elif vi=='b':
                afficher_info(tableau_invalide)  
        else :
                print("Veuillez choisir entre a et b")                      

    elif choix == '2':
        numero = input("Entrez le numéro de l'élève : ")
        afficher_par_numero(tableau_valide,numero) 
        
    elif choix == '3':
        afficher_cinq_premiers(tableau_valide)
    elif choix == '4':
        #infos = {} # remplir avec les nouvelles informations
        numero=input("Entrer le numero de l'eleve : ")
        nom=input("Entrer le nom de l'eleve : ")
        prenom=input("Entrer le prenom de l'eleve : ")
        date_nais=input("Entrer la date  de naissance de l'eleve : ")
        ajouter_infos(tableau_valide,numero, nom, prenom,date_nais,classe)
    elif choix == '5':
        numero = input("Entrez le numéro de l'élève : ")
        nouvelles_infos = {} # remplir avec les nouvelles informations
        modifier_info_invalide(numero, nouvelles_infos, tableau_valide, tableau_invalide)
    elif choix=='6' :

    # Divise les données en pages
        pages = paginate_par_5(tableau_valide, 5)

    # Affiche chaque page
        for i, page in enumerate(pages):
            print(" ")
            print(f"Page {i+1}")
            print("| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |".format("Numero", "Nom", "Prenom", "Date_nais", "Classe"))
            for eleve in page:
                #print(item)
                print("| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |".format(eleve['Numero'], eleve['Nom'], eleve['Prenom'], eleve['Date_nais'], eleve['Classe']))
                
    elif choix=='7' :
    # Demande à l'utilisateur la taille de la pagination
        page_size = int(input("Entrez le nombre de lignes par page : "))

    # Divise les données en pages
        pages = paginate(tableau_valide, page_size)

    # Affiche chaque page
        for i, page in enumerate(pages):
            print(f"Page {i+1}")
            print(" ")
            print("| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |".format("Numero", "Nom", "Prenom", "Date_nais", "Classe"))
            for eleve in page:
                #print(item)
                print("| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |6".format(eleve['Numero'], eleve['Nom'], eleve['Prenom'], eleve['Date_nais'], eleve['Classe']))

          
    elif choix == '8':
        break
    else:
        print("Choix invalide. Veuillez réessayer.")

