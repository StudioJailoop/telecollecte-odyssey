# Loopcraft — Foundation Document v1

> Document de capitalisation stratégique.  
> Rédigé le 2026-06-01.  
> Auteur : Sébastien Keller / Studio Jailoop  
> Ce document est indépendant de tout projet client. Il décrit Loopcraft comme produit.

---

## Table des matières

1. [Vision produit](#1-vision-produit)
2. [Concepts fondamentaux](#2-concepts-fondamentaux)
3. [Fonctionnalités cœur](#3-fonctionnalités-cœur)
4. [Ce qui est spécifique à Club Med / Télécollecte](#4-ce-qui-est-spécifique-à-club-med--télécollecte)
5. [Architecture SaaS cible](#5-architecture-saas-cible)
6. [Branding Loopcraft](#6-branding-loopcraft)
7. [Plan de migration — nouvelle instance](#7-plan-de-migration--nouvelle-instance)

---

## 1. Vision produit

### En une phrase

**Loopcraft est l'outil qui permet à un designer et à Claude de co-construire des wireframes interactifs, en boucle avec les retours de l'équipe.**

### Le problème résolu

Dans un projet de conception, la collaboration entre un designer, ses équipes métier et un Product Owner est fragmentée :
- Les retours arrivent par email, Slack, réunion, Figma — sans structure
- Le designer perd du temps à trier, prioriser, reformuler
- Les équipes ne savent pas si leurs retours ont été pris en compte
- L'IA (Claude) ne peut pas agir sans un brief clair

Loopcraft résout ce problème en créant un **flux structuré et continu**, dans les deux sens :

```
Brief initial → Claude génère le wireframe
     ↓
Équipe commente (pings)
     ↓
Designer qualifie → Brief suivant → Claude itère
     ↓
(boucle)
```

Claude n'est pas seulement celui qui modifie — il est celui qui **construit dès le départ**. Le wireframe naît d'un brief, pas d'une page blanche dessinée à la main.

### Qui est concerné

| Profil | Rôle dans Loopcraft | Ce qu'il gagne |
|--------|---------------------|----------------|
| **Designer** | Pilote l'outil. Qualifie les retours, envoie les briefs à Claude | Gagne en clarté, vitesse, traçabilité |
| **PO / PM** | Dépose des retours sur les wireframes. Consulte le portail | Ses retours sont pris en compte et tracés |
| **Métier / Équipe** | Dépose des retours (pings) directement sur les wireframes | Interface intuitive, pas d'outil supplémentaire |
| **Client / Observateur** | Consulte le portail en lecture seule | Visibilité sur l'avancement |

### Télécollecte = cas de validation, pas le produit

Télécollecte (Club Med) est le **premier projet hébergé dans Loopcraft**. Il a permis de valider le concept et de construire les bases du produit. Ce n'est pas Loopcraft. C'est un client de Loopcraft.

---

## 2. Concepts fondamentaux

### Workspace

L'**instance Loopcraft**. Correspond à une organisation ou un studio.  
Exemple : *Studio Jailoop*

Un workspace contient tous les projets. Il définit :
- Les utilisateurs autorisés (designers, POs, observateurs)
- La Firebase utilisée
- L'identité visuelle de l'interface

### Projet

Un **client ou domaine de travail** au sein du workspace.  
Exemples : *Club Med*, *DDJ*, *Mangas.io*, *Projet perso*

Un projet contient plusieurs sous-projets. Il a un nom, une couleur, une description.

### Sous-projet

Une **fonctionnalité, un flux, une feature** au sein d'un projet.  
Exemples : *Télécollecte*, *Dashboard participants*, *Inscription week-end*, *Parcours achat*

Un sous-projet pointe vers un wireframe. Il a un statut (en cours / terminé), une version courante, une date de mise à jour.

### Wireframe

Le **fichier interactif** associé à un sous-projet. Fichier HTML autonome, sans dépendances externes.  
Il contient : la maquette cliquable + le système de pings + l'espace designer + les règles de gestion simulées.

**Un wireframe ne se dessine pas à la main. Il est généré par Claude à partir d'un brief, puis itéré.**

Quand un sous-projet est créé dans Loopcraft, il n'existe pas encore de wireframe. Le designer envoie un premier brief, Claude génère la coquille HTML, et les itérations suivantes s'appuient sur les pings de l'équipe.

Les wireframes sont versionnés (V1, V2, V3…). Chaque version est un fichier figé. Seule la version active est modifiable.

### Commentaire / Ping

Un **retour déposé sur le wireframe** par un membre de l'équipe.  
Il est positionné sur l'interface (coordonnées x/y), catégorisé, et identifié par auteur.

Catégories :
- `retour` — observation, problème constaté
- `idee` — suggestion d'amélioration
- `rg` — règle de gestion ou contrainte métier
- `question` — interrogation qui nécessite une réponse

Chaque commentaire peut contenir des **réponses** (thread). Il est synchronisé en temps réel via Firebase.

### Brief

Un commentaire **qualifié par le designer** et intégré dans son espace de travail.  
Le designer décide quels pings méritent de devenir des briefs. Un brief est le matériau de travail du designer.

Un brief peut être :
- En cours (actif dans le flux)
- Archivé (traité, envoyé à Claude et appliqué)

### Prompt Claude

Une **sélection de briefs** assemblée par le designer, transformée en instructions structurées pour Claude Code.  
Le prompt est envoyé via le serveur local au terminal Claude Code. Claude applique les modifications sur le wireframe.

Il y a deux types de prompts :
- **Prompt de génération** — premier brief d'un sous-projet. Claude crée le wireframe depuis zéro dans la coquille vide.
- **Prompt d'itération** — briefs suivants, basés sur les pings de l'équipe. Claude modifie ce qui existe sans tout réécrire.

### Version

Un **snapshot figé** d'un wireframe à un instant T. Nommé selon le format `VX.Y`.  
Un fichier versionné n'est **jamais modifié**. Seul le fichier actif évolue.  
Le versionnage permet de revenir en arrière en cas de régression.

### Archive

Un brief passé à l'état `done = true`. Il sort du flux actif et est consultable dans le **mode archives**.  
L'archivage est une action manuelle et contrôlée. On n'archive jamais en masse automatiquement.

---

## 3. Fonctionnalités cœur

Ces fonctionnalités appartiennent à Loopcraft et peuvent servir pour **n'importe quel projet**.

### Coquille wireframe (point de départ d'un sous-projet)
Quand un sous-projet est créé, Loopcraft génère une **coquille HTML vide** contenant uniquement :
- Le système de pings (Firebase, dépôt, threads)
- L'espace designer (briefs, qualification, envoi Claude)
- Le panel Règles de gestion
- La navigation de base et le header

Aucun contenu métier. Claude remplit cette coquille à partir du premier brief.

### Dashboard multi-projets
- Vue d'ensemble de tous les projets du workspace
- KPIs : nombre de sous-projets, retours en attente, progression globale
- Accès rapide à chaque sous-projet

### Gestion projets / sous-projets
- Création, édition, suppression de projets et sous-projets
- Sélection d'une couleur et d'un statut
- Association d'un wireframe URL à un sous-projet

### Système de pings (commentaires)
- Dépôt de retours positionnés sur le wireframe (clic + placement)
- Catégorisation : Retour / Idée / RG / Question
- Label automatique : R1, R2, I1, RG1, Q1…
- Couleur par auteur (identité visuelle de l'équipe)
- Thread de réponses par ping
- Synchronisation Firebase temps réel
- Affichage filtré : pings actifs vs pings archivés

### Espace designer (qualification des retours)
- Modale dédiée accessible depuis le wireframe
- 4 onglets : Retour / Idée / RG / Question
- Visualisation et tri des briefs par catégorie
- Drag & drop pour réordonner les priorités
- Archivage individuel d'un brief

### Génération de prompt Claude
- Sélection de briefs à envoyer (checkboxes)
- Assemblage automatique d'un prompt structuré
- Envoi via server.py au terminal Claude Code
- Historique des prompts envoyés (journal)

### Portail PO (GitHub Pages)
- Page web publique pour les POs et le métier
- Accès aux wireframes en lecture ou en mode commentaire
- Pas d'installation requise — juste un lien

### Versionnage des wireframes
- Snapshot manuel avant chaque évolution majeure
- Fichier snapshot figé, nommé selon convention
- Sélecteur de version dans le wireframe lui-même

### Mode Archives
- Bascule globale entre flux actif et archives
- Briefs archivés consultables mais non éditables
- Badges respectent le mode courant

### Sync Firebase + localStorage
- Firebase = source de vérité pour les pings (temps réel, multi-utilisateurs)
- localStorage = cache local pour les briefs designer (évite la perte en offline)
- Reconciliation automatique au chargement

---

## 4. Ce qui est spécifique à Club Med / Télécollecte

Ces éléments **ne doivent pas être repris tels quels** dans une nouvelle instance.

### Dans studio.html

| Élément | Valeur actuelle | À faire pour la nouvelle instance |
|---------|-----------------|-----------------------------------|
| Credentials | Laurent, Nelly, Julie, Eric, Tiphaine, Florian / pwd "Ody26" | Remplacer par les utilisateurs du nouveau workspace |
| Firebase comments URL | `…/comments.json` | Créer un nouveau nœud `/projects/{workspaceId}/comments` |
| Firebase briefs URL | `…/briefs_telecollecte.json` | Génériciser en `/projects/{projectId}/briefs` |
| Logo Club Med | SVG Trident Ψ | Remplacer par logo du projet concerné |
| Fallback project data | `{id: "club-med", subprojects: [{id: "telecollecte"}]}` | Remplacer par les projets du nouveau workspace |
| localStorage key | `wf_briefs_telecollecte` | Génériciser en `wf_briefs_{subprojectId}` |

### Dans les wireframes

| Élément | Description |
|---------|-------------|
| Wording métier | "Télécollecte", "TPE", "N° Remise", "Caisse ouverte", "Montant calculé" |
| Design System | Odyssey / Trident Ψ 2.0 — spécifique Club Med |
| Données simulées | Montants, noms de caisses, types de paiement |
| Logique RG | Règles de gestion spécifiques à la Télécollecte |

### Dans les docs / config

| Fichier | Ce qui est spécifique |
|---------|----------------------|
| CLAUDE.md | Instructions DS Odyssey, règles Trident 2.0 |
| ARCHITECTURE.md | Référence à Télécollecte partout |
| agents/*.md | Recette Club Med, naming DS Odyssey |
| memory/ | Figma Odyssey, utilisateurs Club Med |

### Ce qu'il faut conserver — c'est Loopcraft, pas Club Med

- La structure HTML/CSS/JS du dashboard (`studio.html`)
- Le système de polling Firebase
- Le mécanisme de creation de projets/sous-projets
- Le server.py (routes génériques)
- Le pattern de sync localStorage ↔ Firebase
- Le système de versionnage des wireframes

---

## 5. Architecture SaaS cible

### Hiérarchie

```
Workspace
└── Projet
    └── Sous-projet
        └── Wireframe (V1, V2, V3…)
            ├── Pings / Commentaires (Firebase temps réel)
            ├── Briefs (localStorage + Firebase)
            └── Prompts Claude (server.py)
```

### Exemple concret

```
Studio Jailoop (workspace)
├── Club Med (projet)
│   ├── Télécollecte (sous-projet) → wireframe-telecollecte-V4.html
│   ├── Date antérieure (sous-projet) → wireframe-date-anterieure-V1.html
│   └── Régularisation (sous-projet) → wireframe-regularisation-V1.html
│
├── DDJ (projet)
│   ├── Dashboard participants (sous-projet) → wireframe-ddj-dashboard-V1.html
│   ├── Inscription week-end (sous-projet) → wireframe-ddj-inscription-V1.html
│   └── Backoffice (sous-projet) → wireframe-ddj-backoffice-V1.html
│
└── Projet perso (projet)
    └── App mobile (sous-projet) → wireframe-app-V1.html
```

### Firebase — structure data cible

```
/{workspaceId}/
  ├── /projects/{projectId}/comments/{commentId}
  ├── /projects/{projectId}/subprojects/{subprojectId}/briefs/{briefId}
  └── /users/{userId}
```

Aujourd'hui : tout est dans `/comments` et `/briefs_telecollecte` sans isolation par projet.  
Cible : chaque projet a son propre espace isolé dans Firebase.

### Configuration par instance

Une nouvelle instance Loopcraft = un fichier `config.js` (ou une section `const CONFIG` dans studio.html) contenant :

```javascript
const CONFIG = {
  workspaceName: "Studio Jailoop",
  firebaseUrl: "https://mon-projet-rtdb.firebaseio.com",
  users: [
    { id: "sebastien", pw: "monpwd", role: "Designer" },
    { id: "collaborateur", pw: "pwd2", role: "PO" }
  ],
  projects: [] // chargés dynamiquement ou définis ici
};
```

---

## 6. Branding Loopcraft

### Nom

**Loopcraft**

- **Loop** → l'itération, le cycle retour → modification → retour
- **Craft** → la fabrication, le soin apporté à la conception
- Ensemble : "l'outil qui fabrique par itération"

Domaine possible : `loopcraft.studio` / `loopcraft.design` / `loopcraft.app`

### Positionnement

> *Loopcraft connecte les retours de votre équipe aux modifications de vos wireframes, assisté par IA.*

Ce n'est pas un outil de wireframing (Figma fait ça).  
Ce n'est pas un outil de feedback (Notion/Slack font ça).  
Ce n'est pas un assistant IA générique (ChatGPT fait ça).  
C'est **l'atelier de conception collaborative** — le designer pilote, l'équipe commente, Claude exécute.

### Palette cible

Neutre, SaaS B2B, ni Club Med ni Studio perso actuel.

| Rôle | Couleur | Hex |
|------|---------|-----|
| Fond principal | Blanc cassé | `#F8F9FB` |
| Primaire (texte, nav) | Bleu nuit profond | `#1E2647` |
| Accent (CTA, highlights) | Jaune doré | `#F5BE00` |
| Succès | Vert | `#22C55E` |
| Erreur | Rouge | `#E24A3B` |
| Secondaire (badges, muted) | Gris neutre | `#6B7280` |

### Logo — direction

Concept : une boucle stylisée qui forme un outil (clé, crayon ou aiguille).  
Évocation : itération + construction.  
Style : minimaliste, monochrome, adapté au favicon et à l'en-tête d'un SaaS.

À NE PAS faire : reprendre le bleu Club Med `#0057A8` ou le trident Ψ.

### Différenciation

| Concurrent perçu | Ce que Loopcraft fait différemment |
|------------------|------------------------------------|
| Figma Comments | Les retours sont qualifiés en briefs, pas juste collectés |
| Notion / Jira | Pas de tickets — les retours restent connectés au wireframe |
| ChatGPT / Claude.ai | Claude agit directement sur le fichier dans une boucle structurée |
| Zeplin / Storybook | Orienté processus de collaboration, pas specs statiques |
| v0 / Bolt | Le designer pilote chaque itération — l'IA ne décide pas seule |

---

## 7. Plan de migration — nouvelle instance

Checklist pour créer une instance Loopcraft indépendante de Club Med.

### Prérequis

- [ ] Compte GitHub personnel (Studio Jailoop perso, pas le compte Club Med)
- [ ] Compte Firebase personnel (nouveau projet Firebase)
- [ ] Compte Anthropic / Claude API (pour la session perso)

### Étapes

**1. Nouveau repository GitHub**
```
Nom : loopcraft-studio (ou loopcraft-{workspace})
Visibilité : private (puis public quand prêt)
Brancher GitHub Pages sur main/
```

**2. Copier les fichiers sources**
```
studio.html          → point de départ du dashboard
server.py            → serveur local (identique, port 8765)
wireframe-template.html → à créer : wireframe vierge sans Club Med
```

**3. Dans studio.html — 4 remplacements**
```javascript
// Remplacer :
const CREDENTIALS = [...]       // → utilisateurs du nouveau workspace
const FB_URL = "..."            // → nouvelle Firebase URL /comments
const FB_BRIEFS_URL = "..."     // → nouvelle Firebase URL /briefs
// Données projet par défaut    // → projets du nouveau workspace
```

**4. Nouveau Firebase**
- Créer un projet Firebase
- Activer Realtime Database
- Copier l'URL du Realtime Database
- Remplacer dans studio.html et dans les wireframes

**5. Nouveau CLAUDE.md**
- Sans référence à Odyssey / Trident 2.0
- Sans règles spécifiques Télécollecte
- Garder la structure (démarrage, règles absolues, anti-régression)

**6. Premier projet de test : DDJ**
- Créer un sous-projet DDJ dans le nouveau studio
- Écrire le premier brief : "Crée un dashboard de gestion des participants DDJ avec liste, statuts et actions principales"
- Claude génère le wireframe dans la coquille vide
- Inviter un collaborateur à déposer des pings
- Qualifier → brief suivant → Claude itère
- Vérifier le cycle complet : brief → génération → ping → brief → itération

**7. Vérifier l'isolation**

S'assurer que les deux instances n'interfèrent jamais :

| | Instance Club Med | Instance perso |
|--|------------------|----------------|
| GitHub | `StudioJailoop/telecollecte-odyssey` | `StudioJailoop/loopcraft-studio` |
| Firebase | `studio-jailoop-default-rtdb` | `loopcraft-perso-rtdb` (nouveau) |
| localStorage | clés avec suffixe `_telecollecte` | clés avec suffixe `_{subprojectId}` |
| Port serveur | 8765 | 8765 (pas de conflit si lancés séparément) |

---

## Notes pour la prochaine session

Quand tu veux démarrer la migration :

1. Lire ce document en entier
2. Lire `Loopcraft/LOOPCRAFT_PRODUCT_DOCUMENTATION.md` pour les détails techniques
3. Créer le repo GitHub perso
4. Créer le projet Firebase perso
5. Commencer par l'étape 3 ci-dessus (les 4 remplacements dans studio.html)

**Ce document ne doit pas être poussé sur le repo Club Med.**  
Il vit dans Dropbox, dans `Docs/Loopcraft/`, accessible localement.

---

*Loopcraft Foundation v1 — 2026-06-01*
