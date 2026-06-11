---
name: feedback-loopcraft-ux-reuse-pattern
description: Règle fondatrice Loopcraft — réutiliser le pattern UX existant avant de créer une nouvelle UI
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6e57a25c-46bc-4e65-8af2-e0b91fa67644
---

Une règle métier ne doit PAS provoquer une nouvelle UI. Elle doit s'intégrer dans l'UI existante.

**Règle :** Avant toute modification UX, se demander "Puis-je réutiliser exactement le même pattern visuel que l'écran équivalent ?" Si oui → réutiliser. Si non → expliquer pourquoi avant de modifier.

**Obligation :** Avant chaque modification UX, déclarer explicitement :
- "Je réutilise le pattern existant" OU
- "Je dois créer un nouveau pattern car..."

**Why:** Sébastien a constaté une tendance à recréer des variantes d'interface ou déplacer des éléments quand une règle métier est ajoutée. Priorité : cohérence utilisateur > logique métier.

**How to apply:**
1. Réutiliser le composant existant
2. Réutiliser les emplacements existants
3. Réutiliser la hiérarchie visuelle
4. Ne créer une nouvelle UI que si c'est impossible fonctionnellement

**Cas concret :** Date antérieure doit avoir le même bloc-date que Télécollecte interfacé :
- Ligne 1 : label + sélecteur date
- Ligne 2 : KPI + badge écart à droite + bouton Valider à droite
Seul le contenu change (Télécollecte saisie au lieu de Montant saisi). Pas de nouvelle disposition.
