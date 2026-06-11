---
name: Toujours publier sur GitHub après chaque modification
description: Toute modification du wireframe ou du portail doit être immédiatement publiée sur GitHub Pages
type: feedback
originSessionId: 9f8442c3-4d5c-4465-87b8-99549a3d219e
---
Après CHAQUE modification des fichiers wireframe ou portail, publier immédiatement sur GitHub sans attendre que l'utilisateur le demande.

**Why:** Les POs ont accès au lien GitHub à tout moment. Si les fichiers ne sont pas à jour, ils voient une version obsolète. C'est non négociable.

**How to apply:**
1. Modifier le fichier localement
2. Publier sur GitHub via git push (pas l'API urllib qui échoue sur les gros fichiers)
3. Confirmer à l'utilisateur que c'est publié

Commande de publication :
```bash
cd "/Users/sebastienkeller/Desktop/Claude Yaki" && \
git add wireframe-telecollecte-cas1-V3.html portail.html && \
git commit -m "Update [description]" && \
git push origin main
```
