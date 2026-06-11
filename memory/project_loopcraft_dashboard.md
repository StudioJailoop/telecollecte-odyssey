---
name: project-loopcraft-dashboard
description: "Loopcraft — espace designer Sébastien, dashboard studio.html avec navigation 3 niveaux (Dashboard → Projet → Sous-projet → Wireframe)"
metadata: 
  node_type: memory
  type: project
  originSessionId: a0584e63-035c-49be-9c55-b53787060cdf
---

## Loopcraft — Dashboard Designer

Outil personnel de Sébastien pour piloter ses projets wireframes. Distinct des wireframes client — c'est son espace de travail.

**Fichier principal :** `/Users/sebastienkeller/Library/CloudStorage/Dropbox/Taff/01_Administratif/Claude Yaki/01_Club Med/Loopcraft/studio.html`
**Répertoire de travail :** `/Users/sebastienkeller/Library/CloudStorage/Dropbox/Taff/01_Administratif/Claude Yaki/01_Club Med`
**Git root :** `/Users/sebastienkeller/Library/CloudStorage/Dropbox/Taff/01_Administratif/Claude Yaki`

**URLs publiques (GitHub Pages) :**
- Dashboard designer : `https://studiojailoop.github.io/telecollecte-odyssey/01_Club%20Med/Loopcraft/studio.html?go=dashboard`
- Wireframe designer : `https://studiojailoop.github.io/telecollecte-odyssey/01_Club%20Med/wireframe-telecollecte-cas1-V4.html?designer=1`
- Portail PO : `https://studiojailoop.github.io/telecollecte-odyssey/` (redirige vers portail.html)

**Raccourci bureau :** `Loopcraft Dashboard.app` → ouvre dashboard GitHub Pages directement

**Accès designer :**
- Depuis dashboard → clic Télécollecte → `?designer=1` ajouté automatiquement → bouton modale PO + bouton retour dashboard visibles
- POs n'ont pas `?designer=1` → voient uniquement leur panneau commentaires

**Firebase :**
- Commentaires pins : `https://studio-jailoop-default-rtdb.firebaseio.com/comments` (poll 5s)
- Briefs PO : `https://studio-jailoop-default-rtdb.firebaseio.com/briefs_telecollecte`
- État briefs : 10 total, 6 archivés (done:true), 4 en attente (done:false)
**Login :** ID = `Studio Jailoop` / mdp = `Loopcraft`
**Auto-login bypass :** `?go=dashboard` dans l'URL (évite l'écran de connexion)

---

## Structure de navigation (3 niveaux)

1. **Dashboard** — vue d'ensemble avec KPIs, contributions, raccourcis
2. **Projet** (ex: Club Med) — liste des sous-projets avec statut (clic direct, pas d'expand sidebar)
3. **Sous-projet** (ex: Télécollecte) → clic ouvre directement le wireframe

Navigation latérale sidebar (Linear/Notion style), projets chargés depuis `Loopcraft/data/projects.json`.
**Sidebar :** clic sur un projet navigue directement via `showProjectView(pid)` — plus d'expand/chevron.

---

## Sections du Dashboard (dans l'ordre)

1. **Vue d'ensemble** — 4 KPI tiles (Projets, Sous-projets, Terminés, En attente)
2. **Analyse + Raccourcis** — côte à côte : Contributions + Santé des projets (gauche) + boutons raccourcis (droite)
3. **Dernier projet travaillé** — card(s) même taille que les KPI tiles (74px de hauteur)
4. **Estimation par sous-projet** — widget 507px large, 74px de hauteur

Padding : 48px 48px 56px. Gap sections : 42px. Section labels avec border-bottom gris.

---

## Layout & mesures clés (session 2026-05-21)

- **KPI tiles** : `height: 74px`, gap 10px, border-radius 12px, border 1px #EAECF0, shadow 0 1px 3px
- **KPI chiffres** : 24px bold, letter-spacing -0.5px
- **KPI labels** : 11px / uppercase / #6B7280
- **Section labels** : 11px / 700 / #9CA3AF / border-bottom 1.5px #EAECF0 / margin-top 42px
- **kpi-strip** : `width: calc(75% - 10px)` — alignée sur le bloc Analyse
- **dash-col-aside** (Raccourcis) : `width: calc(25% - 6px)` — même largeur qu'une KPI card
- **Bloc estimation** : `width: 507px` / `height: 74px` — même largeur que le bloc Contributions
- **Watermark logo** : `logo-jailoop-color.png` en `position:absolute`, centré dans `.main`, `opacity: 0.015`, z-index: 0. `.main` a `overflow: hidden` pour éviter le scroll.
- **Fond page** : `#F7F8FA`
- **Cards internes** : border-radius 12px, border 1px #EAECF0, shadow 0 1px 3px

---

## KPI "En attente"

Source : `wf_briefs_telecollecte` localStorage, filtre `done: false`.
Actuellement : 4 en attente sur 10 briefs total.
Remplace l'ancien KPI "Non lus" (Firebase messages — sans tracking réel).

---

## Données projets

**Fichier :** `Loopcraft/data/projects.json`
**Projet actif :** Club Med > Télécollecte
**Fichier actif :** `../wireframe-telecollecte-cas1-V4.html` (version "En cours")
**V5 existe** mais n'est pas le fichier de travail actif — V4 reste la référence

---

## Retour au dashboard depuis un wireframe

Bouton "← Retour au dashboard" (cercle blanc, bordure grise, flèche ←) :
- Positionné `bottom: 24px; left: 24px` (sous le bouton chat jaune à `bottom: 84px`)
- Lien : `Loopcraft/studio.html?go=dashboard`
- Visible uniquement sur localhost

---

## Bugs corrigés session 2026-05-21

### Commentaires équipe (badge incohérent)
- Badge "1" affiché mais panel vide
- Cause 1 : `.forEach(r => {` sans `ri` déclaré → `ri` undefined
- Fix : `.forEach((r, ri) => {`
- Cause 2 : badge ne filtrait pas `requalified: true`
- Fix : ajout `&& !p.requalified` / `&& !r.requalified` dans le calcul du badge

### Bouton sticky "Valider la saisie" (wireframe)
- Décalage vertical au scroll
- Cause : `height: auto` + `transition: height` dans `.is-stuck` empêchait le recalcul correct
- Fix : suppression `transition: height`, `height: 64px` fixe sur `.is-stuck`, tabs forcées à `height: 64px` + `align-items: center`, bouton avec `align-self: center`
- Résultat mesuré : `diff: 0px` (centre bouton = centre barre)

---

## Documentation confidentielle

`Loopcraft/LOOPCRAFT_PRODUCT_DOCUMENTATION.md` — 1171 lignes, 14 sections (vision, users, architecture, écrans, data model, roadmap).
**Gitignored — local uniquement, jamais pousser sur GitHub.**

---

## État GitHub

Repo : `StudioJailoop/telecollecte-odyssey`
Dernier push session 2026-05-21 : `fix(wireframe): bouton sticky parfaitement centré — diff:0px confirmé`
Dashboard (`studio.html`) est dans le repo et publié.

**Why:** Loopcraft est le cockpit de Sébastien — à ne pas confondre avec les wireframes client. C'est une couche au-dessus.

**How to apply:** Quand Sébastien parle de "son dashboard" ou de "Loopcraft", c'est studio.html. Quand il parle du wireframe, c'est wireframe-telecollecte-cas1-V4.html (fichier de travail actif).
