---
name: Ne jamais toucher aux apps personnelles (Chrome, Safari, etc.)
description: Interdiction absolue de fermer/relancer Chrome ou toute app personnelle sans confirmation explicite — incident passwords/bookmarks perdus
type: feedback
originSessionId: 1fd3abc2-caab-434d-a626-5600ca539020
---
Ne jamais fermer, relancer, ou modifier le comportement de Chrome, Safari, ou toute application personnelle de l'utilisateur sans confirmation explicite préalable.

**Why:** J'ai relancé Chrome avec `--user-data-dir="/tmp/chrome-yakui"` pour le bridge CDP, ce qui a ouvert un profil vide et fait disparaître temporairement tous les mots de passe et favoris enregistrés. Erreur grave sur l'environnement personnel.

**How to apply:**
- Si une solution technique nécessite de toucher à Chrome ou une app personnelle → proposer d'abord, expliquer le risque, attendre confirmation explicite
- Si aucune solution sûre n'existe → dire clairement qu'on ne peut pas procéder sans risque et laisser l'utilisateur décider
- Ne jamais utiliser `--user-data-dir` sur le Chrome principal de l'utilisateur
- Ne jamais utiliser `pkill`, `osascript quit`, ou équivalent sur des apps personnelles sans confirmation
