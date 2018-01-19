# Pérégrination sur le problème des paramètres qui n'influent pas la réponse instrumentale mais qui doivent être suivis

Après la réunion de mercredi, nous savons qu'il existe plusieurs types d'informations :

  * celles qui changent la réponse instrumentale et demandent théoriquement la création d'un nouveau canal
  * celles qui ne changent rien à ce canal mais dont l'historique doit être retenu

Nous savons également que dans les paramètres d'un équipement - qu'on copie pour les lier au canal - il existe certains paramètres qui influent sur la réponse instrumentale, d'autres non.

Pour régler ce problème j'avais envisagé plusieurs possibilités, et je t'en donne l'historique. À la fois pour avoir ton avis sur la solution que j'envisage, mais peut-être qu'en donnant ma réflexion tu verrais quelque chose que j'ai loupé. Ça me paraît nécessaire.

## Solution 1 : plusieurs States

Étant donné qu'on a proposé la solution avec State (des States qui se suivent, sans overlap et qui contiennent toutes les infos du matériel sur la période choisie), la première réaction c'était "pas grave, on autorise plusieurs State.

Le problème : on a pas vraiment de contrainte forte avec ça. La vérification des States est embêtante tout simplement parce qu'on est censé autoriser 1 seul State par équipement, sauf dans le cas où les States se suivraient correctement l'un après l'autre (comme présenté sur le schéma que j'avais donné en pièce jointe).

Ça ne me paraît pas du tout correct comme solution.

## Solution 2 : JSON modifié

Du coup on se dit qu'après tout, avec un JSON, on pourrait l'agrémenter et ajouter une section "timeline" qui contiendrait toutes les lignes des champs modifiés qui n'influent pas sur la réponse instrumentale. Un peu du style : 

"timeline": [
    {
        "date": "2018-01-02 10:31:49",
        "user": "olivier.dossmann",
        "parameter": "status",
        "value": "running",
        "note": "Change equipment battery",
    }
]

Ce qui m'embête avec cette solution, c'est l'affichage du résultat sur l'équipement, le channel, peut-être la Station.

Toujours faisable, mais pas concluant.

## Solution 3 : Un autre objet lié à State

J'ai donc pensé à mettre les informations ailleurs, dans une table liée à State afin d'avoir l'historique des changements de ces champs acculé à ce State.

Avec des colonnes comme : 

  * date
  * user
  * parameter
  * value
  * note

Mais pareil, pour un équipement donné, faire la liste de toutes ces choses me paraît over-compliquées.

## Solution 4 : la Timeline

Il reste donc la solution proposée initialement par Jérôme, le Notebook. Mais je n'aime pas le nom, parce que ça implique presque qu'on fasse ce qu'on veut dedans.

Je ne sais plus si c'est toi qui parlait du mot Timeline ou si c'est lié à un des projets auquel je travaillais déjà, quoiqu'il en soit j'ai pensé à Timeline : des évènements sur un équipement. C'est à dire, les même colonnes que proposées dans la solution 3, mais avec une colonne supplémentaire : "equipment_id".

Tous les champs sont obligatoires, excepté la note.

Au niveau des données, ça me paraît censé : les paramètres qui influent sur la réponse instrumentale sont dans State. Et un seul State par équipement et par Canal semble permettre de filtrer correctement et de faire matcher les State/Channel.
Et les paramètres qui n'influent pas sont suivi dans cette Timeline.

Reste à faire un affichage de tout ceci. Pour ça, j'ai plusieurs idées, mais généralement c'est d'afficher les données en lecture seule sur le channel, ou sur l'équipement (ou les deux suivant les paramètres/données).
Sur channel, à côté de l'ensemble des paramètres qui influent sur la réponse instrumentale, afficher quelque chose comme "Corriger" pour permettre de les modifier via State. Ceci implique de ne pas permettre d'accéder à State en édition depuis Équipement par exemple. Et probablement pas de montrer les States depuis Équipement en fait. Pas en tant que State en tout cas.

Sur channel, on pourrait aussi montrer les paramètres qui n'influent pas sur la réponse instrumentale, soit par un formulaire intégré qui demande date/utilisateur/note et un bouton de validation, soit par un bouton "Modifier" qui amène à un wizard. Ce même wizard qui pourrait être proposé sur Équipement.

En somme, Timeline et State ne serait à propement parler pas disponibles sur l'interface admin de Django, mais nous les modifierions par les différents Wizard/boutons/autre qu'on proposerait.

Concernant les interventions, ce serait un aggrégat des notebooks d'une station, des timelines de l'équipement (pendant les périodes des States sur cette Station) et peut-être de certaines infos du Canal (mais je ne vois pas quoi par rapport à ce qui existe déjà).

## Conclusion

Ma solution serait la solution 4. Ça demanderait un gros boulot, mais on le sent bien que ces Channel et l'historique est problématique à chaque fois.
La liste de ce que je vois à faire : 

  * adapter StationXML
  * refaire la page Station pour afficher les équipements, les channels, l'historique des changements
  * wizard pour créer un channel
  * adapter le wizard 3 channels
  * refaire la page Equipement pour afficher des paramètres
  * wizard pour changer les paramètres de l'équipement en conservant un historique
  * wizard de création d'un nouveau State pour l'équipement (paramètres qui influent sur la réponse instrumentale) avec proposition de fermer le canal en cours
  * adapter le wizard close channels : juste changer le champ ciblé pour la date et modifier la vérification
  * API à revoir ? Il faut réfléchir à comment proposer les différentes informations du Channel/Équipement du coup. Et le timeline aussi
  * rajouter à la plupart des objets created\_at, updated\_at et mettre à jour à chaque fois (utile pour les Channels et l'API)
  * adapter l'état d'une station (calculé en fonction des channels ouvertes, fermées, etc.)
  * adapter la carte des Stations si nécessaire (à première vue pas besoin)

Ça me semble colossal. D'un coup je suis moins confiant :-/. Qu'en penses-tu ?
