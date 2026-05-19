# TECH_RULES.md

## Règles de développement absolues

### 1. Archivage des briefs — CRITIQUE
```javascript
// ✅ CORRECT — seulement les sélectionnés
claudeSelection.forEach(key => {
  const b = briefs.find(b => String(b.id) === String(key));
  if (b) b.done = true;
});

// ❌ INTERDIT — archive tout
briefs.forEach(b => { b.done = true; });
```

### 2. Badges — respect de archivesMode
```javascript
// ✅ CORRECT dans renderBriefs ET updateAllCounts
const n = briefs.filter(b => b.type === t && (archivesMode ? b.done : !b.done)).length;

// ❌ INCORRECT — ignore archivesMode
const n = briefs.filter(b => b.type === t && !b.done).length;
```

### 3. Display buttons — style.setProperty pour forcer
```javascript
// Quand un bouton a display:none en inline style, utiliser setProperty
btn.style.setProperty('display', 'flex', 'important');
```

### 4. Publish workflow
```bash
# Toujours dans cet ordre
git add wireframe-telecollecte-cas1-V4.html
git commit -m "Description claire"
git push origin main
```

### 5. Backup avant modif
```python
import shutil
shutil.copy('wireframe-telecollecte-cas1-V4.html', 'wireframe-telecollecte-cas1-V4-REF.html')
```

### 6. Audit avant publication
Vérifier systématiquement :
- `function updateAllCounts` → utilise `archivesMode ? b.done : !b.done`
- `claudeSelection.forEach` → seul chemin vers `b.done = true`
- `renderBriefs` → filtre `archivesMode ? b.done : !b.done`
- `btnv-reg`, `btnv-ant-footer` → display géré dans `goTo()`
- `copy-btn` (Envoyer à Claude) → visible sauf en mode archives

## Patterns JavaScript

### IDs → éléments DOM critiques
```javascript
// Navigation principale
#tab-tpe, #tab-ant, #tab-reg        // tabs principales
#mc, #view-ant, #view-reg           // vues contenu

// Buttons validation
#btnv                                // Valider la saisie (tpe)
#btnv-ant                            // Valider la saisie sticky (ant, dans barre TPE)
#btnv-ant-footer                     // Valider la saisie footer (ant)
#btnv-reg                            // Faire une régularisation footer (reg)
#btnv-inline                         // Valider la saisie sticky (tpe, dans barre TPE)
#copy-btn                            // ⚡ Envoyer à Claude

// Outil PO
#briefs-panel, #briefs-overlay       // Modale Retours PO
#briefs-list                         // Liste des briefs actifs
#lastmodifs-panel                    // Journal des modifs
#claude-panel                        // Section sélection Claude
#team-comments-list-panel            // Commentaires équipe

// Archives
#sw-archives                         // Switch archives
#btab-lastmodifs                     // Pill Journal des modifs (visible si archivesMode)

// Corbeille
#trash-panel, #trash-overlay, #trash-list

// Commentaires
.comment-pin                         // Pins sur le wireframe
#comment-popover                     // Nouveau commentaire
#thread-popover                      // Thread réponses
```

### Fonctions critiques — ne pas modifier sans audit
```
goTo(id)                // Navigation principale — gère footer, pins, tabs
renderBriefs()          // Affichage briefs — doit respecter archivesMode
updateAllCounts()       // Badges — doit respecter archivesMode
sendToClaude()          // Envoi — SEUL endroit où done=true est autorisé
toggleArchivesMode(on)  // Switch archives — masque/affiche éléments
checkAll()              // Validation montant/remise — rows visibles uniquement
fbSave() / fbLoad()     // Sync Firebase — ne pas bloquer le thread principal
```

## Syntaxe JS — pièges courants

```javascript
// Apostrophes dans template literals → échapper
`Aujourd\\'hui`  // ✅
`Aujourd'hui`    // ❌ SyntaxError

// Comparaison IDs (numériques vs strings)
String(b.id) === String(key)  // ✅ toujours convertir
b.id === key                   // ❌ peut échouer si types différents

// display flex vs block
btn.style.display = 'flex'    // ✅ pour flex containers
btn.style.display = 'block'   // ⚠️ casse le flex:2 du bouton
```

## LocalStorage keys

| Clé | Contenu |
|-----|---------|
| `wf_briefs_telecollecte` | Array des retours PO |
| `wf_briefs_trash` | Corbeille 30j |
| `wf_comments_telecollecte` | Pins commentaires |
| `wf_pin_counter` | Compteur global pins |
| `wf_briefs_reset_done_v4` | Flag reset one-time |
