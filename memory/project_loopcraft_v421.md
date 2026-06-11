---
name: project-loopcraft-v421
description: "État V4.21 du wireframe Télécollecte — checkpoint fin de session 2026-06-05, version envoyée aux POs"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6a12bd0b-ab6d-4c7f-a04e-28d11d0c6606
---

Version de référence active : **wireframe-telecollecte-cas1-V4.21.html** (commit `3031bcf`, 2026-06-05)
Dernier commit repo : `3ec9f10` — fix index.html pointe vers V4

**Why:** V4.21 est le checkpoint officiel de fin de session — c'est la version envoyée aux POs (Julie, Nelly) pour la phase de review métier.

**How to apply:** Ne pas modifier V4.html sans vérifier d'abord que les POs n'ont pas de commentaires en attente. Phase de review = stabilité prioritaire sur features.

---

## Features ajoutées en session 2026-06-05 (depuis V4.11)

**Complément non-interfacé**
- Fix revalidation complément : reset champs + accumulation `_frozenAttendu`

**Harmonisation wordings (14 libellés)**
- Colonnes tableau, KPI, têtes Date antérieure — voir commits refactor(ux)

**Régularisation — workflow complet**
- Tableau 2 colonnes, WeChat masqué (pas d'écart)
- Modale + toaster réutilisés depuis Télécollecte
- Mode complétable post-validation : "Régularisation effectuée" + "Complément"
- KPI cohérents : Écart à régulariser décroît, recalculé ensemble avec Total/Solde
- Badge Solde restant supprimé (KPI suffisants)
- Couleurs : Écart à régulariser rouge→vert, Total régularisé navy

**Documentation — 27 RG dans le drawer**
- Télécollecte RG-01→08, Date antérieure RG-09→18 (incl. purge comptable), Régularisation RG-19→27
- Init au chargement de page (IIFE scope global, version `v2.0-27rg`)
- Blocs "Question métier à valider" orange
- Bouton Copier pour Jira inclut les questions

---

## Phase de review PO — État au 2026-06-05

**Portail PO :** `https://studiojailoop.github.io/telecollecte-odyssey/`
**Comptes PO :** Julie / Ody26 · Nelly / Ody26
**Commentaires :** stockés Firebase (`studio-jailoop-default-rtdb.firebaseio.com/comments`) + localStorage cache. Poll toutes les 5s.
**Règle absolue :** tout push en phase de review doit préserver les commentaires Firebase — ils sont sur Google, jamais dans le repo.

**Ce que voient les POs (sans ?designer=1) :**
- Wireframe V4.html complet (Télécollecte · Date antérieure · Régularisation)
- Bouton 💬 bas droite → commentaires pins
- Bouton 📘 Documentation dans le panel PO → 27 RG
- PAS de panel designer, toggles, sélecteur version, outil briefs

---

## Risques identifiés (audit stabilité)

- Firebase offline passager → fallback localStorage, commentaires récupérés au retour
- PUT global `fbSave()` → risque de conflit si 2 POs modifient au même instant (faible en review)
- Ces risques ne sont pas critiques pour la phase de review à faible volume

---

## Fichier de travail actif
`01_Club Med/wireframe-telecollecte-cas1-V4.html`

## Repo git
`/Users/sebastienkeller/Library/CloudStorage/Dropbox/Taff/01_Administratif/02_Studio Jaïloop/Studio J/00_Club med/01_Club Med`
