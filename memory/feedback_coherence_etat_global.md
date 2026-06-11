---
name: feedback-coherence-etat-global
description: Toujours vérifier la cohérence de TOUS les éléments visuels quand un état global change — pas seulement le composant principal
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a4b5600a-4d06-4dda-88d0-d5e60db2c5b9
---

Quand un état global change (archivesMode, currentTab, commentMode…), tous les éléments visuels qui dépendent de cet état doivent être mis à jour ensemble — pas seulement le composant principal de la feature.

**Why:** Lors du toggle archivesMode, `renderBriefs()` était appelé mais pas `refreshPins()` — les pins restaient en désync. Sébastien a dû le signaler lui-même alors que c'était détectable à la lecture du code.

**How to apply:** À chaque fois qu'une fonction modifie un état global (toggle, navigation, switch…), lire TOUTES ses dépendances et vérifier que chaque composant visuel concerné est rafraîchi. Ne pas se limiter au composant demandé par la feature en cours.
