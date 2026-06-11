---
name: feedback-conservation-existant
description: "Règles absolues de modification du wireframe Odyssey — conservation de l'existant, anti-régression, process obligatoire"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9f8442c3-4d5c-4465-87b8-99549a3d219e
---

## Règle absolue — Conservation de l'existant

Toute modification est une **amélioration additive**, jamais une réécriture.

**Why:** Le système existant fonctionne sur des points critiques (archivage, badges, sélection Claude, navigation, génération prompts, sync, briefs, workflow PO). Chaque réécriture a causé des régressions.

**How to apply:** Ajouter PAR-DESSUS l'existant. Modifier le minimum possible. Jamais réécrire goTo(), renderBriefs(), sendToClaude() sans nécessité explicite.

## Systèmes à NE JAMAIS toucher sans validation

- `goTo()` — navigation principale
- `renderBriefs()` — affichage briefs
- `sendToClaude()` — archivage (SEUL endroit done=true autorisé)
- Badges (`archivesMode ? b.done : !b.done`)
- Sélection Claude
- Génération de prompts
- Synchronisation Firebase

## Process obligatoire avant toute modification

1. Analyser l'existant — identifier dépendances, effets de bord, fonctions couplées
2. Identifier les fonctions réellement concernées
3. Modifier le minimum possible (modifications ciblées, conditions supplémentaires, ajustements locaux)
4. Tester les flows critiques après modification
5. Vérifier l'absence de régression
6. Confirmer les comportements inchangés

## Tests obligatoires après chaque modification

- Ouverture/fermeture modale
- Navigation défaut ↔ Claude ↔ Équipe ↔ Archives ↔ Dernières modifications
- Archivage (seulement claudeSelection → done=true)
- Badges (respectent archivesMode)
- Sélection Claude
- Génération prompt
- Retour vision par défaut à la réouverture
- Absence d'erreur console

## Ce qu'il ne faut PAS faire

- Réécriture complète
- Remplacement d'architecture
- Refactor agressif
- Simplification destructrice
- Modifier des systèmes critiques sans nécessité
