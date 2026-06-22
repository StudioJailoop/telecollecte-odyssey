# LOOPCRAFT — CHECKLIST PRÉ-CODE OBLIGATOIRE

Avant toute modification, répondre à cette checklist. Si un risque existe → STOP et demander validation.

---

## Checklist

| # | Question | Réponse |
|---|---|---|
| 1 | Invariants Loopcraft impactés ? | oui / non |
| 2 | Risque sur vue Designer ? | oui / non |
| 3 | Risque sur vue PO ? | oui / non |
| 4 | Risque sur séparation des rôles ? | oui / non |
| 5 | Risque sur le Panel (Designer ou PO) ? | oui / non |
| 6 | Risque sur la Design Zone ? | oui / non |
| 7 | Risque sur les commentaires / remontée PO→Designer ? | oui / non |
| 8 | Risque sur les archives ? | oui / non |
| 9 | Risque sur Claude / envoi à Claude ? | oui / non |
| 10 | Risque sur la documentation ? | oui / non |
| 11 | Risque sur les règles de gestion ? | oui / non |
| 12 | Risque sur le shell projet ? | oui / non |
| 13 | Risque sur les données existantes ? | oui / non |
| 14 | Risque sur la navigation dashboard ? | oui / non |

---

## Si tout est NON → on peut coder

## Si au moins un OUI → STOP, expliquer le risque, demander validation

---

## Rappel des erreurs à ne jamais refaire

- `if (!isDesigner) panel.style.display = 'none'` → interdit
- `isDesigner = location.hostname === 'localhost'` → interdit
- Reconstruire header/sidebar/panel from scratch pour un sous-projet → interdit
- Push sans validation visuelle → interdit
- Inventer du contenu RG/documentation → interdit
