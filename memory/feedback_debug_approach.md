---
name: Approche debug - ne jamais confirmer sans tester
description: Règles de debug pour éviter les cycles infinis de corrections
type: feedback
originSessionId: 9f8442c3-4d5c-4465-87b8-99549a3d219e
---
Ne jamais dire "c'est bon" sans avoir testé avec Playwright ou une vérification concrète.

**Why:** Plusieurs fois j'ai confirmé des corrections qui ne marchaient pas, forçant l'utilisateur à répéter "ça ne marche pas" 5-10 fois.

**How to apply:**
1. **Après 2 tentatives infructueuses → STOP** — poser une série de questions précises avant toute nouvelle tentative :
   - "Quel élément exact tu cliques ?" (pin rouge / badge / bouton / etc.)
   - "Qu'est-ce que tu vois quand tu cliques ?" (s'ouvre / ne se ferme pas / rien / erreur)
   - "Sur quel onglet / quelle page tu es ?"
   - "C'est sur local ou sur GitHub ?"
2. Ne jamais continuer à chercher dans le vide — attendre les réponses avant de coder
3. Utiliser Playwright browser_evaluate pour tester la logique avant de dire "c'est bon"
4. Les vidéos MP4 ne sont pas lisibles — demander une capture d'écran ou description en 1 phrase
5. Ne JAMAIS dire "c'est bon" sans avoir testé concrètement
