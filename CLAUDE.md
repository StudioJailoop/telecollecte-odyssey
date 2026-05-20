# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> **Système réutilisable** : tout le système est documenté dans les fichiers ARCHITECTURE.md, UX_RULES.md, TECH_RULES.md. Lire ces fichiers avant toute intervention.

## Démarrage immédiat

```bash
cd "/Users/sebastienkeller/Desktop/Claude Yaki"
python3 server.py   # Serveur local permanent (launchd auto-restart)
# → http://localhost:8765
```

Ouvrir le wireframe : `http://localhost:8765/wireframe-telecollecte-cas1-V4.html`

## Design System — RÈGLE NON NÉGOCIABLE

**Tout design Club Med est construit EXCLUSIVEMENT avec :**

| DS | Figma |
|----|-------|
| **Ody Trident Ψ 2.0** | `https://www.figma.com/design/EROcTR22vREhq7plcNLldI` |
| **Main Trident Ψ 2.0** | `https://www.figma.com/design/tYBVCMeWwSsiQbdZrUOuoX` |

- Avant tout élément UI → chercher dans le DS via `mcp__figma__search_design_system`
- Si trouvé → utiliser tel quel
- Si pas trouvé → demander avant de créer
- Si un choix déroge au DS → demander l'accord explicite

## Règles absolues

1. **Versionner avant toute évolution** : copier V4 → V5, etc. Fichier versionné = figé
2. **Publier sur GitHub après chaque modification** sans attendre
3. **Jamais régresser depuis V4-REF** — `wireframe-telecollecte-cas1-V4-REF.html` est immuable
4. **Audit avant publication** : vérifier les features clés listées dans KNOWN_BUGS.md
5. **Tester avec Playwright** avant de confirmer que c'est bon
6. **Max 2 tentatives de fix** puis poser des questions précises
7. **ARCHIVAGE** : seuls `claudeSelection` items → `done=true`. JAMAIS `briefs.forEach(b => b.done=true)`

## Fichier de travail unique — RÈGLE ANTI-DIVERGENCE

**Un seul fichier reçoit les modifications : `wireframe-telecollecte-cas1-V4.html`**

- Toute nouvelle feature, fix, ou retour PO → appliqué sur **V4.html uniquement**
- Les snapshots versionnés (V4.1, V4.2, V4.3…) sont des copies figées — **jamais modifiées**
- Quand on crée un snapshot : `cp V4.html V4.X.html` → mettre à jour le sélecteur de version dans la copie seulement
- **Playwright** : uniquement `navigate` + `screenshot` + `evaluate` en lecture — jamais appeler `goTo()`, `openBriefs()`, `toggleArchivesMode()` ou toute fonction JS qui modifie l'état visible dans le browser de l'utilisateur

## Conservation absolue de l'existant — RÈGLE CRITIQUE

**Toute modification est additive. Jamais une réécriture.**

### Fonctions interdites à réécrire sans validation explicite
- `goTo()` — navigation principale
- `renderBriefs()` — affichage briefs + badges
- `sendToClaude()` — seul chemin vers done=true
- `toggleArchivesMode()` — cascade de changements UI
- `checkAll()` / `checkReg()` — validation métier

### Process obligatoire avant toute modification
1. Lire les fonctions concernées et leurs dépendances
2. Identifier les effets de bord possibles
3. Modifier le minimum — conditions supplémentaires, ajustements locaux
4. Tester les flows critiques avec Playwright

### Tests obligatoires après chaque modification
```
✓ Ouverture/fermeture modale → onglet Retours par défaut
✓ Navigation Claude ↔ Équipe ↔ Archives ↔ Dernières modifs
✓ Archivage → seulement claudeSelection → done=true
✓ Badges → respectent archivesMode
✓ Sélection Claude + génération prompt
✓ Aucune erreur console (hors Firebase offline)
```

## Commit de référence stable — 2026-05-19

```
9cb6aba  — état stable avec toutes les features de la session 2026-05-19
```

Features incluses dans cet état stable :
- Boutons CTA dans le bloc-date (text → date → bouton)
- Bouton sticky dans barre TPE au scroll
- Footer supprimé
- openBriefs() recharge briefs depuis localStorage
- Couleurs auteurs corrigées

**En cas de régression → voir KNOWN_BUGS.md section "Retour arrière d'urgence"**

## Anti-régression — vérifications OBLIGATOIRES avant tout push

Après CHAQUE modification, vérifier avec Playwright :
1. Modale Retours PO s'ouvre → briefs s'affichent (pas "Aucun élément" si des briefs existent)
2. Onglet Télécollecte → bouton "Valider la saisie" dans le bloc-date
3. Scroll → bouton réapparaît dans barre TPE sticky
4. Onglet Régularisation → "Faire une régularisation" visible
5. Aucune erreur JS dans la console (hors Firebase offline)

## Méthodologie tests — OBLIGATOIRE après chaque grosse feature

Après chaque modification significative, exécuter cette checklist Playwright **avant** de pusher :

### Checklist de régression — à vérifier à chaque session
```
1. Modale Retours PO
   - Ouvrir la modale → les briefs existants s'affichent (pas "Aucun élément")
   - Onglet Retour / Idée / RG / Question → chacun affiche le bon contenu
   - Ajouter un brief → apparaît immédiatement
   - Mode Archives (switch) → affiche les done=true uniquement

2. Navigation onglets
   - Télécollecte → bouton "Valider la saisie" visible dans bloc-date
   - Scroll → bouton réapparaît dans barre TPE sticky
   - Date antérieure → même comportement
   - Régularisation → "Faire une régularisation" visible, activé quand total OK

3. Badges
   - Badges des types respectent archivesMode (BUG-001)
   - sendToClaude → seuls les sélectionnés passent done=true (BUG-002)

4. Pins
   - Les pins s'affichent sur le wireframe
   - Clic sur pin → popover thread s'ouvre
```

### Après chaque grosse feature — commande Playwright
```javascript
// Vérifier l'absence d'erreurs JS critiques
mcp__playwright__browser_console_messages({ level: 'error' })

// Vérifier que les briefs sont rendus
mcp__playwright__browser_evaluate(() =>
  document.getElementById('briefs-list').children.length > 0 ||
  document.getElementById('briefs-list').textContent.includes('Aucun')
)
```

## Serveur local (routes)

| Route | Méthode | Usage |
|-------|---------|-------|
| `/rewrite-result` | GET | Polling réécriture IA |
| `/get-journal-text/:id` | GET | Polling texte journal |
| `/rewrite-request` | POST | Demande réécriture → Claude Code |
| `/send-to-claude` | POST | Envoi prompt → Claude Code |
| `/save-journal-text` | POST | Sauvegarde texte journal reformulé |
| `/reset-briefs-done` | POST | Reset emergency done=false |

## GitHub

- Repo : `StudioJailoop/telecollecte-odyssey`
- Token : [dans les notes personnelles de Sébastien — ne jamais committer]
- URL publique : `https://studiojailoop.github.io/telecollecte-odyssey/`
- Push : `git add . && git commit -m "..." && git push origin main`

## Firebase

- URL : `https://studio-jailoop-default-rtdb.firebaseio.com/comments`
- Usage : commentaires pins partagés temps réel
- Sync toutes les 5s (poll)
