---
name: feedback-startup-behavior
description: "À l'ouverture d'une conversation, mentionner uniquement la dernière version active — pas les proposals, pas les chantiers en suspens"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0ac70445-1d86-4157-82b0-f9f02eba488b
---

À l'ouverture d'une conversation, ne mentionner que la **dernière version active** sur laquelle on s'est arrêté (ex. V4.21) et son état (en review, stable, en cours...).

**Why:** L'utilisateur ne veut pas être noyé par le contexte global au démarrage — Prop_A, Prop_B, Prop_C, features en suspens, etc. Ce n'est pas utile tant qu'il ne les demande pas.

**How to apply:** Résumé d'ouverture = 2-3 lignes max : version active + état court. Tout le reste (proposals, chantiers, risques) reste disponible mais n'est jamais proactivement mentionné au lancement.
