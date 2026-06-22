# LOOPCRAFT — CONSTITUTION

> Ce fichier est immuable. Toute modification doit être validée explicitement par Sébastien Keller.

---

## 1. CE QU'EST LOOPCRAFT

Loopcraft est un **outil global d'itération entre Designer et PO**, permettant de construire, commenter, documenter et faire évoluer des wireframes avec l'aide de l'IA.

Loopcraft n'est pas :
- un wireframe
- un projet
- Télécollecte
- Cardex
- Club Med

Les projets et sous-projets sont du **contenu** — ils peuvent changer.  
L'essence de Loopcraft ne doit **jamais** changer.

---

## 2. HIÉRARCHIE PRODUIT

```
LOOPCRAFT (outil global, stable, invariant)
└── PROJETS (espaces de travail)
    ├── Club Med
    │   └── Odyssée (CRM Club Med)
    │       ├── Télécollecte (feature)
    │       └── Cardex (feature)
    └── DDJ (projet distinct — aucun lien avec Club Med)
```

**Règle :** DDJ et Club Med sont deux projets Loopcraft différents. Ils ne partagent pas de shell.  
Télécollecte et Cardex partagent le shell Club Med / Odyssée.

---

## 3. DEUX VUES — INVARIANT ABSOLU

Loopcraft repose toujours sur **deux vues distinctes** :

### Vue Designer
Le Designer arrive depuis le dashboard Loopcraft.

**Accès :**
- Dashboard Loopcraft
- Bouton retour dashboard
- **Le Panel Designer** (bas-droite)
- **La Design Zone** (modale jaune)
- Commentaires équipe
- Requalification des commentaires
- Catégories : Retour / Idée / Question / Règle de gestion
- Archives
- Sélection et envoi à Claude
- Gestion des propositions, règles, documentation
- Pilotage du wireframe

### Vue PO
Le PO arrive depuis le portail PO (login).

**Accès :**
- Le wireframe (consultation)
- **Le Panel PO** (bas-droite — contenu adapté)
- Règles de gestion (lecture seule)
- Documentation (lecture seule)
- Propositions visibles (si elles existent)
- Possibilité de commenter
- Voir ses propres commentaires

**Interdit pour le PO :**
- Dashboard Loopcraft
- Bouton retour dashboard
- La Design Zone (modale jaune)
- Commentaires équipe
- Requalification
- Archives Designer
- Envoyer à Claude
- Édition des règles / documentation

---

## 4. LE PANEL — DÉFINITION

Le Panel est la **fenêtre flottante bas-droite** (bouton + / −).

Il est présent dans **les deux vues** mais avec un contenu adapté.

**Panel Designer contient :**
- Switches de pilotage (ex: Interfacé, Open tills)
- En cours (version active)
- Propositions (avec actions)
- Commentaires (afficher/masquer pings)
- Documentation (lien vers drawer)

**Panel PO contient :**
- Règles de gestion (lecture seule)
- Documentation (lecture seule)
- Propositions visibles (lecture seule)
- Possibilité de commenter

**Règle absolue :** Ne jamais supprimer le Panel côté PO. `PO = panel PO`, pas `PO = pas de panel`.

---

## 5. LA DESIGN ZONE — DÉFINITION

La Design Zone est la **grande modale** ouverte par le bouton jaune 💬 dans la vue Designer.

Elle est **réservée au Designer uniquement**.

Elle contient :
- Onglet Claude (sélection + envoi)
- Onglet Contexte / RG
- Onglet Commentaires équipe
- Switch Archives
- Tabs : Retour / Idée / Question
- Requalification
- Envoi à Claude ⚡
- Corbeille

**Règle absolue :** Le PO ne doit jamais voir la Design Zone ni le bouton jaune.

---

## 6. LE WORKFLOW COMMENTAIRES

```
PO commente (pin sur wireframe)
→ arrive dans "Commentaires équipe" côté Designer
→ Designer qualifie : Retour / Idée / Question / Règle de gestion
→ peut alimenter une proposition, une règle ou une documentation
→ peut être sélectionné et envoyé à Claude
→ est archivé (jamais supprimé)
```

Ce workflow est l'essence du produit. Il ne doit jamais être cassé.

---

## 7. LES RÔLES — LOGIQUE EXPLICITE

Le rôle ne doit **jamais** dépendre uniquement de `localhost`.

**URLs correctes :**
- Designer : `?role=designer` ou `?designer=1` (depuis dashboard)
- PO : `?role=po&user=Laurent` (depuis portail après login)

**Portail PO :** `portail.html` → login → redirection vers `?role=po&user=NOM`

---

## 8. ÉTATS VIDES

Si un sous-projet n'a pas encore de contenu, la structure doit exister avec des états vides :

- "Aucune proposition"
- "Aucune règle de gestion"
- "Aucune documentation"
- "Aucun commentaire en attente"

Ne jamais inventer du contenu pour remplir l'espace.

---

## 9. RÈGLES ABSOLUES À NE JAMAIS CASSER

1. Ne jamais reconstruire un sous-projet comme une page autonome.
2. Ne jamais casser la séparation Designer / PO.
3. Ne jamais décider du rôle uniquement avec localhost.
4. Ne jamais supprimer le Panel côté PO — le remplacer par le Panel PO.
5. Ne jamais donner la Design Zone au PO.
6. Ne jamais supprimer automatiquement un commentaire.
7. Ne jamais confondre archiver et supprimer.
8. Ne jamais écraser silencieusement les règles de gestion.
9. Ne jamais inventer de documentation ou règles inexistantes.
10. Ne jamais casser l'accès dashboard côté Designer.
11. Ne jamais casser la remontée des commentaires PO vers "Commentaires équipe".
12. Ne jamais modifier le shell Loopcraft pour résoudre un problème de contenu métier.
13. Ne jamais faire dépendre l'essence Loopcraft d'un projet spécifique.

---

## 10. NOUVEAUX PROJETS / SOUS-PROJETS

**Nouveau projet :** hérite du socle Loopcraft — deux vues, workflow commentaires, isolation données.

**Nouveau sous-projet dans un projet existant :**
- Copier le shell du projet parent (ex: Télécollecte V4 pour Club Med)
- Remplacer UNIQUEMENT la zone métier centrale (`<main>`)
- Adapter les 4 clés d'isolation
- Ne jamais reconstruire header/sidebar/panel/Design Zone
