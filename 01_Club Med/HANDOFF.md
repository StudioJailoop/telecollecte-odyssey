# HANDOFF.md — État du produit pour transmission d'équipe

**Date** : 2026-05-19 | **Préparé par** : Claude Code | **Pour** : Nouvelle session Claude

---

## Résumé exécutif

Le projet est un **wireframe interactif HTML** enrichi d'un **outil de collaboration PO unique** pour le module Télécollecte TPE d'Odyssey / Club Med. Il est fonctionnel à ~85%, déployé sur GitHub Pages, accessible aux POs via portail authentifié.

Le wireframe simule fidèlement l'interface de saisie avec le DS Trident Ψ 2.0 et permet à une équipe distribuée de collaborer via des pins contextuels, des retours catégorisés, et une boucle complète retour → IA → modification.

---

## Ce qui fonctionne en production

✅ 3 onglets wireframe avec logique de validation métier  
✅ 5 TPE par onglet avec navigation sticky  
✅ Pins de commentaires Firebase (sync 5s)  
✅ Outil Retours PO complet (localhost Sébastien)  
✅ Portail PO GitHub Pages avec auth  
✅ Génération de prompts Claude structurés  
✅ Système d'archives avec Journal des modifs éditorial  
✅ Corbeille 30j  
✅ Réécriture IA via pont server.py  
✅ Serveur permanent via launchd  

---

## Ce qui est en cours

⚠️ Bouton "Faire une régularisation" — visible mais grisé par défaut (comportement normal mais vérifier affichage Chrome)  
⚠️ Reformulation journal IA — manuelle en attendant crédit Anthropic (~20$)  
⚠️ Sync Firebase côté POs GitHub Pages — non implémentée  

---

## Risques identifiés

🔴 **Régression archivage** : La ligne `briefs.forEach(b => b.done=true)` ne doit JAMAIS être utilisée  
🔴 **Régression badges** : `renderBriefs` doit toujours utiliser `archivesMode ? b.done : !b.done`  
🟡 **Syntaxe JS** : Les apostrophes dans les template literals cassent silencieusement le JS  
🟡 **display inline** : Certains boutons ont `display:none` en style inline — nécessite `setProperty('important')`  

---

## Priorité immédiate

1. Vérifier que le bouton "Faire une régularisation" s'affiche sur l'onglet Régularisation
2. S'assurer qu'aucune régression n'a été introduite sur les badges Archives

---

## Pour démarrer en 2 minutes

```bash
# Vérifier le serveur
lsof -i :8765 | grep LISTEN || (cd "/Users/sebastienkeller/Desktop/Claude Yaki" && python3 server.py &)

# Ouvrir
open "http://localhost:8765/wireframe-telecollecte-cas1-V4.html"
```

Lire dans l'ordre : `START_HERE.md` → `CURRENT_STATE.md` → `KNOWN_BUGS.md`
