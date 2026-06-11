---
name: project-loopcraft-proposals-locked
description: "État verrouillé des propositions Prop_A et Prop_Abis — validées le 2026-05-27, ne plus toucher"
metadata:
  type: project
  originSessionId: current
---

## Propositions verrouillées — validées le 2026-05-27

### Prop_A — VALIDÉE ✅
- Ligne 1 : texte date à gauche + bouton "Valider la saisie" à droite
- Ligne 2 : KPI (Montant attendu / Montant saisi / Écart) + badge "Écart détecté" à droite
- Sticky : pill "Écart : -5,00 €" + bouton Valider, gap 48px entre les deux

### Prop_Abis — VALIDÉE ✅
- Tout sur une seule ligne : texte date + KPI (Attendu/Saisi/Écart) + bouton Valider
- Sticky : identique à Prop_A (même pill + bouton)

### Règle absolue — NE PLUS TOUCHER
Prop_A et Prop_Abis sont figées. Aucune modification sans demande explicite.

### Architecture technique (commit 764cced)
- `bloc-date-main` : `display:block` (pas flex) pour ne pas interférer avec les enfants
- `bloc-date-row` : `display:flex; align-items:center; width:100%` — la ligne date+bouton
- `showProposal()` remet `display:flex` (pas `''`) sur `bloc-date-row` au retour d'Abis
- L'IntersectionObserver gère le pill sticky pour Prop_A ET Prop_Abis (`activeProposal === 'a' || activeProposal === 'abis'`)

### Règle des 3 screenshots
Avant ET après toute modification dans cette zone :
1. screenshot En cours
2. screenshot Prop_A  
3. screenshot Prop_Abis
→ Si un état change alors qu'il ne devait pas, annuler immédiatement.

**Why:** Boucle de régressions croisées sur 2026-05-27 — la zone est fragile car les propositions partagent le même `bloc-date`.

**How to apply:** Ne jamais toucher au `bloc-date`, au sticky, à l'IntersectionObserver, ou à `showProposal()` sans respecter le protocole 3 screenshots.
