# TODO

## Status

  * Mettre les Status en dur (liste prédéfinie). Savoir que "New" est celui par défaut. Et que Failure et Broken sont ceux qui mettent une Station en état Failure.

## StationXML

  * adapter StationXML pour fonctionner (\_get\_obspy\_equipment par exemple)

## Wizard Channel

  * Ajouter le user comme paramètre du Wizard Channel pour garder QUI a crée le Channel (et qui a choisi les paramètres)
  * Changer le nom du champ "Code format" en "orientation format"
  * Le "location code" n'est pas modifiable sur les 3 channels
  * À la place de Filter, pour chaque channel il faut pouvoir modifier des paramètres qui sont marqués spécialement (un booléen à False par défaut sur le Paramètre)
  * Wizard channel : create links between Channels and configuration from given equipments
  * le lien Channel et Paramètre ne se fait QUE sur les paramètres "change\_response" = True
  * Channel wizard : afficher un récapitulatif avec les paramètres de chaque équipement et finalement on valide tout ça.
  * Dans wizard Channel : ne pas permettre d'ajouter des Channels à une date où les équipements sont sur une Place qui a une date de fin qui ne correspond pas !
  * Le dip est entre -90 et 90 => adapter le code qui donne le triplet

## Channel

  * ajouter created\_at, updated\_at + mise à jour de updated\_at en pre\_save chaque fois
  * Tester l'overlap entre 2 canaux à la création (span\_\_overlap avec un filtrage sur d'autres champs comme network, location code, station, code) dans un pre\_save probablement (Cf. le check\_overlap() de Timeline)
  * Channel change form: Permettre d'aller sur la page de chaque équipement
  * Channel change form: Permettre d'aller sur les places du channel ?
  * faire l'affichage de Channel avec tous les paramètres confondus (en lecture seule)
  * dans Channel Configuration, il faudrait faire un pre-save pour REFUSER les paramètres qui sont différent d'un impact = 2 !!!
  * Afficher correctement la date (span) dans l'admin
  * Afficher lati/long/elevation de la place du Sensor (ou de l'hybrid)
  * Afficher les paramètres de configuration du canal…

## Notebook

  * ajouter l'utilisateur et l'organisme présent à ce moment là (ça peut être que EDF par exemple, ou qu'une personne de l'EOST)

## Station

  * Station : faire apparaître un bouton "Add Channel" seulement si la station a des équipements. Et si elle n'a pas de date de fin !
  * Adapter Station Map
  * faire l'affichage d'une station pour avoir :
    * la liste des équipements en cours
    * la liste des équipements passés sur cette Station
    * l'historique des modifications (sorte de mélange entre Notebooks Station, Timeline Equipment et Channel)
  * adapter la fonction d'état "state" (ou status ?) d'une Station
  * Ne PAS permettre la modification des places de la station : LECTURE SEULE

## Place

  * Hériter de lat/long/elevation de la station quand on crée la Place ? (si une station est donnée)
  * EquipmentInline doit être en Readonly (et ne laisser que le bouton EDIT)
  * Place : rendre la date de début obligatoire ?
  * Place : ajouter une date de fin
  * on garde lat/long/elevation/depth sur une Place ! Plus besoin sur Channel (on le lit sur la place) ni sur l'équipement ! Et pas besoin d'historique des lat/long/elev. puisqu'on crée une nouvelle Place au besoin. Exemple: une Place en haut du puit, et une place pour le fond du puit. Et qu'une Place ne devrait pas se déplacer de toute manière. Même si c'est le cas, on crée une nouvelle Place ^_^
  * Gestion de l'historique des Place => soit on fait quelque chose à part, soit on l'ajoute dans "Configure". Mais à ce moment là il faudrait aussi un utilisateur et une date !

## Equipment

  * Move equipment : ne PAS proposer les paramètres d'Impact = 2 dans la liste !
  * Move equipment : ne pas autoriser de date supérieure à aujourd'hui!
  * Equipment : comment modifier des valeurs a posteriori? Genre les valeurs de la date initiale, etc. ? => toujours afficher les valeurs de la date de l'URL (sinon les dernières). QUESTION : Rendre ces valeurs modifiables uniquement dans l'équipement ou bien dans un objet Configuration ? (plus facile dans un objet Configuration puisqu'il permet de faire des champs adaptés pour chaque paramètre). On peut potentiellement faire les 2 : 1/ on part sur un équipement qui a une configuration et où on peut naviguer entre les dates, on choisit notre équipement, puis 2/ on clique sur un bouton "Edit configuration" pour modifier la configuration
  * WIZARD Equipment : ne PAS afficher les paramètres qui ont un impact de type CHANNEL !
  * WIZARD Equipment : ne PAS permettre la modification des paramètres qui ont une influence sur la réponse instrumentale SI un channel est lié (vérifier en fonction de la date donnée aussi)
  * ajouter un paramètre à l'URL d'équipement pour voyager dans le temps et avoir les infos de cet Équipement à une date donnée
  * rajouter un système pour voyager dans le temps sur l'équipement (une ligne de temps avec les différentes dates et un curseur par exemple)
  * Sur equipment adapter le bouton "Station" pour qu'il renvoie vers la BONNE station de l'équipement (suivant l'URL et la date saisie dans l'URL)
  * Equipment : Faire un message d'erreur pour le changement d'une place SI une channel est acollée pour cette date donnée
  * Equipment : faire un bouton History pour voir la liste des modifications. On donne un champ "début" (obligatoire), un champ "fin" (non obligatoire), on valide : ça donne l'historique entre ces dates ou bien depuis la première date à aujourd'hui
  * vérifier qu'au changement de Place d'un Équipement il n'y ait pas de Channel ouvert. Cas échéant : demander à l'utilisateur de fermer le canal. Ce qui devrait mettre une date de fin au State et au canal et créer un nouveau State. Si changement de Place de l'équipement (quand aucun canal ouvert dessus), alors on adapte le State en conséquence (le dernier State, trié par date).
  * Changer le nom du bouton "Station" en "Go to Station" ou similaire (trouver un nom)
  * Wizard Configure : pour les paramètres dip/azimuth, ajouter un help_text qui définit que c'est par rapport au NORD qu'on les définit

## Parameter

  * Parameter : on ne devrait pas pouvoir supprimer DIP/AZIMUTH d'un modèle de type Sensor ou Hybrid ! Sinon ça casserait les configurations et les channels (pour le calcul)
  * Parameter : une valeur par défaut EST obligatoire ! Faire du Javascript ou trouver un stratagème pour qu'on ait toujours une et une seule valeur par défaut !
  * Parameter : ne pas permettre de prendre DEUX valeurs par défaut. Toujours une. Obligatoire
  * Sur Parameter afficher un encart WARNING (comme à l'époque pour les interventions) pour signaler qu'il n'a pas de valeur par défaut et qu'il serait sage d'en ajouter une ?
    * FAIT | créer un champ calculé have\_default\_value
    * utiliser ce champ calculé pour l'affichage du Warning
  * À l'enregistrement du Parameter, signaler à l'utilisateur s'il a plusieurs valeurs par défaut (encart WARNING)
  * Création automatique de certains paramètres pour un modèle d'équipement défini (suivant la liste d'après)
  * Faire une liste des paramètres qui iront sur les paramètres des équipements désormais : 
    * storage_format (datalogger)
    * clock_drift (datalogger)
    * clock\_drift\_unit (datalogger)
    * status
    * dip (sensor)
    * azimuth (sensor)
  * Vérifier, que ce soit à la création du modèle ou de l'équipement, que pour un Sensor on ait certains paramètres d'existant, pour un Datalogger d'autres paramètres (storage format par exemple).
  * Récupérer dans l'URL (par request) le model_id__exact=2 pour que lorsqu'on arrive dans Add Parameter on utilise cet ID comme valeur par défaut (dans le \_\_init\_\_) pour le champ "Model". En somme on veut préremplir le champ

## Intervention

  * Mélange de Notebook et Configuration (il se passe quelque chose au début d'une Configuration) et Channel

## Migration

Créer un nouveau script de migration depuis 0 en Django.

  1. Utiliser Django plutôt que Peewee
  2. Adapter pour en faire un "runscript"
  3. Enlever tout ce qui touche à Historique
  4. Adapter les principales fonctions de transitions en Django (celles pour les types d'équipement, les modèles, les stations, les places, les builts, etc.)
  5. Quand on migre les channels, demander à Maxime quelles sont les règles ZNE pour récupérer soit le dip, soit l'azimuth, etc.

Divers : 

  * à la migration depuis Gissmo 1.9 : storage\_format, clock\_drift, clock\_drift\_unit, dip et azimuth devront être crées comme paramètre des équipements qui ont une valeur pour ce champ
  * migration : sample_rate n'est PAS un paramètre, il ira dans Channel
