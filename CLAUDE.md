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
