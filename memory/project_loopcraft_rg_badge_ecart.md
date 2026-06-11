---
name: project-loopcraft-rg-badge-ecart
description: "RG à inclure dans la documentation — badge écart doit afficher uniquement les MDP qui contribuent réellement à l'écart"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6e57a25c-46bc-4e65-8af2-e0b91fa67644
---

## RG — Badge écart : cohérence MDP / écart réel

Le badge "Écart détecté · Visa · Amex · -5,00 €" n'est pas décoratif.

**Règle :** La liste des moyens de paiement affichés dans le badge doit être calculée à partir des lignes réellement en écart. Un MDP n'apparaît dans le badge que s'il contribue à l'écart total.

**Exemple valide :**
- Visa : -3 € / Amex : -2 € → badge affiche Visa · Amex

**Exemple invalide :**
- Visa : 0 € / Amex : 0 € / WeChat : -5 € → badge doit afficher WeChat uniquement, pas Visa · Amex

**Why:** Règle définie le 2026-06-04 — le badge est un indicateur métier, pas visuel. Afficher le mauvais MDP induirait l'utilisateur en erreur sur l'origine de l'écart.

**How to apply:** À inclure dans la documentation fonctionnelle (drawer Règles de gestion) quand Sébastien demandera de rédiger les RG. Section : Télécollecte interfacée + Date antérieure. Invisible pour l'utilisateur dans la version wireframe actuelle (valeurs hardcodées), à implémenter en production.
