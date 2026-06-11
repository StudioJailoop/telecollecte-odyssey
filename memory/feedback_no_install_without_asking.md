---
name: Ne rien installer sans demander
description: Toujours demander confirmation avant d'installer des packages, créer des fichiers système, ou modifier quoi que ce soit hors du dossier Claude Yaki
type: feedback
originSessionId: 0220a95e-df9f-4bdc-b89a-34aeb76ba3c0
---
Ne jamais installer de dépendances, créer de fichiers système, ou modifier l'environnement sans demander d'abord.

**Why:** L'utilisateur veut garder son Mac propre et organisé. Tout ce qui est lié aux projets Claude doit aller dans `~/Desktop/Claude Yaki/`. Les exceptions système (ex: LaunchAgents) doivent être expliquées et validées avant.

**How to apply:** Avant tout `npm install`, création de `.plist`, ajout de LaunchAgent, ou toute action hors de `Claude Yaki` — demander d'abord et expliquer pourquoi c'est nécessaire.
