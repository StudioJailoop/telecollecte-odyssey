---
name: feedback-loopcraft-regle-fondatrice
description: Règle fondatrice Loopcraft — TOUS les commentaires dans Commentaires équipe, designer inclus — règle immuable depuis 2026-06-02
metadata:
  node_type: memory
  type: feedback
  originSessionId: a4b5600a-4d06-4dda-88d0-d5e60db2c5b9
---

## Règle fondatrice — Commentaires Loopcraft (mise à jour 2026-06-02)

**TOUS les messages arrivent dans Commentaires équipe — designer compris.**

La règle précédente (PO uniquement, jamais le designer) est **définitivement abandonnée** le 2026-06-02 par Sébastien.

### Nouvelle circulation

**Tout commentaire** (designer ou PO/intervenant) → arrive dans **Commentaires équipe** → recatégorisation a posteriori si besoin.

### Règles de filtre pour `loadTeamComments()`

Supprimer le filtre `author !== DESIGNER`. Tous les auteurs sont inclus.

```javascript
// CORRECT — nouvelle règle
!p.requalified && !p.archived

// INTERDIT — ancienne règle abandonnée
p.author !== DESIGNER && !p.requalified && !p.archived
```

**Why:** Sébastien écrit des commentaires rapides et veut pouvoir les recatégoriser ensuite. Le flux de qualification reste le même — la source change. Décision explicite du 2026-06-02, nouvelle norme immuable.

**How to apply:** Ne jamais filtrer les commentaires du designer hors de Commentaires équipe. Tout message, quelle que soit son origine, atterrit dans le même flux.
