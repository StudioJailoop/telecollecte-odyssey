---
name: feedback-cardex-design-rules
description: Règles de conception Cardex — DS strict, no new components, spacing x4, cohérence avant créativité
metadata:
  type: feedback
---

## Sources de vérité (ordre de priorité)
1. Design System Figma (Ody Trident Ψ 2.0)
2. Écrans existants validés
3. Maquettes Cardex fournies
4. Règles métier documentées

En cas de conflit : maquettes + DS font foi.

## Composants — règle absolue
- NE PAS inventer de composants
- Avant toute proposition : chercher dans le DS, vérifier variantes existantes, réutiliser
- Si aucun composant ne correspond : signaler le manque précisément, demander validation avant création
- Réutiliser un composant à 90% > créer un nouveau

## Spacing — grille x4 stricte
Valeurs autorisées : 4, 8, 12, 16, 20, 24, 32, 40, 48, 64
Valeurs interdites : 13px, 17px, 22px, 37px — tout ce qui n'est pas multiple de 4
Si un espacement déroge : corriger ou justifier explicitement.

## Checklist avant toute production
- [ ] Composants utilisés → tous issus du DS ?
- [ ] Variantes utilisées → correctes ?
- [ ] Espacements → conformes grille x4 ?
- [ ] Hiérarchie visuelle → cohérente ?
- [ ] Cohérence avec les autres écrans Club Med ?

## Principe fondateur
Cohérence > créativité.
L'écran doit sembler conçu par la même équipe, avec les mêmes composants et les mêmes règles.
En cas de doute entre créer/réutiliser → toujours réutiliser, demander confirmation avant exception.

**Why:** Le client veut un produit cohérent, pas des écrans isolés — chaque déviation du DS crée de la dette design.
**How to apply:** Sur tout travail Cardex (et par extension tout travail Club Med), appliquer cette checklist avant de proposer quoi que ce soit. Jamais de spacing libre, jamais de composant inventé.
