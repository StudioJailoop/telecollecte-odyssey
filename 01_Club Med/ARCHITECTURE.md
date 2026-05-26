# ARCHITECTURE.md

## Stack technique

```
HTML/CSS/JS inline (zero dépendance)
├── Firebase Realtime DB  → commentaires partagés
├── server.py (Python)    → pont Claude Code ↔ navigateur
├── localStorage          → briefs, corbeille, pins, préférences
└── GitHub Pages          → hébergement portail PO
```

## Structure du fichier wireframe (3013 lignes)

```
<head>
  <style>          → ~520 lignes CSS
    :root           → tokens couleurs
    .header         → navbar Odyssey DS
    .sidebar        → navigation latérale DS
    .main           → zone contenu principale
    .tabs-bar       → tabs principales
    .tpe-tabs-bar   → tabs TPE Tertiary sticky
    .t-head/.t-row  → composants tableau
    .wf-panel       → panel Options (bas-droite)
    Commentaires    → pins, popover, thread
    Outil PO        → modale Retours PO
    Archives        → switch, journal
  </style>

<body>
  <!-- Bouton jaune bulle designer -->     → #briefs-nav-btn
  <!-- Panel Corbeille -->                 → #trash-panel + #trash-overlay
  <!-- Panneau Retours PO -->              → #briefs-panel + #briefs-overlay
  <!-- Popover nouveau commentaire -->     → #comment-popover
  <!-- Thread popover -->                  → #thread-popover
  <!-- Bouton toggle sidebar -->           → .toggle-btn
  <!-- LAYOUT -->
    <!-- SIDEBAR -->                       → nav.sidebar#sidebar
    <!-- MAIN -->
      <!-- Tabs principales -->            → .tabs-bar
      <!-- Tabs TPE Tertiary -->           → .tpe-tabs-bar#tpe-tabs-bar
      <!-- Zone contenu scrollable -->     → .content
        <!-- Vue Télécollecte -->          → #mc
        <!-- Vue Date antérieure -->       → #view-ant
        <!-- Vue Régularisation -->        → #view-reg
      <!-- Footer principal -->            → footer.footer#main-footer
  <!-- Panel wireframe Options -->         → .wf-panel
  
<script>           → ~2400 lignes JS
```

## Variables globales JS critiques

```javascript
// Navigation
currentTab          // 'tpe' | 'ant' | 'reg'
commentMode         // bool — mode pose de pins
currentThreadId     // ID du pin dont le thread est ouvert

// Outil PO
currentBriefTab     // 'retour'|'idee'|'rg'|'question'|'claude'|'team'|'lastmodifs'
archivesMode        // bool — mode archives ON/OFF
claudeSelection     // Set<string> — IDs sélectionnés pour Claude

// Données
briefs              // Array — retours PO (localStorage: wf_briefs_telecollecte)
comments            // Array — pins Firebase (localStorage: wf_comments_telecollecte)
BRIEFS_KEY          // 'wf_briefs_telecollecte'
STORAGE_KEY         // 'wf_comments_telecollecte'
TRASH_KEY           // 'wf_briefs_trash'
FB_URL              // 'https://studio-jailoop-default-rtdb.firebaseio.com/comments'
CURRENT_USER        // depuis URL ?user=Prénom (défaut: 'Sébastien')
```

## Flux de données

```
PO (GitHub Pages)
  → pose pin → saveComment() → localStorage + fbSave()
  → Firebase sync → Sébastien voit le pin

Sébastien (localhost)
  → crée brief → addBrief() → localStorage
  → sélectionne briefs → claudeSelection.add()
  → génère prompt → generatePrompt()
  → envoie → sendToClaude() → server.py → presse-papier → Claude Code
  → Claude modifie HTML → git push
  → briefs sélectionnés → done=true → Archives

Archives
  → updateAllCounts() → badges selon archivesMode
  → renderBriefs() → filtre done/!done selon archivesMode
  → Journal des modifs → generateJournalText() → server.py → reformulation narrative
```

## Composants DS utilisés

| Composant | Node DS | Usage |
|-----------|---------|-------|
| Background/Sidebar | Ody 2.0 node 33:3697 | Layout principal |
| List/Row | Ody 2.0 node 2235:5808 | Lignes tableau |
| Tabs Tertiary | Ody 2.0 node 2013:18455 | Tabs TPE |
| Textfields with Label | Main 2.0 node 6145:2476 | Champ date |
| Text Buttons Saffran Disabled | Main 2.0 node 6145:2050 | Bouton Valider |

## Couleurs tokens

```css
--navy:    #1E2643   /* Ultramarine blue DS */
--yellow:  #FDBE00   /* Saffran yellow DS */
--white:   #FFFFFF
--grey-bg: #F4F4F4
--grey-bd: #E0E0E0
--grey-txt:#6B7280
--red:     #D93025
--lavender:#9EAEF4
```
