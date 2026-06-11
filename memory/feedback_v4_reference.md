---
name: V4 version de référence — ne jamais régresser
description: La version V4 avec badges Archives corrects est la référence absolue — toute modification doit être auditée contre cette base
type: feedback
originSessionId: 9f8442c3-4d5c-4465-87b8-99549a3d219e
---
La version `wireframe-telecollecte-cas1-V4.html` (commit 3ad3059) est la référence immuable.

**Why:** De nombreuses régressions ont été introduites lors des corrections du système Archives/badges. L'utilisateur a clairement demandé que cette version ne soit plus jamais détruite.

**Bug corrigé clé :** Dans `renderBriefs`, les badges comptaient `!b.done` au lieu de `archivesMode ? b.done : !b.done`. Cette seule ligne causait tous les problèmes de badges incorrects en mode Archives.

**RÈGLE ABSOLUE — archivage :**
Seuls les briefs **explicitement sélectionnés** avec ⚡ et envoyés à Claude via `claudeSelection` peuvent passer à `done=true`. La ligne `briefs.forEach(b => { b.done = true })` est INTERDITE — elle archive tout sans distinction. Toujours utiliser : `claudeSelection.forEach(key => { const b = briefs.find(...); if (b) b.done = true; });`

**How to apply:**
1. Avant toute modification → vérifier que `wireframe-telecollecte-cas1-V4-REF.html` existe et est intact
2. Après toute modification → audit complet des features (voir script d'audit dans project_odyssey_system.md)
3. En cas de doute → restaurer depuis `wireframe-telecollecte-cas1-V4-REF.html`
4. Le fichier `-REF.html` ne doit JAMAIS être modifié
