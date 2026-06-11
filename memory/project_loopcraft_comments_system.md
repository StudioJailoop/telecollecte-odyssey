---
name: project-loopcraft-comments-system
description: "Architecture complète du système de commentaires Loopcraft — essence du produit, source des modifications design"
metadata: 
  node_type: memory
  type: project
  originSessionId: a4b5600a-4d06-4dda-88d0-d5e60db2c5b9
---

## Système de commentaires — Cœur de Loopcraft

Les commentaires sont **l'essence du produit**. Ce sont eux qui génèrent les modifications design. Toute régression sur ce système est critique.

**Firebase est la source de vérité absolue.** Tout est dans Firebase. En cas de problème, tout peut être récupéré ou corrigé directement depuis Firebase.

---

## URLs Firebase

- **`/comments`** — tous les pins visuels (designer + PO) → `https://studio-jailoop-default-rtdb.firebaseio.com/comments.json`
- **`/briefs_telecollecte`** — briefs structurés (onglets Retour/Idée/RG/Question) → `https://studio-jailoop-default-rtdb.firebaseio.com/briefs_telecollecte.json`

---

## Flux de circulation (RÈGLE FONDATRICE — NE JAMAIS MODIFIER)

### Commentaire Designer (Sébastien)
```
Pose un pin → choisit une catégorie → enregistre
↓
Écrit immédiatement dans Firebase /comments (fbSaveOne — atomique)
↓
Créé simultanément comme brief dans Firebase /briefs_telecollecte (fbSaveBriefOne — atomique)
↓
Visible dans l'onglet correspondant (Retour / Idée / RG / Question)
↓
NE PASSE JAMAIS par Commentaires équipe
```

### Commentaire PO / Intervenant (Julie, Nelly, Laurent...)
```
Pose un pin → choisit une catégorie → enregistre
↓
Écrit immédiatement dans Firebase /comments (fbSaveOne — atomique)
↓
Arrive dans "Commentaires équipe" chez le designer
↓
Le designer valide / requalifie
↓
Devient un brief dans Firebase /briefs_telecollecte (fbSaveBriefOne — atomique)
↓
Visible dans la catégorie finale (Retour / Idée / RG / Question)
```

---

## Règle d'écriture atomique — ABSOLUE

**JAMAIS de PUT global sur `/comments.json` ou `/briefs_telecollecte.json`** lors d'une création ou modification individuelle.

| Opération | Fonction | Firebase |
|---|---|---|
| Nouveau commentaire (PO ou designer) | `fbSaveOne(comment)` | PUT `/comments/{id}.json` |
| Nouveau brief (ajout manuel ou requalification) | `fbSaveBriefOne(brief)` | PUT `/briefs_telecollecte/b{id}.json` |
| Modifier brief (done, type, text) | `fbUpdateBrief(brief)` | PUT `/briefs_telecollecte/b{id}.json` |
| Supprimer brief | `DELETE` | DELETE `/briefs_telecollecte/b{id}.json` |
| Mise à jour batch (réponses, fbSave) | `fbSave()` | PUT `/comments.json` — UNIQUEMENT pour update global |

**Raison :** un PUT global avec un localStorage désynchronisé écrase tout Firebase → perte définitive des données.

---

## Lecture

- `fbLoad()` : poll toutes les 5s, accepte tableau OU objet keyed par ID
- `openBriefs()` : charge depuis Firebase en priorité, localStorage en fallback
- En cas de problème → inspecter Firebase directement via les URLs ci-dessus

---

## Filtre `loadTeamComments()`

```javascript
const DESIGNER = 'Sébastien';
// Inclure seulement :
p.author !== DESIGNER   // pas le designer
&& !p.requalified       // pas encore validé
&& !p.archived          // pas archivé
```

---

## Champs d'un commentaire (pin)
```javascript
{
  id: Date.now(),        // clé unique Firebase
  author: CURRENT_USER,
  text: '...',
  date: 'jj/mm/aaaa',
  tab: 'tpe' | 'ant' | 'reg',
  pinLabel: '9S',        // numéro global + initiale auteur
  commentType: 'retour' | 'idee' | 'rg' | 'question',
  qualifiedType: '...',  // après requalification designer
  requalified: true,     // après validation → disparaît de Commentaires équipe
  archived: true,        // archivé → invisible partout
  project: 'club-med'
}
```

## Champs d'un brief
```javascript
{
  id: ..., author: ..., text: ...,
  type: 'retour' | 'idee' | 'rg' | 'question',
  date: ..., done: false,
  pinLabel: ..., sourcePin: id_du_pin,
  sourceKey: 'pin-{id}',  // si créé depuis un commentaire équipe
  tab: ..., source: 'team' // si issu d'un PO
}
```

---

## Ce qui NE doit JAMAIS arriver
- PUT global Firebase lors d'une création → écrase tout
- Commentaire Sébastien dans "Commentaires équipe"
- Commentaire PO directement dans les onglets sans passer par Commentaires équipe
- `openBriefs()` lisant uniquement le localStorage (perd les briefs d'autres sessions)

## Récupération d'urgence

Si des données semblent manquantes :
1. Vérifier Firebase directement : `curl https://studio-jailoop-default-rtdb.firebaseio.com/comments.json`
2. Les pins requalifiés (`requalified: true`) contiennent le `qualifiedType` → peuvent reconstruire les briefs
3. Réinjecter avec un script Python `PUT /briefs_telecollecte/{key}.json` par entrée

**Why:** Firebase est la source de vérité absolue — tout ce qui est écrit atomiquement est récupérable. Sébastien l'a confirmé le 2026-05-26 : "au moindre problème on peut tout récupérer ou toucher dans Firebase".

**How to apply:** Avant tout fix sur le système — vérifier Firebase en premier. Ne jamais supposer que le localStorage est à jour. Toujours écrire atomiquement, jamais en PUT global.
