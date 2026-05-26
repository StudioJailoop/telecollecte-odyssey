# START_HERE.md — Point d'entrée nouvelle session

## Contexte produit en 30 secondes

Tu travailles avec **Sébastien Keller**, UX/UI Designer chez Studio Jailoop, sur un projet pour **Club Med / Odyssey**.

Le projet est un **wireframe interactif HTML** du module "Saisie des Télécollectes TPE" — l'interface que les réceptionnistes Night Audit utilisent pour déclarer les transactions par carte bancaire en fin de journée.

Ce wireframe est enrichi d'un **système de collaboration PO complet** : annotations contextuelles, retours catégorisés, génération de prompts Claude, archives, journal des modifications.

---

## Commandes de démarrage

```bash
# 1. Vérifier que le serveur tourne (launchd auto-restart)
lsof -i :8765 | grep LISTEN

# Si pas actif :
cd "/Users/sebastienkeller/Desktop/Claude Yaki" && python3 server.py &

# 2. Ouvrir le wireframe
open "http://localhost:8765/wireframe-telecollecte-cas1-V4.html"

# 3. Ouvrir le portail PO
open "http://localhost:8765/portail.html"
```

---

## Fichiers critiques

| Fichier | Rôle |
|---------|------|
| `wireframe-telecollecte-cas1-V4.html` | **Fichier de travail courant** |
| `wireframe-telecollecte-cas1-V4-REF.html` | **Référence immuable — NE PAS MODIFIER** |
| `server.py` | Serveur local avec routes IA |
| `portail.html` → `index.html` sur GitHub | Portail PO avec auth |

---

## Ce que l'utilisateur attend de toi

1. Modifier le wireframe sur demande
2. Toujours publier sur GitHub après chaque modif
3. Ne jamais casser ce qui fonctionne (voir KNOWN_BUGS.md)
4. Utiliser uniquement Trident Ψ 2.0 + Odyssey 2.0 comme DS
5. Tester avant de confirmer

---

## Accès PO (GitHub Pages)

URL : `https://studiojailoop.github.io/telecollecte-odyssey/`

| ID | Mdp | Nom |
|----|-----|-----|
| Seb | ody26 | Sébastien |
| Julie | Ody26 | Julie |
| Nelly | Ody26 | Nelly |
| Jerome | Ody26 | Jérôme |
| Kirsty | Ody26 | Kirsty |
| Laurent | Ody26 | Laurent |

---

## Premier réflexe

Lire dans cet ordre : `CURRENT_STATE.md` → `ARCHITECTURE.md` → `UX_RULES.md` → `TECH_RULES.md`
