---
name: project-loopcraft-v422
description: "État V4.22 du wireframe Télécollecte — session 2026-06-12, fixes sticky + textes EN + mémoire projet déplacée"
metadata:
  type: project
---

Version active : **wireframe-telecollecte-cas1-V4.html** (commit `9818b39`, 2026-06-12)

**Why:** Session de préparation présentation Télécollecte — fixes UI + textes anglais + consolidation mémoire.

**How to apply:** V4.html est le fichier de travail actif. Les snapshots versionnés (V4.21, V4.22...) sont figés.

---

## Changements session 2026-06-12

**Textes UI → anglais**
- Tous les labels UI passés en anglais (tabs, boutons, badges, KPI, headers tableau)
- Phrase intro : "Please proceed with the telecollection of [date]"
- Tabs : Telecollection / Previous Date / Regularisation
- Boutons : Submit entry / Submit regularisation / Complete regularisation
- Badges : No discrepancy / Discrepancy detected / Regularised / Remaining balance

**Fix bouton sticky Submit entry**
- Telecollection ET Previous Date : bouton visible au scroll (était absent)
- Remplace IntersectionObserver (ne se déclenchait pas sur vue display:none) par scroll listener + getBoundingClientRect
- top: 0 sur .tpe-tabs-bar (corrige barre partiellement cachée)

**Mémoire projet**
- Toute la mémoire déplacée dans `memory/` Dropbox (référence unique)
- CLAUDE.md mis à jour pour pointer vers `memory/`
- Token GitHub retiré de project_odyssey_system.md

**Cardex V2**
- Prop D ajoutée : 3 colonnes (Profil | Room+Expense | Cardex) — calée sur maquette Figma Prospective
- V1 figée, V2 = fichier de travail actif pour Cardex
- Règles de conception Cardex enregistrées (DS strict, spacing x4, no new components)

---

## Playwright / serveur local
- Playwright fonctionnel sur `http://127.0.0.1:8765/` (pas localhost)
- server.py bindé sur `127.0.0.1` depuis fix 2026-06-11

## Repo git
`/Users/sebastienkeller/Library/CloudStorage/Dropbox/Taff/01_Administratif/02_Studio Jaïloop/Studio J/00_Club med/01_Club Med`
