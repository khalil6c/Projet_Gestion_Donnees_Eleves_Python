
def est_numero_valide(numero):
    
    if len(numero) != 7:
        return False
    for c in numero:
        if not c.isdigit() and not c.isupper():
            return False
    return True
#print(est_numero_valide("2014079LH"))

def est_prenom_valide(prenom):
    
    if len(prenom) < 3:
        return False
    if not prenom[0].isalpha():
        return False
    return True


def est_nom_valide(nom):
    
    if len(nom) < 2:
        return False
    if not nom[0].isalpha():
        return False
    return True


def est_date_valide(date_str):
    month_str=''
    day_str=''
    day=0
    month=0
    year=0
    mois_en_nombre = {
        "janvier": "01",
        "février": "02",
         "fev":"02",
        "fevrier":"02",
        "mars": "03",
        "avril": "04",
        "mai": "05",
        "juin": "06",
        "juillet": "07",
        "août": "08",
        "septembre": "09",
        "octobre": "10",
        "novembre": "11",
        "decembre": "12",
        "décembre": "12"
    } 
     
    # On divise la chaîne en trois parties : le jour, le mois et l'année
    if len(date_str)==0:
        return False
    if date_str.count('/') > 2 :
        return False
    if date_str.count('/')==2 :
        day_str, month_str, year_str = date_str.split("/")
        
    for mois in mois_en_nombre.keys():
        if   month_str==mois :
            month_str=mois_en_nombre[month_str.lower()]
    # On essaie de convertir les parties en entiers
    try:
        day = int(day_str)
        month = int(month_str)
        year = int(year_str)
    except ValueError:
        # Si la conversion échoue, c'est que la chaîne n'est pas au bon format
        #return "date invalid",False
        return False
    # On vérifie que le jour, le mois et l'année sont valides
    if day < 1 or day > 31 or month < 1 or month > 12 or year < 1:
        return False
    
    # On vérifie que le mois a le bon nombre de jours
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            # Année bissextile
            if day > 29:
                return False
        else:
            # Année non bissextile
            if day > 28:
                return False
    
    # Si toutes les vérifications ont réussi, la date est valide
    return True
  

def est_classe_valide(classe) :
    
    if not  (classe[0] in ['6','5','4','3'] and classe[-1] in ["A","B"]) :
        return False
    else :
        return True    
    #return False

# #Cettte fonction prend en argument une liste de notes
def notes_devoir_valides(notes):
    
    note_float=0.0
    if len(notes)==0 :
        return False
    
    for note in notes:
        try:
            note_float = float(note)
        except ValueError:
            return False
        if note_float < 0 or note_float > 20:
            return False
    return True
#verifier_notes(['11','12'])
##################################################
def note_examen_valide(notes):
    note_float=0.0
    if len(notes)==0 :
        return False
    
    for note in notes:
        try:
            note_float = float(note)
        except ValueError:
            return False
        if note_float < 0 or note_float > 20:
            return False
    return True
