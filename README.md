# Prototype Gissmo

Quelques réflexions sur le prototype.

## Idée pour résoudre le souci des States qui se suivent pour un Channel

Problème : Pour les Channel/State/Equipement, comment garder l'historique des changements d'état d'un équipement sans influer sur les états d'un Channel ?

  * soit permettre plusieurs State par équipement pour un Channel : pose des problèmes pour "choisir" les états des équipements sur le Channel
  * soit créer un "notebook" pour les équipements (avec les changements d'état, des notes, etc.) => paraît compliqué car on gère parfois des changements d'état (running/available/failure) et parfois juste des notes. D'autres fois l'état broken implique la fermeture d'un canal

Quoiqu'il en soit, je pense qu'il serait intéressant : 

1/ d'afficher le status (running/available/to test) sur l'équipement, mais de le stocker dans le State
2/ si le status change, alors on créer un nouveau State identique au précédent et on l'ajoute au Channel (si le state précédent est lié à un Channel)
3/ si le status est broken (ajouter un marqueur "this state close channels) alors on ferme le canal, on ferme le state actuel, et on démarre un nouveau State en broken sur aucun channel et sans aucune date de fin
4/ sur le channel on affiche que les équipements choisis (au lieu des States)
5/ sur le channel, on propose que les équipements qui ont des States qui pointent sur la station identique au channel. Et dont l'agrégat (par code station) donne une date de début et une date de fin qui contient celle du channel (sauf si le channel n'a pas de date de fin, alors les states doivent avoir une date de début inférieure ou égale à celle de la date de début du channel)
6/ sur le channel, on ajoute des boutons "change equipment" à côté de chaque équipement, pour vérifier s'il est possible d'utiliser les "State" adéquat d'un nouvel équipement par rapport aux dates => ceci impliquerait de pouvoir un jour supprimer des State car on se serait trompé ?
7/ sur channel on affiche un encart contenant les infos contenues dans chaque équipement (State) sans dire que c'est un State
8/ sur Equipment, on affiche aussi toutes les infos contenues dans le State et on propose le changement, MAIS si on change les infos, on doit vérifier que soit on créer un nouveau state, soit on doit fermer le channel (dans le cadre d'une fermeture de Channel, on doit bloquer la vue et le signaler)

## Question

  * Que faire du wizard de création de 3 canaux : 1/ on adapte pour choisir les States d'équipement dans une étape supplémentaire ou 2/ on crée automatiquement des State pour les équipements choisis ?
  * Est-ce le State qui est modifiable quand on a un canal dessus ou bien sur le canal qu'on choisit un autre State ? Car si le state n'est pas modifiable quand on a un canal, on ne peut pas éditer grand chose sur canal : si on modifie la date du canal, on doit revérifier les date des States. Peux-t-on changer le State d'un canal ?
  * Devons-nous ajouter automatiquement une date de fin au State d'un canal si on ajoute une date de fin audit canal ? Selon moi oui, par exemple dans "Close channels", ajouter une date de fin fera tout automatiquement : 1/ la date de fin va sur le canal 2/ la date de fin va également sur les States donnés
  * Si on a des dates de fin aux States/Channels, pouvons-nous encore modifier les States/Channels ? Si une personne comprend mal la notion de State, et qu'on laisse la possibilité de changer, est-ce grave de modifier "l'historique" de ce canal ?
  * Que faire si on s'est trompé de State ou d'équipement dans un Channel ? On peut supprimer des States ? Si oui, comment supprimer des States a posteriori ?

## Station

  * on doit légèrement adapter le wizard "Add 3 channels" pour prendre des States d'équipement (un peu comme le wizard Channel du coup)

## Équipement

  * les équipements n'ont plus de Place

## State

  * champ 'note' (ou description?) pour décrire la manipulation de cet équipement (ajouter un help\_text pour ça). Champ obligatoire ?
  * champ 'status' pour définir l'état de l'équipement à ce moment là
  * champ 'users' avec l'ensemble des personnes impliquées pour ce changement d'état. À défaut l'utilisateur courant
  * faire la liste des champs "obligatoires" et celle qui changera
    * obligatoires : users, latitude, longitude, elevation (défault = 0), status, code station, place
    * qui changeront : paramètre/valeurs, clock\_drift, storage\_format, adresse IP, services/protocoles (http, smtp, ftp, etc.)

## Channel

  * Quand on ajoute/modifie une date au canal, il faut vérifier que les States soient compatibles
