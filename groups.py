# COMMENTEZ CHAQUE LIGNE DE CE SCRIPT EN EXPLIQUANT CE QU'ELLE FAIT ET POURQUOI

# EXPLIQUEZ CE QUE FAIT RANDOM.SAMPLE ET LES ALTERNATIVES QUI EXISTENT EN CHERCHANT SUR INTERNET

# EXPLIQUEZ LE %S DU PRINT, QUELS SONT LES AUTRES POSSIBILITES

# EXPLIQUEZ LE BUT DE CE SCRIPT

# CORRIGEZ LES ERREURS CE SCRIPT

# RAJOUTER AU SCRIPT UNE PARTIE QUI AFFICHE TOUS LES NOMS

# FAITES EN SORTE QUE LE RESULTAT RESSEMBLE A
    # GROUP #1:  ['nameX', 'nameX']
    # GROUP #2:  ['nameX', 'nameX']
    # GROUP #3:  ['nameX', 'nameX']
    
# MODIFIEZ LE PRINT POUR REVENIR A LA LIGNE AVANT D'AFFICHER LES GROUPES

# MODIFIEZ LE SCRIPT POUR SELECTIONNER UN A UN LES MEMBRES DE LA LISTE "selected"

# MODIFIEZ LE SCRIPT PRECEDANT POUR OBTENIR LE MEME FONCTIONNEMENT SANS AVOIR A DETERMINER LE NOMBRE DE GROUPES
# INDICE: TOUT SE PASSE SUR LA LISTE NAMES
# INDICE: PENSER A WHILE

# TRANSPOSER CE CODE DANS UN FICHIER .PY ET TROUVER COMMENT L'EXECUTER DEPUIS UN TERMINAL

import random
import logging
import datetime
import json

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log_format = '%(asctime)s %(filename)s: %(message)s'
logging.basicConfig(filename="test.log", format=log_format,
                    datefmt='%Y-%m-%d %H:%M:%S' )

logger.info("import library")
 
with open('./name.txt', 'r') as f:
    logging.info("Script started")
    print(datetime.datetime.now(), ":")
    names = f.read().split()
    print(names)
print(names)


nb_groups = 3

logging.info("ask user to enter number group")
nbr_per_group = int(input('Choississez le nombre de personnes par groupe : '))
logging.info("ask number from user")
while len(names) >= nbr_per_group:
    selected = random.sample(names, nbr_per_group)
    logging.info("select in names random group")
    print("\n GROUP : %s" %  (selected))
    for sel in selected:
        names.remove(sel)

print("il reste=", names)

logging.info("add group in json file")
with open('group.json', 'w', encoding='utf_8') as f:
    json.dump(selected, f, ensure_ascii=False, indent=4)

logging.info("Script ended !")