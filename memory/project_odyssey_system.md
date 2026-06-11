---
name: Système complet Wireframe + Outil PO Odyssey
description: Architecture complète du système de wireframes interactifs et de l'outil de collaboration PO — réutilisable pour tout nouveau projet
type: project
originSessionId: 9f8442c3-4d5c-4465-87b8-99549a3d219e
---
## Contexte
Projet Club Med / Odyssey — wireframes HTML interactifs avec système de collaboration PO intégré.
Réutilisable pour tout nouvel écran ou module.

---

## Stack technique
- **HTML/CSS/JS** inline dans un seul fichier — zéro dépendance
- **Firebase Realtime Database** — commentaires partagés en temps réel
- **GitHub Pages** — hébergement public du portail PO
- **server.py** — serveur local Python qui fait le pont avec Claude Code
- **localStorage** — persistance locale (briefs, corbeille, pins)

---

## Fichiers du projet
```
~/Desktop/Claude Yaki/
├── server.py                          ← Serveur local (TOUJOURS utiliser, pas http.server)
├── portail.html                       ← Portail d'accès PO (index.html sur GitHub)
├── wireframe-[sujet]-V3.html          ← Fichier de travail courant
├── wireframe-[sujet]-V1.html          ← V1 figée
├── wireframe-[sujet]-V2.html          ← V2 figée
└── CLAUDE.md                          ← Documentation projet
```

---

## Démarrage serveur
```bash
cd "/Users/sebastienkeller/Desktop/Claude Yaki"
python3 server.py
# → http://localhost:8765
```

---

## Architecture du wireframe

### Layout Odyssey DS exact
- **Header** : navy `#1E2643`, logo SVG, search pill, Scan Bracelet jaune, What's new, avatar
- **Sidebar** : 292px ouverte / 94px fermée (closed par défaut), toggle cercle
- **Main** : fond blanc, border-top-left-radius 16px
- **Tabs principales** : pills navy actif / gris inactif
- **Zone contenu** : fond gris `#F4F4F4`, overflow-y scroll

### Composants DS à toujours utiliser
- Textfield with Label : DS Main Trident 2.0 — node `6145:2476`
- List / Row : DS Ody 2.0 — node `2235:5808`
- Tabs Tertiary : DS Ody 2.0 — node `2013:18455`
- Background/Sidebar : DS Ody 2.0 — node `33:3697`

### Panel wireframe (bas droite)
- Switch Interfacé (variante pré-remplie vs saisie manuelle)
- Switch Caisses ouvertes (état bloquant)
- Sélecteur de version (V1, V2, V3...)
- Collapse avec bouton −/+

---

## Système de commentaires PO

### Pins
- `position: absolute` dans `.content` — scrollent avec le contenu
- Couleur selon type : navy=Retour, orange=Idée, violet=RG, cyan=Question
- Label : `NombreInitiale` (1L, 2J, 3S...) — compteur global Firebase
- Drag & drop pour repositionner
- Contexte capturé automatiquement au clic (onglet + zone + élément)

### Popover de saisie
- Sélecteur de type : 💬 Retour / 💡 Idée / 📋 Règle de gestion / ❓ Question
- Nom de l'auteur automatique depuis l'URL `?user=Prénom`
- Thread avec réponses

### Firebase
- URL : `https://studio-jailoop-default-rtdb.firebaseio.com/comments`
- Sync toutes les 5s (poll)
- Suppression synchronisée

---

## Outil Retours PO (modale — Sébastien uniquement)

### Accès
- Bouton jaune bulle en bas à gauche — visible uniquement sur localhost
- Invisible sur GitHub Pages pour les POs

### Onglets
**Ligne 1 (pills)** : ⚡ Claude | 💬 Commentaires équipe
**Ligne 2 (tabs)** : 💬 Retour | 💡 Idée | 📋 Règle de gestion | ❓ Question

### Fonctionnalités par carte
- **↻** Réécriture IA via pont server.py → Claude Code → injection automatique
- **✏️** Édition directe inline
- **⇄** Reclassification vers autre catégorie
- **⚡** Ajout à la sélection Claude (éclair éteint/allumé)
- **✓** Marquer comme traité (jamais automatique)
- **×** Supprimer → corbeille (avec confirmation)

### Commentaires équipe
- Affiche uniquement les commentaires des POs (pas Sébastien)
- Requalification inline : assigne un type + déplace vers l'onglet
- Disparaît de "Commentaires équipe" une fois requalifié

### Section Claude
- Sélection temporaire de messages à prompter
- Bouton "↻ Générer le prompt" → prompt structuré professionnel
- Champ éditable avant envoi
- "⚡ Envoyer à Claude" → via server.py ou presse-papier

### Corbeille
- Tous les messages supprimés y vont (30 jours)
- Badge rouge sur le picto 🗑
- Restauration en un clic
- Vider définitivement avec confirmation

### Réécriture IA (système pont)
1. Clic ↻ → POST `/rewrite-request` → prompt collé dans Claude Code
2. Claude réécrit → commande python3 → `/tmp/wf_rewrite_response.json`
3. Polling `/rewrite-result` toutes les 2s → champ mis à jour en vert

---

## Espace PO (GitHub Pages)

### Portail
- URL : `https://studiojailoop.github.io/telecollecte-odyssey/`
- Login avec ID/mdp (Prénom + Ody26)
- Ouvre le wireframe avec `?user=Prénom`

### Ce que voit un PO
- Le wireframe complet en lecture/annotation
- Bouton jaune bulle bas droite avec son nom affiché
- Mode commentaire : clic → popover (type + texte)
- "Mes commentaires" : liste ses pins + suppression possible
- **Pas accès** au panneau Retours PO

### Comptes actuels
| ID | Mdp | Nom |
|---|---|---|
| Seb | ody26 | Sébastien |
| Julie | Ody26 | Julie |
| Nelly | Ody26 | Nelly |
| Jerome | Ody26 | Jérôme |
| Kirsty | Ody26 | Kirsty |
| Laurent | Ody26 | Laurent |

---

## Publication GitHub
```python
# Depuis Claude Code :
python3 << 'EOF'
import urllib.request, json, base64
TOKEN = "[GITHUB_TOKEN — dans les notes personnelles de Sébastien]"
OWNER = "StudioJailoop"
REPO  = "telecollecte-odyssey"
# ... push index.html + wireframe V3
EOF
```

---

## Pour réutiliser sur un nouveau projet

1. Copier `wireframe-telecollecte-cas1-V3.html` → `wireframe-[nouveau-sujet]-V1.html`
2. Vider le contenu spécifique (tables TPE, onglets Télécollecte) — garder header/sidebar/panel
3. Créer un nouveau repo GitHub ou un nouveau dossier dans le même repo
4. Adapter `portail.html` avec les bons comptes et le bon lien wireframe
5. Créer une nouvelle collection Firebase ou réutiliser avec une clé différente (`/comments-[projet]`)
6. `server.py` est générique — aucune modification nécessaire

**Ce qui est portable à 100% :** système de commentaires pins, outil Retours PO, réécriture IA, corbeille, portail PO, sidebar Odyssey DS.
