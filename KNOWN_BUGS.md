# KNOWN_BUGS.md

## Bugs résolus — NE PAS RÉINTRODUIRE

### BUG-001 : Badges incorrects en mode Archives ★★★
- **Symptôme** : Idée affiche 1 en mode Archives alors que 0 éléments archivés
- **Cause** : `renderBriefs` calculait `!b.done` au lieu de `archivesMode ? b.done : !b.done`
- **Ligne** : Dans `renderBriefs`, calcul des compteurs de badges
- **Fix** : Ligne 2119 — `briefs.filter(b => b.type === t && (archivesMode ? b.done : !b.done))`

### BUG-002 : Archivage de TOUS les briefs après envoi Claude ★★★
- **Symptôme** : Tous les retours passent en Archives après un envoi à Claude
- **Cause** : `briefs.forEach(b => { b.done = true })` dans sendToClaude
- **Fix** : Seuls les `claudeSelection` items → `b.done = true`

### BUG-003 : Bouton designer invisible au chargement ★★
- **Symptôme** : Le bouton jaune bulle ne s'affiche pas sur localhost
- **Cause** : Script exécuté avant que le DOM soit prêt
- **Fix** : Déplacé dans `DOMContentLoaded`

### BUG-004 : Drag involontaire des pins ★★
- **Symptôme** : Le pin se déplace lors d'un simple clic
- **Cause** : Pas de seuil de déplacement minimum
- **Fix** : Seuil 8px avant activation du drag

### BUG-005 : display:none inline résistant aux changements JS ★★
- **Symptôme** : `btnv-reg` reste invisible malgré `style.display = 'flex'`
- **Cause** : Style inline `display:none` a priorité sur JS
- **Fix** : `style.setProperty('display', 'flex', 'important')`

### BUG-006 : Noms d'auteurs en rouge dans les threads ★
- **Symptôme** : Tous les noms d'auteurs affichés en rouge dans les bulles de thread, quelle que soit la personne
- **Cause** : `getColor()` retournait toujours `#D93025` — `AUTHOR_COLORS` était déclarée mais jamais utilisée
- **Note** : Bug encore présent dans V4 (détecté lors de l'audit runtime 2026-05-19)
- **Fix appliqué en V4** : `getColor()` lit maintenant `AUTHOR_COLORS[author]`, fallback `#6B7280`
- **Fix complémentaire** : `AUTHOR_COLORS` complétée avec Jérôme (#DC2626), Kirsty (#0891B2), Laurent (#D97706)

---

## Zones fragiles — surveiller à chaque modif

### Zone 1 : goTo() — touche tout
Toute modification de `goTo()` peut casser :
- Affichage footer (btnv, btnv-ant-footer, btnv-reg)
- Visibilité des pins (refreshPins)
- Barre TPE ant
- Bouton Envoyer à Claude

### Zone 2 : renderBriefs() — logique duale
Doit toujours respecter `archivesMode` pour :
- Filtre des éléments affichés
- Calcul des badges
- Affichage des outils (actifs vs archivés)

### Zone 3 : toggleArchivesMode() — cascade de changements
Doit gérer :
- Claude + team pills visibility
- Dernières modifs pill visibility
- Envoyer à Claude button
- Zone saisie
- Recalcul badges

### Zone 4 : sendToClaude() — SEUL chemin d'archivage
Seule fonction autorisée à mettre `done=true`. Vérifier à chaque session.

---

## Checklist audit avant publication

- [ ] `renderBriefs` utilise `archivesMode ? b.done : !b.done` pour les badges
- [ ] `sendToClaude` utilise `claudeSelection.forEach` (pas `briefs.forEach`)
- [ ] `goTo('reg')` affiche `btnv-reg`
- [ ] `goTo('ant')` affiche `btnv-ant-footer`
- [ ] `goTo('tpe')` affiche `btnv`
- [ ] `copy-btn` visible sur tous les onglets sauf Archives
- [ ] `btab-lastmodifs` visible seulement en mode Archives
- [ ] Pas d'erreur de syntaxe JS (apostrophes dans template literals)
- [ ] Tous les panels ont leur `display` géré dans `setBriefTab`
