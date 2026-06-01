# LOOPCRAFT — Product Documentation

> Version 1.0 — Mai 2026  
> Rédigé par Studio Jailoop  
> Confidentiel — usage interne

---

## TABLE DES MATIÈRES

1. [Vision Produit](#1-vision-produit)
2. [Utilisateurs](#2-utilisateurs)
3. [Architecture Produit](#3-architecture-produit)
4. [Parcours Utilisateurs](#4-parcours-utilisateurs)
5. [Écrans](#5-écrans)
6. [Système de Commentaires](#6-système-de-commentaires)
7. [Espace Designer](#7-espace-designer)
8. [Espace Intervenants](#8-espace-intervenants)
9. [Espace Claude](#9-espace-claude)
10. [Génération de Prompts](#10-génération-de-prompts)
11. [Modèle de Données](#11-modèle-de-données)
12. [Architecture Technique](#12-architecture-technique)
13. [Roadmap Potentielle](#13-roadmap-potentielle)
14. [Résumé Exécutif](#14-résumé-exécutif)

---

## 1. VISION PRODUIT

### Le problème que Loopcraft résout

Dans un projet UX/UI classique, la collaboration entre le designer, les Product Owners et les métiers est profondément fragmentée :

- Les retours arrivent par e-mail, Slack, WhatsApp, réunion
- Le designer recopie à la main dans Notion ou une liste
- Il doit comprendre, trier, prioriser seul
- Il transmet ensuite à l'IA (Claude) en reformulant de zéro
- L'IA ne connaît pas le contexte du wireframe
- Le suivi des décisions est perdu

**Résultat** : perte de temps massive, contexte dégradé, modifications appliquées sans traçabilité, retours perdus entre deux sessions.

### Pourquoi Loopcraft existe

Loopcraft est un **espace de travail collaboratif centré sur le wireframe**. Il connecte directement :

- le wireframe (interface de travail du designer)
- les retours des intervenants (PO, métier, équipe)
- l'IA (Claude) pour qualifier, challenger et appliquer les modifications

L'objectif est de **supprimer toutes les frictions entre le retour et la modification appliquée**, en gardant une traçabilité complète de chaque décision.

### Ce qui différencie Loopcraft des outils existants

| Outil | Limite par rapport à Loopcraft |
|---|---|
| **Figma** | Commentaires non structurés, pas de workflow de qualification, pas de connexion IA, pas de prompt generation |
| **Miro** | Outil de brainstorming, pas de wireframe fonctionnel, pas de système de retours typés, pas d'IA intégrée |
| **Jira** | Gestion de tickets, pas de lien direct avec le wireframe, pas de collaboration visuelle, pas d'IA contextuelle |
| **Notion** | Prise de notes, pas de wireframe, pas de commentaires positionnés, pas de prompt generation |
| **Lyssna / Maze** | Tests utilisateurs, pas de collaboration design/PO, pas de modification en temps réel |

### Proposition de valeur principale

> Loopcraft transforme les retours bruts des intervenants en modifications appliquées directement sur le wireframe, via l'IA, avec une traçabilité complète de chaque décision.

---

## 2. UTILISATEURS

### 2.1 Designer (Studio Jailoop — Sébastien)

**Rôle** : Propriétaire du produit. Seul utilisateur avec accès complet.

**Droits** : Lecture + écriture + administration

**Objectifs** :
- Centraliser tous les retours des intervenants
- Qualifier, prioriser, reclassifier les retours
- Générer des prompts structurés pour Claude
- Suivre l'avancement des modifications
- Gérer les projets et sous-projets

**Actions possibles** :
- Accéder au dashboard Loopcraft Studio
- Créer / modifier / archiver des projets et sous-projets
- Ouvrir le panneau "Retours PO" (espace designer)
- Voir tous les commentaires de tous les auteurs
- Qualifier un retour (Retour / Idée / RG / Question)
- Reclassifier un retour vers un autre type
- Réécrire un retour via IA
- Sélectionner des retours pour Claude (⚡)
- Générer le prompt structuré
- Envoyer à Claude via le pont local
- Archiver les retours traités (done=true)
- Accéder aux archives (Journal des modifs)
- Restaurer depuis la corbeille (30 jours)
- Basculer entre les versions du wireframe

**Actions interdites** : Aucune — accès total.

---

### 2.2 Product Owner (PO)

**Rôle** : Intervenant principal. Accède au wireframe via un lien public (GitHub Pages).

**Droits** : Lecture du wireframe + dépôt de commentaires

**Objectifs** :
- Observer le wireframe en cours
- Déposer des retours fonctionnels
- Qualifier ses propres commentaires (type)
- Suivre ses propres contributions

**Actions possibles** :
- Visualiser le wireframe
- Poser des pins de commentaires sur le wireframe (clic gauche)
- Répondre à un thread existant
- Qualifier son commentaire : Retour / Idée / RG / Question
- Voir ses propres commentaires via le panel PO (bouton bas-droite)
- Changer de version du wireframe (sélecteur)

**Actions interdites** :
- Voir les retours des autres POs dans le panel PO (chacun voit les siens)
- Accéder au panneau designer "Retours PO" (bouton jaune — localhost uniquement)
- Modifier ou supprimer les retours du designer
- Archiver des retours
- Générer des prompts
- Accéder au dashboard Loopcraft Studio

---

### 2.3 Métier

**Rôle** : Utilisateur terrain. Accède au wireframe via un lien avec son prénom (`?user=Prénom`).

**Droits** : Lecture + commentaires

**Objectifs** :
- Valider la conformité fonctionnelle
- Signaler des incohérences avec les processus métier
- Apporter des précisions sur les règles de gestion

**Actions possibles** : Identiques au PO.

**Actions interdites** : Identiques au PO.

---

### 2.4 Observateur / Sponsor

**Rôle** : Consultation passive. Accède au wireframe en lecture seule (sans paramètre `?user=`).

**Droits** : Lecture seule

**Objectifs** :
- Suivre l'avancement du projet
- Visualiser le wireframe sans interagir

**Actions possibles** :
- Visualiser le wireframe
- Changer de version

**Actions interdites** :
- Déposer des commentaires
- Accéder à tout espace designer ou PO

---

## 3. ARCHITECTURE PRODUIT

### Hiérarchie complète

```
Loopcraft Studio (dashboard)
│
├── Projet (ex: Club Med)
│   ├── Métadonnées : nom, couleur, description, date
│   │
│   └── Sous-projet (ex: Télécollecte)
│       ├── Métadonnées : nom, statut (En cours / Done), version, date màj
│       ├── Wireframe (ex: V5)
│       │   ├── Vues fonctionnelles : Télécollecte / Date antérieure / Régularisation
│       │   ├── Versions : V1 → V2 → V3 → V4 → V5 (sélecteur intégré)
│       │   ├── Panel Options (bas-droite) : toggles, version, commentaires
│       │   └── Système de commentaires (pins Firebase)
│       │       ├── Pins positionnés sur l'interface
│       │       ├── Threads de discussion
│       │       └── Catégories : Retour / Idée / RG / Question
│       │
│       └── Espace Designer (localhost uniquement)
│           ├── Panneau Retours PO
│           │   ├── Onglets par type : Retour / Idée / RG / Question
│           │   ├── Onglet Claude : sélection + génération prompt
│           │   ├── Onglet Commentaires équipe
│           │   └── Mode Archives : Journal des modifs
│           └── Pont Claude Code (server.py)
│               ├── Envoi prompt → Claude Code
│               ├── Réécriture IA des retours
│               └── Génération texte journal narratif
│
└── Espace PO (GitHub Pages — public)
    └── Portail intervenants (portail.html)
        └── Accès wireframe avec identité (?user=Prénom)
```

### Rôle de chaque niveau

| Niveau | Rôle |
|---|---|
| **Dashboard** | Vue globale de l'activité — projets, retours, contributions, santé |
| **Projet** | Conteneur client — regroupe tous les chantiers d'un client |
| **Sous-projet** | Unité de travail — correspond à une feature, un parcours, un écran |
| **Wireframe** | Interface fonctionnelle — prototype interactif built avec le DS Trident Ψ 2.0 |
| **Version** | Snapshot historique — chaque itération est figée, versionnée, accessible |
| **Commentaires** | Retours positionnés — ancrés sur l'interface, typés, synchronisés Firebase |
| **Espace Claude** | Sélection + génération prompt structuré → modification directe du wireframe |

---

## 4. PARCOURS UTILISATEURS

### 4.1 Workflow principal : du retour à la modification

```
[Designer]
Crée le projet dans Loopcraft Studio
        ↓
Crée le sous-projet et associe le wireframe
        ↓
Partage le lien wireframe aux intervenants
        ↓
[Intervenants — POs / Métier]
Ouvrent le wireframe (GitHub Pages)
S'identifient via ?user=Prénom
Posent des pins sur l'interface
Qualifient leurs commentaires (type)
        ↓
[Firebase]
Synchronisation temps réel des pins
        ↓
[Designer — localhost]
Ouvre le panneau "Retours PO" (bouton jaune)
Voit tous les retours agrégés
Requalifie si nécessaire
Reclassifie vers le bon type
        ↓
Sélectionne les retours à traiter (⚡ éclair)
        ↓
Génère le prompt structuré (onglet Claude)
        ↓
Envoie à Claude via le pont local (server.py)
        ↓
[Claude Code]
Analyse les retours
Challenge les suggestions
Modifie le wireframe HTML directement
        ↓
[Designer]
Les retours envoyés passent en done=true → Archives
        ↓
Nouvelle version créée (V4 → V5)
        ↓
Mise à jour du sélecteur de versions
```

---

### 4.2 Workflow intervenant : déposer un commentaire

```
[PO / Métier]
Reçoit le lien ?user=Prénom
        ↓
Ouvre le wireframe dans son navigateur
        ↓
Clique sur une zone de l'interface
        ↓
Popover s'ouvre → champ texte + sélection type
(Retour / Idée / Règle de gestion / Question)
        ↓
Valide → pin ancré sur l'interface
        ↓
Sauvegarde locale (localStorage) + Firebase
        ↓
Le designer voit le pin en temps réel (sync 5s)
        ↓
Le PO peut voir tous ses propres commentaires
via le panel PO (bouton bas-droite)
```

---

### 4.3 Workflow versionning

```
[Designer]
Travaille sur wireframe-V4.html (fichier actif)
        ↓
Décide de créer un snapshot
        ↓
Copie V4 → V4.1, V4.2, etc. (figé, immuable)
        ↓
Ajoute la nouvelle version dans le sélecteur
        ↓
Continue à travailler sur V4.html
        ↓
À la livraison → renomme en V5.html
        ↓
V5 devient la version de référence publique
        ↓
Mis à jour dans projects.json (sous-projet)
```

---

### 4.4 Workflow Claude

```
[Designer — Panneau Retours PO]
Ouvre l'onglet Claude (⚡)
        ↓
Sélectionne les retours à inclure
(clic sur ⚡ de chaque carte → mise en surbrillance)
        ↓
Le prompt se génère automatiquement en temps réel
        ↓
Vérifie le contenu du prompt
        ↓
Clique "Envoyer à Claude"
        ↓
server.py reçoit la requête POST
        ↓
Copie dans le presse-papier
        ↓
Claude Code reçoit le prompt + modifie le fichier HTML
        ↓
Les retours sélectionnés → done=true (archivés)
        ↓
Journal des modifs : Claude génère une phrase narrative
pour chaque retour archivé
```

---

## 5. ÉCRANS

### 5.1 Login — Loopcraft Studio

**Objectif** : Authentification du designer  
**Utilisateurs** : Designer uniquement  
**Fonctionnalités** :
- Champ Identifiant (`Studio Jailoop`)
- Champ Mot de passe (`Loopcraft`)
- Validation et accès au dashboard

**Note** : Login bypassé si paramètre `?go=dashboard` dans l'URL (retour depuis wireframe).

---

### 5.2 Dashboard Loopcraft Studio

**Objectif** : Vue globale de l'activité — point d'entrée quotidien  
**Utilisateurs** : Designer uniquement  
**URL** : `http://localhost:8765/Loopcraft/studio.html`

**Composants** :

| Zone | Contenu | Données |
|---|---|---|
| **KPIs** × 4 | Projets / Sous-projets / Terminés / Messages non lus | Réel (projects.json + Firebase) |
| **🔴 À traiter** | Retours groupés par type avec badge total | Firebase réel |
| **↗ Reprendre** | Derniers sous-projets, version, date | projects.json |
| **Activité récente** | Timeline avec avatars colorés, type, temps relatif | Firebase réel |
| **Contributions** | Classement auteurs avec barre proportionnelle | Firebase réel |
| **Santé projets** | Par projet : retours, en cours, terminés, barre progression | Croisé réel |

**Actions** :
- Clic sur projet dans la sidebar → ouvre la page projet
- Clic sur sous-projet dans "Reprendre" → ouvre le wireframe
- Bouton "+ Nouveau projet" → modal création

---

### 5.3 Page Projet (ex: Club Med)

**Objectif** : Vue dédiée à un client — liste des sous-projets  
**Utilisateurs** : Designer  
**Navigation** : Sidebar → clic projet, ou clic card dashboard

**Composants** :

| Zone | Contenu |
|---|---|
| **Banner coloré** | Couleur client + logo Ψ + nom + description + chips stats |
| **Grille sous-projets** | Cards avec nom, version, statut, date, bouton accès wireframe |
| **Carte "+ Nouveau sous-projet"** | Création d'un nouveau sous-projet |

**Actions** :
- Clic card sous-projet → ouvre le wireframe dans un nouvel onglet
- Bouton "+ Nouveau sous-projet" → modal création
- Retour dashboard via breadcrumb ou sidebar

---

### 5.4 Wireframe (ex: Télécollecte V5)

**Objectif** : Interface prototype fonctionnelle — espace de travail principal  
**Utilisateurs** : Designer (localhost) + Intervenants (GitHub Pages)  
**URL** : `http://localhost:8765/wireframe-telecollecte-cas1-V5.html`

**Vues fonctionnelles** :

| Onglet | Contenu |
|---|---|
| **Télécollecte** | Tableau de saisie par TPE (5 TPE), modes interfacé/non-interfacé, validation montant + N° remise, bouton "Valider la saisie" |
| **Date antérieure** | Même structure avec colonne régularisation, validation déportée |
| **Régularisation** | Total écart + 3 champs MDP, calcul automatique, bouton conditionnel |

**Composants systèmes** :

| Composant | Position | Accès |
|---|---|---|
| Sidebar navigation | Gauche | Tous |
| Sélecteur de version | Panel Options | Tous |
| Pins de commentaires | Sur l'interface | Tous (dépôt : intervenants) |
| Bouton "Retours PO" | Bas-gauche (jaune) | Designer uniquement (localhost) |
| Bouton "Mes commentaires" | Bas-droite | Intervenants uniquement |
| Panel Options | Bas-droite | Tous |
| ← Retour au dashboard | Panel Options | Tous |

---

### 5.5 Portail PO (portail.html)

**Objectif** : Espace d'accueil des intervenants — accès au wireframe avec identité  
**Utilisateurs** : POs, métier  
**URL** : `https://studiojailoop.github.io/telecollecte-odyssey/portail.html`

**Fonctionnalités** :
- Login avec identité PO (nom)
- Accès au wireframe avec paramètre `?user=Prénom`
- Vue de ses propres commentaires

---

### 5.6 Panel "Retours PO" (Designer uniquement)

**Objectif** : Espace de qualification et d'envoi vers Claude  
**Accès** : Bouton jaune bulle bas-gauche — visible uniquement sur localhost  
**Position** : Tiroir latéral droite (680px)

**Structure** :

```
Header (Navy)
├── Titre "Retours PO"
└── Sous-titre "Notez les retours — copiez pour Claude"

Ligne 1 — Navigation principale
├── ⚡ Claude
├── 💬 Commentaires équipe
└── Switch "Archivés"

Ligne 2 — Types de retours
├── 💬 Retour
├── 💡 Idée
├── 📋 Règle de gestion
└── ❓ Question

Zone contenu (selon onglet actif)
└── Cards de retours avec actions

Footer
├── Champ textarea : retour rapide
└── Boutons : Annuler / ⚡ Envoyer à Claude
```

---

### 5.7 Panel PO (Intervenants uniquement)

**Objectif** : Consultation des propres commentaires de l'intervenant  
**Accès** : Bouton bas-droite avec avatar — visible uniquement hors localhost  

**Contenu** :
- Liste de ses propres commentaires sur ce wireframe
- Identité affichée (connecté en tant que `CURRENT_USER`)
- Date et onglet d'origine de chaque commentaire

---

### 5.8 Popover Nouveau Commentaire

**Objectif** : Dépôt d'un commentaire positionné sur l'interface  
**Déclencheur** : Clic gauche sur le wireframe (mode commentaire actif)

**Champs** :
- Sélecteur auteur (Julie / Nelly / Jérôme / Kirsty / Laurent / Sébastien)
- Textarea commentaire
- Sélecteur type (visible pour les POs) : Retour / Idée / RG / Question
- Boutons : Annuler / Sauvegarder

---

### 5.9 Thread Popover

**Objectif** : Discussion fil sur un pin existant  
**Déclencheur** : Clic sur un pin déjà posé

**Contenu** :
- Message original + auteur + date
- Réponses avec auteur + texte
- Zone "Dernières modifs" (réservée designer)
- Champ réponse + bouton envoyer

---

### 5.10 Panel Corbeille

**Objectif** : Restauration des retours supprimés  
**Accès** : Designer uniquement  
**Rétention** : 30 jours

**Fonctionnalités** :
- Liste des retours supprimés avec date
- Bouton "Restaurer" par élément

---

## 6. SYSTÈME DE COMMENTAIRES

### Création d'un commentaire

1. L'intervenant ouvre le wireframe avec `?user=Prénom`
2. Un clic gauche sur l'interface déclenche l'ouverture du popover
3. L'auteur saisit son texte et sélectionne le type
4. Validation → pin créé à la position exacte du clic

### Stockage et affichage

- Les pins sont stockés en **localStorage** (clé : `wf_comments_telecollecte`)
- Synchronisés vers **Firebase Realtime DB** (URL : `https://studio-jailoop-default-rtdb.firebaseio.com/comments`)
- Le designer voit tous les pins via la sync Firebase (polling toutes les 5s)
- Chaque pin est représenté par un rond coloré avec label numéroté (ex: `1S`, `2L`)

### Couleurs par auteur

| Auteur | Couleur |
|---|---|
| Sébastien | `#1E2643` (Navy) |
| Julie | `#7C3AED` (Violet) |
| Nelly | `#059669` (Vert) |
| Jérôme | `#DC2626` (Rouge) |
| Kirsty | `#0891B2` (Bleu) |
| Laurent | `#D97706` (Orange) |

### Édition et suppression

- **Édition** : Clic sur le pin → thread → modifier le texte (propre message uniquement)
- **Suppression** : Bouton 🗑 sur la carte dans le panel designer → corbeille 30j
- **Restauration** : Panel corbeille → bouton "Restaurer"

### Synchronisation

- Lecture : polling Firebase toutes les 5 secondes
- Écriture : immédiate → localStorage puis Firebase async
- Fallback : si Firebase indisponible → localStorage local maintenu

### Drag & Drop

- Les pins sont déplaçables (drag volontaire > 8px de mouvement)
- Position sauvegardée après déplacement
- Protection anti-sélection-texte pendant le drag

---

### Catégories de commentaires

| Type | Icône | Couleur | Usage |
|---|---|---|---|
| **Retour** | 💬 | Navy `#1E2643` | Feedback fonctionnel, correction d'interface |
| **Idée** | 💡 | Orange `#D97706` | Suggestion d'amélioration, proposition nouvelle fonctionnalité |
| **Règle de gestion** | 📋 | Violet `#7C3AED` | Contrainte métier, règle fonctionnelle à intégrer |
| **Question** | ❓ | Bleu `#0891B2` | Demande de clarification, ambiguïté |
| **Commentaire équipe** | 💬 | Rouge `#D93025` | Discussion interne équipe design/dev |

---

## 7. ESPACE DESIGNER

### Accès

Le panneau "Retours PO" est **exclusivement accessible depuis localhost**. Sur GitHub Pages, il est masqué. Cette restriction est hardcodée :

```javascript
if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') {
  document.getElementById('briefs-nav-btn').style.display = 'flex';
}
```

### Réception des commentaires

Les retours arrivent de deux sources :
1. **Pins Firebase** : commentaires posés par les intervenants sur le wireframe
2. **Briefs manuels** : retours saisis directement par le designer dans le panel

À l'ouverture du panel, les pins Firebase sont automatiquement importés comme briefs si leur type correspond à un type connu.

### Qualification

Chaque retour affiché dans le panel comporte :
- Le texte du retour
- L'auteur
- La date
- Le type (badge coloré)
- Une bordure colorée gauche selon le type

### Requalification

Le designer peut changer le type d'un retour via le bouton ⇄ sur chaque carte. Cela met à jour le badge, la couleur et l'onglet d'appartenance.

### Réécriture IA

Le bouton ↻ sur chaque carte déclenche une réécriture via le pont Claude Code :
1. Un prompt est envoyé à `http://localhost:8765/rewrite-request`
2. Claude reformule le retour de façon plus précise et actionnable
3. La nouvelle formulation remplace le texte original dans la carte

### Filtrage

- Par type : navigation dans les onglets (Retour / Idée / RG / Question)
- Par statut : switch "Archivés" ON/OFF
- Par auteur (dans les pins) : sélecteur dans le panel Options du wireframe

### Mode Archives

Lorsque le switch "Archivés" est activé :
- Les retours `done=false` sont masqués
- Les retours `done=true` (traités) sont affichés
- L'onglet Claude et Commentaires équipe sont masqués
- L'onglet "📋 Journal des modifs" apparaît

### Journal des modifs

Le journal présente les retours archivés sous forme éditoriale :
- Numérotation chronologique
- Texte narratif généré par l'IA ("Le champ date a été rendu non modifiable")
- Formaté comme un compte-rendu d'itération

### Sélection Claude

La sélection Claude est un **Set JavaScript** (`claudeSelection`) contenant les IDs des éléments à inclure dans le prompt :
- Clic sur ⚡ → ajoute/retire l'ID de la sélection
- Compteur en temps réel sur le bouton Claude
- La sélection peut inclure : briefs typés + commentaires équipe + threads pins

---

## 8. ESPACE INTERVENANTS

### Ce que voient les POs et le métier

Lorsqu'un intervenant accède au wireframe via `wireframe-telecollecte-cas1-V5.html?user=Laurent` :

**Visible** :
- Le wireframe complet en mode interactif (onglets, tableaux, boutons)
- Les pins de tous les auteurs sur l'interface
- Le sélecteur de versions (panel Options)
- Son propre bouton "Mes commentaires" (bas-droite)
- Le bouton "← Retour au dashboard" (uniquement si connecté via le portail)

**Non visible** :
- Le bouton jaune "Retours PO" (masqué)
- Les briefs qualifiés du designer
- L'espace Claude
- Le mode Archives

### Panel "Mes commentaires" (intervenants)

Chaque intervenant a accès à ses propres commentaires via le bouton bas-droite :
- Affiche uniquement ses pins (filtrés par `CURRENT_USER`)
- Permet de revoir le texte et le contexte de chaque commentaire
- Ne permet pas de voir les commentaires des autres

### Ce qu'ils ne peuvent pas faire

- Voir les retours qualifiés dans le panel designer
- Accéder à l'espace Claude
- Modifier les retours d'autres utilisateurs
- Changer le statut (done / not done) des retours
- Créer des versions
- Accéder au dashboard Loopcraft Studio

---

## 9. ESPACE CLAUDE

### Principe

L'espace Claude est l'interface de **transmission des retours vers l'IA**. Il transforme une sélection de retours humains en un prompt structuré, contextualisé, et l'envoie directement à Claude Code via un pont HTTP local.

### Accès

Onglet **⚡ Claude** dans le panel "Retours PO" — accessible uniquement en mode non-archivé.

### Ajout d'un retour à la sélection

Sur chaque carte de retour, le bouton **⚡** (éclair) :
- Ajoute l'ID du retour dans `claudeSelection` (Set JavaScript)
- Colore la carte en surbrillance (border-left accentué)
- Met à jour le compteur sur l'onglet Claude

Les threads de pins peuvent également être sélectionnés (filtrage : exclut l'auteur Sébastien pour ne garder que les retours externes).

### Suppression de la sélection

- Reclique sur ⚡ → retire de la sélection
- Ou clic "Tout désélectionner" dans l'onglet Claude

### Génération du prompt

Automatique et en temps réel : dès qu'un élément est sélectionné ou désélectionné, le prompt se régénère dans la textarea de l'onglet Claude.

### Envoi

Bouton **"⚡ Envoyer à Claude"** :
1. Envoie le prompt via `POST http://localhost:8765/send-to-claude`
2. `server.py` copie le contenu dans le presse-papier
3. Claude Code récupère le prompt et exécute les modifications
4. Les retours sélectionnés passent en `done=true` → archivés

### Règle critique d'archivage

```
UNIQUEMENT les briefs dans claudeSelection → done=true
JAMAIS briefs.forEach(b => b.done=true)
```

---

## 10. GÉNÉRATION DE PROMPTS

### Structure du prompt généré

Le prompt est composé de 4 sections structurées :

```
─── CONTEXTE ───────────────────────────────────────────

Je travaille sur le wireframe "fichier.html" — interface de saisie 
des télécollectes TPE pour le projet Odyssey / Club Med.
Ce wireframe est construit sur le Design System Trident Ψ 2.0 et 
Odyssey 2.0. Toute modification doit impérativement respecter ces deux DS.

J'ai collecté N retours (X Retours, Y Idées, Z RG) auprès de mon équipe 
et de mes POs.
Avant d'appliquer quoi que ce soit, je te demande de synthétiser ces 
retours en les challengeant avec ton expertise UX/UI.

─── RETOURS COLLECTÉS ──────────────────────────────────

💬 RETOURS (N)
1. [Localisation] Texte du retour — Auteur
2. ...

💡 IDÉES (N)
1. ...

📋 RÈGLES DE GESTION (N)
1. ...

❓ QUESTIONS (N)
1. ...

─── TA MISSION ─────────────────────────────────────────

En tant qu'expert design de niveau mondial :
1. Synthétise et challenge ces retours
2. Pour chaque retour retenu, propose la meilleure solution UX/UI
3. Identifie les règles de gestion à intégrer dans la logique fonctionnelle
4. Si un retour est ambigu → pose la question avant d'appliquer
5. Applique directement les modifications validées dans le fichier cible

─── INSTRUCTIONS D'APPLICATION ─────────────────────────

Fichier cible : /chemin/vers/wireframe-V5.html

Règles strictes :
• Respecter le Design System Trident Ψ 2.0 et Odyssey 2.0
• Si une RG impacte un comportement → intégrer dans la logique JS
• Pas de régression
• Confirmer chaque modification appliquée
• Si arbitrage nécessaire → poser la question
```

### Traitement des données

Les retours sélectionnés sont regroupés par type, puis ordonnés :
1. Retours
2. Idées
3. Règles de gestion
4. Questions

Chaque retour inclut :
- Sa localisation (label du pin ou onglet d'origine)
- Le texte du retour
- L'auteur (si différent du designer)

### Exemple de prompt généré

```
─── CONTEXTE ───────
Je travaille sur le wireframe "wireframe-telecollecte-cas1-V5.html"...
J'ai collecté 3 retours (2 Retours, 1 Règle de gestion).

─── RETOURS COLLECTÉS ───────
💬 RETOURS (2)
1. [TPE 1] Si le montant est mis en interfacé le numero doit etre mis egalement — Sébastien
2. [Régularisation] Bouton a remettre bien pour lancer la régularisation — Sébastien

📋 RÈGLES DE GESTION (1)
1. Régularisation possible que pour les Financial manager. — Sébastien
```

---

## 11. MODÈLE DE DONNÉES

### Projet

```json
{
  "id": "club-med",
  "name": "Club Med",
  "color": "#0057A8",
  "description": "Refonte de l'outil Odyssey pour les équipes Club Med",
  "subprojects": []
}
```

| Propriété | Type | Description |
|---|---|---|
| `id` | string | Identifiant unique kebab-case |
| `name` | string | Nom du client |
| `color` | string | Couleur hex pour l'identité visuelle |
| `description` | string | Contexte du projet |
| `subprojects` | Array\<SousProjet\> | Liste des sous-projets |

**Relations** : contient N sous-projets

---

### Sous-Projet

```json
{
  "id": "telecollecte",
  "name": "Télécollecte",
  "status": "in_progress",
  "wireframe": "../wireframe-telecollecte-cas1-V5.html",
  "version": "V5",
  "updated": "2026-05-21"
}
```

| Propriété | Type | Description |
|---|---|---|
| `id` | string | Identifiant unique |
| `name` | string | Nom du sous-projet / feature |
| `status` | `in_progress` \| `done` | Statut de progression |
| `wireframe` | string | Chemin relatif vers le fichier HTML |
| `version` | string | Version courante (ex: V5) |
| `updated` | string | Date dernière mise à jour (ISO) |

**Relations** : appartient à 1 Projet, pointe vers 1 Wireframe

---

### Commentaire (Pin Firebase)

```json
{
  "id": "pin-1716285600000",
  "author": "Julie",
  "text": "Le bouton Valider devrait être disabled si le montant est vide",
  "type": "retour",
  "tab": "tpe",
  "x": 847,
  "y": 312,
  "date": "2026-05-21",
  "timestamp": 1716285600000,
  "replies": [
    {
      "author": "Sébastien",
      "text": "Oui, à intégrer en V5",
      "date": "2026-05-21"
    }
  ]
}
```

| Propriété | Type | Description |
|---|---|---|
| `id` | string | Identifiant unique horodaté |
| `author` | string | Prénom de l'auteur |
| `text` | string | Contenu du commentaire |
| `type` | `retour` \| `idee` \| `rg` \| `question` | Catégorie |
| `tab` | string | Onglet d'origine (tpe / ant / reg) |
| `x`, `y` | number | Position absolue en px sur `.content` |
| `date` | string | Date de création |
| `timestamp` | number | Unix timestamp ms |
| `replies` | Array | Réponses du thread |

**Stockage** : localStorage + Firebase Realtime DB  
**Clé localStorage** : `wf_comments_telecollecte`  
**Firebase URL** : `https://studio-jailoop-default-rtdb.firebaseio.com/comments`

---

### Brief (Retour Designer)

```json
{
  "id": 1716285600001,
  "author": "Sébastien",
  "text": "Date non modifiable, juste indicatif",
  "type": "rg",
  "date": "2026-05-21",
  "time": "14:35",
  "done": false,
  "pinLabel": "3S",
  "sourcePin": 1716285600000,
  "tab": "tpe",
  "journalText": "La date de télécollecte a été rendue non modifiable."
}
```

| Propriété | Type | Description |
|---|---|---|
| `id` | number | Identifiant unique |
| `author` | string | Auteur du retour |
| `text` | string | Contenu qualifié |
| `type` | string | Type qualifié par le designer |
| `done` | boolean | `true` = archivé après envoi à Claude |
| `pinLabel` | string | Label du pin source (si issu d'un pin) |
| `sourcePin` | number | ID du pin d'origine |
| `journalText` | string | Texte narratif IA du journal |

**Stockage** : localStorage uniquement (côté designer)  
**Clé localStorage** : `wf_briefs_telecollecte`

---

### Prompt

Structure non persistée — générée à la volée par `generatePrompt()`.

```json
{
  "context": "...",
  "retours": [],
  "idees": [],
  "rg": [],
  "questions": [],
  "mission": "...",
  "targetFile": "wireframe-telecollecte-cas1-V5.html"
}
```

---

### Utilisateur (côté wireframe)

```json
{
  "name": "Laurent",
  "initials": "L",
  "color": "#D97706",
  "source": "URL param ?user=Laurent"
}
```

Pas d'objet persisté — construit à partir du paramètre URL à chaque session.

---

## 12. ARCHITECTURE TECHNIQUE

### Stack

| Couche | Technologie | Rôle |
|---|---|---|
| **Interface** | HTML/CSS/JS inline | Zero dépendance — portabilité maximale |
| **Design System** | Trident Ψ 2.0 + Odyssey 2.0 | Composants UI Club Med / Figma |
| **Persistance locale** | localStorage | Briefs, pins, préférences |
| **Sync temps réel** | Firebase Realtime DB | Commentaires partagés |
| **Serveur local** | Python 3 (server.py) | Pont Claude Code ↔ navigateur |
| **Hébergement** | GitHub Pages | Portail PO public |
| **IA** | Claude Code (CLI) | Modifications wireframe |
| **Dashboard** | HTML/CSS/JS (studio.html) | Interface designer |
| **Données projets** | JSON (projects.json) | Structure projets/sous-projets |

---

### Organisation des fichiers

```
/Claude Yaki/
├── server.py                          → Serveur HTTP local (port 8765)
├── portail.html                       → Portail d'accès PO (public)
├── wireframe-telecollecte-cas1-V1.html → Version 1
├── wireframe-telecollecte-cas1-V2.html → Version 2
├── wireframe-telecollecte-cas1-V3.html → Version 3
├── wireframe-telecollecte-cas1-V4.html → Version active (travail)
├── wireframe-telecollecte-cas1-V4-REF.html → Référence immuable
├── wireframe-telecollecte-cas1-V5.html → Version livrée (actuelle)
├── wireframe-telecollecte-cas1-V4.1/4.2/4.3.html → Snapshots intermédiaires
│
└── Loopcraft/
    ├── studio.html                    → Dashboard designer
    ├── logo-jailoop.png               → Logo Studio Jailoop
    └── data/
        └── projects.json             → Données projets/sous-projets
```

---

### Serveur local (server.py)

Le serveur Python expose 6 routes HTTP sur le port 8765 :

| Route | Méthode | Rôle |
|---|---|---|
| `GET /rewrite-result` | GET | Polling — retourne le résultat de réécriture IA |
| `GET /get-journal-text/:id` | GET | Polling — retourne le texte journal narratif |
| `POST /rewrite-request` | POST | Reçoit une demande de réécriture → transmet à Claude Code |
| `POST /send-to-claude` | POST | Reçoit le prompt → copie dans le presse-papier |
| `POST /save-journal-text` | POST | Sauvegarde le texte journal reformulé |
| `POST /reset-briefs-done` | POST | Réinitialise done=false (urgence) |

Le serveur sert également les fichiers statiques (HTML, images, JSON).

---

### Stockage Firebase

- **Type** : Firebase Realtime Database
- **URL** : `https://studio-jailoop-default-rtdb.firebaseio.com/comments`
- **Format** : objet JSON indexé par ID
- **Sync** : polling côté designer (5s), écriture immédiate côté intervenants
- **Accès** : public (lecture/écriture sans auth — prototype)

---

### Identification des utilisateurs

Les intervenants sont identifiés par un paramètre URL :

```
wireframe-telecollecte-cas1-V5.html?user=Laurent
```

- Prénom récupéré via `URLSearchParams`
- Utilisé comme `CURRENT_USER` pour tous les commentaires de la session
- Sans paramètre → défaut : `Éric`
- Designer identifié par accès localhost (pas de paramètre)

---

## 13. ROADMAP POTENTIELLE

### 🟢 Faible effort / Fort impact

| Fonctionnalité | Description | Impact |
|---|---|---|
| **Statut par sous-projet** | Toggle En cours / Done depuis la page projet | Suivi visuel immédiat |
| **Persistance Firebase des briefs** | Migrer localStorage → Firebase pour cross-device | Designer mobile possible |
| **Notifications en temps réel** | Badge sur le dashboard si nouveau commentaire PO | Réactivité |
| **Export PDF du prompt** | Sauvegarder le prompt généré en PDF | Traçabilité réunion |
| **Filtre par auteur dans le dashboard** | Voir l'activité d'un PO spécifique | Gestion multiclients |
| **Lien partageable par sous-projet** | URL directe vers un sous-projet spécifique | Onboarding PO |

---

### 🟡 Effort moyen

| Fonctionnalité | Description | Impact |
|---|---|---|
| **Authentification Firebase** | Login sécurisé pour les intervenants | Sécurité + multi-projets |
| **Historique des prompts** | Conserver tous les prompts envoyés à Claude | Traçabilité complète |
| **Statut des retours modifiables par PO** | PO peut marquer un retour "traité" | Collaboration bidirectionnelle |
| **Vue Kanban des retours** | Retours en colonnes : À traiter / En cours / Done | Pilotage plus visuel |
| **Multi-wireframes par sous-projet** | Plusieurs fichiers HTML par sous-projet | Scale multi-écrans |
| **Commentaires intégrés au dashboard** | Répondre à un thread depuis le dashboard | Centralisation |
| **Dark mode** | Dashboard + wireframe en dark | Confort designer |

---

### 🔴 Gros chantiers

| Fonctionnalité | Description | Impact |
|---|---|---|
| **Backend Node.js / API REST** | Remplacer server.py + localStorage par une vraie API | Scale, multi-users, SaaS |
| **Intégration Claude API** | Appels directs à l'API Anthropic (sans CLI) | Automatisation totale |
| **Versionning automatique** | Snapshot automatique avant chaque modification IA | Sécurité + historique |
| **Diff visuel entre versions** | Comparaison avant/après côte à côte | Revue d'itération |
| **Espace Design Tokens** | Gestion des tokens du DS directement dans Loopcraft | Cohérence DS |
| **Multi-tenant** | Plusieurs designers/studios indépendants | SaaS |
| **Intégration Figma** | Import/export composants Figma ↔ wireframe | Workflow design |
| **Génération de wireframe par IA** | Créer un wireframe depuis un brief textuel | 0 to 1 accéléré |
| **Mobile app** | Dashboard mobile pour suivre l'activité | Mobilité |

---

## 14. RÉSUMÉ EXÉCUTIF

### Qu'est-ce que Loopcraft ?

Loopcraft est un **outil de collaboration design-product-IA** qui connecte un wireframe interactif, les retours des intervenants et l'intelligence artificielle dans un workflow unifié.

### Comment ça fonctionne ?

1. **Le designer crée un wireframe** construit sur le Design System Trident Ψ 2.0 / Odyssey 2.0
2. **Il partage un lien** aux POs et utilisateurs métier
3. **Les intervenants posent des commentaires typés** (Retour / Idée / Règle de gestion / Question) directement sur l'interface, à la position exacte
4. **Le designer qualifie ces retours** dans son espace dédié, les reclassifie, les priorise
5. **Il sélectionne les retours à traiter** et génère un prompt structuré
6. **Claude Code reçoit le prompt** et modifie directement le fichier HTML du wireframe
7. **Les retours traités sont archivés** avec un journal narratif généré par l'IA
8. **Une nouvelle version est créée** — le cycle recommence

### Ce qui rend Loopcraft unique

- **Commentaires positionnés** sur l'interface — pas dans un outil séparé
- **Prompt generation structurée** — les retours bruts deviennent un brief IA complet avec contexte, DS et règles d'application
- **Boucle fermée** — du retour humain à la modification appliquée, tout reste dans le même système
- **Traçabilité complète** — chaque retour, chaque décision, chaque version sont conservés
- **Design System enforced** — le prompt impose le respect du DS à Claude
- **Zero friction** — aucun outil tiers, aucun copier-coller entre Slack/Notion/Figma

### Fonctionnalités principales

| Fonctionnalité | Statut |
|---|---|
| Wireframe interactif multi-vues | ✅ Livré |
| Commentaires positionnés partagés (Firebase) | ✅ Livré |
| Catégorisation des retours (4 types) | ✅ Livré |
| Qualification et requalification | ✅ Livré |
| Sélection Claude + génération prompt | ✅ Livré |
| Envoi à Claude via pont local | ✅ Livré |
| Archives + Journal des modifs IA | ✅ Livré |
| Versionning avec sélecteur intégré | ✅ Livré |
| Dashboard SaaS (Loopcraft Studio) | ✅ Livré |
| Architecture Projet > Sous-projet | ✅ Livré |
| Portail PO public (GitHub Pages) | ✅ Livré |
| Authentification Firebase | 🔜 Roadmap |
| API backend | 🔜 Roadmap |

### Utilisateurs cibles

- **Studio de design** souhaitant industrialiser la collaboration avec ses clients
- **Product Designers** travaillant sur des projets à forte composante IA
- **Agences UX** gérant plusieurs clients simultanément
- **Product teams** cherchant à réduire les frictions entre retours et livraison

---

*Document généré le 21 mai 2026 — Studio Jailoop*  
*Ce document est vivant et doit être mis à jour à chaque nouvelle itération majeure.*
