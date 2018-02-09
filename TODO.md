# TODO

## State

  * initialiser les valeurs à défaut suivant l'équipement donné (avec les paramètres de l'équipement, etc.)
  * créer un bouton "create State" depuis Equipment
  * Lister les états sous Equipment (avec juste les dates et quelques paramètres), puis permettre d'afficher un détail en allant sur la page spécifique d'un State ?
  * Comment enlever le menu "State" dans l'accueil de l'admin ? Idée : ne pas faire de admin.site.register(State), mais créer des URL /state/edit et /state/show pour afficher/éditer les états
  * wizard pour créer un State : 
    * step1: choix de l'équipement (+ bouton "new state" depuis Equipment) et la Date de début (supérieure à la purchase date)
    * step2: affichage des paramètres en fonction du modèle de l'équipement choisi et d'une place (et un code station si la place est accolée)
    * step3 (optionnel): choix d'un canal pour le lier avec (step2 ajouter une coche)
  * Tester l'overlap dans le clean() du Form pour afficher un message d'erreur parlant
  * Migrer DOC d'intervention vers State ? Si oui, que faire d'une doc d'intervention sur une station ? On la lie à quoi ?

## Channel

  * wizard pour créer le canal : 
    * step1: d'abord choisir la station et la date (range), le channel code, le location code et le code Station (à la soumission vérifier que code station existe, et de manière unique)
    * step2: choisir les équipements (afficher 3 (voire plus ?) champs pour choisir un équipement dont le state a un jour été sur une place de cette station en fonction de la date)
    * step3: afficher les states possibles pour ces équipements (dans les dates fournies et qui n'ont pas déjà un lien avec un Channel) => problème car on a 3 channels sur un même équipement. Donc pas possible de bloquer en fonction de ça… (sinon il faudrait 3 State par équipement…)
  * ajouter created\_at, updated\_at + mise à jour de updated\_at en pre\_save chaque fois

## Notebook

  * ajouter l'utilisateur et l'organisme présent à ce moment là (ça peut être que EDF par exemple, ou qu'une personne de l'EOST)

## Intervention

  * Mélange de Notebook et State (il se passe quelque chose au début d'un State, et à la fin) et Channel (comme State)

## Migration

Créer un nouveau script de migration depuis 0 en Django.

  1. Utiliser Django plutôt que Peewee
  2. Adapter pour en faire un "runscript"
  3. Enlever tout ce qui touche à Historique
  4. Adapter les principales fonctions de transitions en Django (celles pour les types d'équipement, les modèles, les stations, les places, les builts, etc.)


## Solution 4 : Timeline

  * faire nettoyage comme prévu : supprimer les triggers, supprimer les historiques, supprimer les interventions, mettre à jour l'interface pour qu'elle fonctionne sans cela.
  * ajouter un champ 'influe sur la réponse instrumentale' coché par défaut sur tous les paramètres des modèles
  * ajouter organisme à Notebook (Station)
  * créer un objet Timeline, avec lien obligatoire vers Equipment. Champs : date, user, equipment_id, paramètre, valeur, note (optionnel)
  * supprimer le champ "parent" sur l'équipement
  * champs sur Équipement : status, storage\_format, clock\_drift, clock\_drift\_unit, adresses IP et Service sont en lecture seule
  * ajouter le champ 'status' pour l'Équipement et laisser l'autre nommé "State". Adapter le formulaire et chercher les répercutions sur le code existant (avec le mot clé State)
  * wizard de modification des paramètres de l'équipement avec toujours date + user. 1/ garder sur l'équipement les dernières valeurs modifiées 2/ enregistrer autant de lignes de Timeline que de paramètres modifiés. IDÉE : inclure ce "wizard" sur Equipement lui-même ? Avec les bons boutons/champs supplémentaires pour valider le formulaire de changement
  * Scinder le wizard "Change equipment parameter" en 2 : d'abord l'utilisateur et la date, puis les paramètres (en prenant les derniers paramètres connus):
    * à l'affichage initial, on doit présenter les dernières valeurs connues
    * si pas de paramètres (dans Timeline), il faudra créer une ligne de Timeline de base, puis la nouvelle valeur
  * Au save d'un Equipment: vérifier si purchase_date a changé. Si oui, changer toutes les lignes de Timeline qui ont cette date avec la nouvelle date.
  * À la création de l'équipement, créer des lignes de Timeline sur les champs spécifiques (avec l'utilisateur courant et la purchase_date comme date)
  * ajouter l'élément State avec les champs place, station_code, dip, azimuth, latitude, longitude, elevation et un champ data contenant "depth" (si Sensor/Hybrid) et les paramètres du modèle à aujourd'hui

  * Channel : 1/ supprimer les champs dip, azimuth, latitude, longitude, elevation, depth, etc. Tout est sur State désormais. 2/ adapter get\_current\_position pour prendre celle du State de type Sensor. 3/ changer start/end en span (pour la plage de dates)

  * créer un wizard de création du State ? (bouton "New State" sur Équipement ?)
  * créer le wizard de création de channels => faut-il propose de choisir simplement les équipements dans la première étape (5 équipements maxi en fonction des dates) et s'occuper automatiquement de prendre les States correspondants et dans l'étape 2 d'afficher les paramètres de ces équipements ?
  * faire l'affichage de Channel avec tous les paramètres confondus (en lecture seule)
  * adapter le wizard 3 channels pour générer les States si besoin, ou encore vérifier si les States existe => à réfléchir
  * adapter le wizard de fermeture de channels
  * créer le Wizard de changement d'un State pour un Channel ? (peut-être juste avoir un bouton "corriger" à côté de chaque équipement)
  * adapter StationXML pour fonctionner (\_get\_obspy\_equipment par exemple)
  * faire l'affichage d'une station pour avoir :
    * la liste des équipements en cours
    * la liste des équipements passés sur cette Station
    * l'historique des modifications (sorte de mélange entre Notebooks Station, Timeline Equipment et Channel)
  * adapter la fonction d'état "state" (ou status ?) d'une Station
  * vérifier qu'au changement de Place d'un Équipement il n'y ait pas de Channel ouvert. Cas échéant : demander à l'utilisateur de fermer le canal. Ce qui devrait mettre une date de fin au State et au canal et créer un nouveau State. Si changement de Place de l'équipement (quand aucun canal ouvert dessus), alors on adapte le State en conséquence (le dernier State, trié par date).
  * Équipement : supprimer la table configuration ? Si oui, le post\_save aussi (add\_configuration) 2/ Si on supprime pas, il faut mettre à jour la Configuration à chaque MàJ du Timeline SI c'est la dernière Timeline…
  * vérifier que Station Map fonctionne encore
  * API : vérifier le paragraphe suivant pour toutes les modifications nécessaires

## Solution 5 : Ajout des paramètres à liste non finie dans les paramètres de l'équipement et Configuration

### Fini

  * Adapter la table Value pour avoir un champ "default" (booléen). Le booléen est par défaut à False.
  * Contrainte sur parameter_id, value dans Value (pour pas avoir 2 fois la même valeur)
  * Vérifier qu'à la création d'un équipement on crée chaque ligne de Configuration avec les paramètres par défaut (add_configuration sûrement)
  * Sur Parameter afficher la liste des Value en Inline, avec le champ "default" pour chaque valeur (pour choisir lequel est par défaut

### À faire

  * Sur Parameter afficher un encart WARNING (comme à l'époque pour les interventions) pour signaler qu'il n'a pas de valeur par défaut et qu'il serait sage d'en ajouter une ?
    * FAIT | créer un champ calculé have\_default\_value
    * utiliser ce champ calculé pour l'affichage du Warning
  * À l'enregistrement du Parameter, signaler à l'utilisateur s'il a plusieurs valeurs par défaut (encart WARNING)
  * Adapter le "Change timeline" de l'équipement pour les paramètres d'un équipement et ses valeurs (toujours avec une date de début et un utilisateur qui a fait la modification)
  * Pour la saisie des paramètres d'un équipement : si qu'une seule ligne (maximum) de Value pour un paramètre donné : le champ est libre pour l'utilisateur. Si plusieurs valeurs : menu déroulant avec les valeurs possibles pour ce paramètre.
  * Ajouter le champ "start" sur Configuration (dans module Equipment). Aussi une note comme sur Timeline ?
  * faire une liste des paramètres qui iront sur les paramètres des équipements désormais : 
    * storage_format
    * clock_drift
    * clock\_drift\_unit
    * sample_rate (datalogger/hybrid)
  * supprimer storage\_format, clock\_drift et clock\_drift\_unit des équipements (ça deviendra des paramètres d'un équipement)
  * supprimer sample_rate de Channel car il devient également un paramètre des équipements : il n'est plus nécessaire dans Channel
  * créer une table de relation entre Channel et Configuration (manytomany sur channel vers Configuration)
  * vérifier contrainte unique sur Station code (unique=True sur code/name)
  * le lien Channel et Paramètre ne se fait QUE sur les paramètres "change_response" = True
  * le wizard de création de Channel fait plutôt référence à la création d'un "Stream" impliquant des équipements, un sample rate (qui définit la première lettre H, L, etc.), un groupement de code (ZNE, ou Z12 ou Z23) et un algorithme particulier pour générer les Channels => demander à Jérôme l'algo pour ce calcul
  * sur Equipment garder l'historique des Place avec quelque chose de similaire à Timeline (table entre Equipment et Place avec un start)
  * on garde lat/long/elevation/depth sur une Place ! Plus besoin sur Channel (on le lit sur la place) ni sur l'équipement ! Et pas besoin d'historique puisqu'on crée une nouvelle Place au besoin. Exemple: une Place en haut du puit, et une place pour le fond du puit.
  * faire une alerte à la création d'un Channel si les équipements choisis ne disposent pas des paramètres obligatoires habituels (dip et azimuth pour Sensor, clock_drift/unit et storage\_format pour Datalogger, etc.) => sûrement dans le Wizard entre deux étapes
  * supprimer l'objet Timeline
  * ajouter un paramètre à l'URL d'équipement pour voyager dans le temps et avoir les infos de cet Équipement à une date donnée
  * rajouter un système pour voyager dans le temps sur l'équipement (une ligne de temps avec les différentes dates et un curseur par exemple)

  * à la migration depuis Gissmo 1.9 : storage\_format, clock\_drift, clock\_drift\_unit devront être crées comme paramètre des équipements qui ont une valeur pour ce champ
  * à la migration depuis Gissmo 1.9 : sample\_rate de Channel devra devenir un paramètre du Datalogger et/ou de l'Hybrid de la chaîne d'acquisition

## API

  * ajouter le champ change_response de Parameter
  * ajouter l'objet "Notebook" de Station (sous le nom station_notebooks ?)
  * créer une API pour Channel qui mette à disposition les bonnes informations : 
    * supprimer channel_config sûrement
    * trouver comment rendre tous les paramètres du canal dans Channel
  * ajouter l'historique des Place pour un Équipement donné
