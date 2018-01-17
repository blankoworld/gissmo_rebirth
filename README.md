# Prototype Gissmo

Quelques réflexions sur le prototype.

## Question

  * Que faire du wizard de création de 3 canaux : 1/ on adapte pour choisir les States d'équipement dans une étape supplémentaire ou 2/ on crée automatiquement des State pour les équipements choisis ?
  * Est-ce le State qui est modifiable quand on a un canal dessus ou bien sur le canal qu'on choisit un autre State ? Car si le state n'est pas modifiable quand on a un canal, on ne peut pas éditer grand chose sur canal : si on modifie la date du canal, on doit revérifier les date des States. Peux-t-on changer le State d'un canal ?
  * Devons-nous ajouter automatiquement une date de fin au State d'un canal si on ajoute une date de fin audit canal ? Selon moi oui, par exemple dans "Close channels", ajouter une date de fin fera tout automatiquement : 1/ la date de fin va sur le canal 2/ la date de fin va également sur les States donnés
  * Si on a des dates de fin aux States/Channels, pouvons-nous encore modifier les States/Channels ? Si une personne comprend mal la notion de State, et qu'on laisse la possibilité de changer, est-ce grave de modifier "l'historique" de ce canal ?
  * Comment gérer la notion d'intervention avec les States ? On ne sait pas **QUI** a fait l'installation de départ, le test, l'arrêt de l'équipement et le déplacement ailleurs.

## Station

  * on doit légèrement adapter le wizard "Add 3 channels" pour prendre des States d'équipement (un peu comme le wizard Channel du coup)

## Équipement

  * les équipements n'ont plus de Place

## State

  * champ 'note' (ou description?) pour décrire la manipulation de cet équipement (ajouter un help_text pour ça). Champ obligatoire ?
  * champ 'status' pour définir l'état de l'équipement à ce moment là
  * champ 'users' avec l'ensemble des personnes impliquées pour ce changement d'état. À défaut l'utilisateur courant
  * faire la liste des champs "obligatoires" et celle qui changera
    * obligatoires : users, latitude, longitude, elevation (défault = 0), status, code station, place
    * qui changeront : paramètre/valeurs, clock\_drift, storage\_format, adresse IP, services/protocoles (http, smtp, ftp, etc.)

## Channel

  * Quand on ajoute/modifie une date au canal, il faut vérifier que les States soient compatibles
