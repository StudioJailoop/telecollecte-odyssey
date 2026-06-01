# UX_RULES.md

## Contexte métier

**Module** : Saisie des Télécollectes TPE — Club Med Odyssey
**Utilisateurs** : Réceptionnistes Night Audit (profil GO interne Club Med)
**Moment d'usage** : En fin de journée (~21h-01h), après fermeture de toutes les caisses

## Les 3 cas d'usage (onglets)

### 1. Télécollecte (Jour J)
- **Qui** : Réceptionniste profil standard
- **Quand** : Soir même, avant ~1h du matin
- **Condition** : Toutes les caisses fermées (sinon alerte bloquante)
- **Action** : Saisir montant + n° remise par mode de paiement (Visa/Amex/WeChat) par TPE
- **Village interfacé** : montants pré-remplis, modifiables
- **Village non interfacé** : saisie 100% manuelle
- **CTA** : "Valider la saisie" (Saffran yellow, disabled jusqu'à validation)

### 2. Date antérieure
- **Qui** : Réceptionniste (à confirmer si manager requis)
- **Quand** : Le lendemain ou après, si J-1 n'a pas été saisi
- **Condition** : Aucune (caisses peuvent être ouvertes)
- **Action** : Saisir colonnes régularisation (montant + n° remise) sur données existantes
- **CTA** : "Valider la saisie" en footer

### 3. Régularisation
- **Qui** : Financier / profil supérieur uniquement
- **Quand** : N'importe quand
- **Action** : Corriger un écart — saisir la répartition par mode de paiement
- **Logique** : Somme des champs = Total écart → bouton actif
- **CTA** : "Faire une régularisation" (gris si écart ≠ 0, navy si OK)

## Règles UX critiques

### Validation montant/remise
- Si montant saisi → n° remise OBLIGATOIRE
- Champ remise en erreur (`border: #BF2F17`) si montant sans remise
- Bouton disabled tant qu'une erreur existe
- Les rows masquées (`display:none`) sont ignorées par la validation

### Navigation
- Sidebar fermée par défaut (94px) — l'utilisateur ouvre si besoin
- Tabs TPE : sticky au scroll, fond transparent → blanc avec ombre
- Bouton "Valider" sticky dans la barre TPE
- Changement d'onglet principal → pins se masquent/affichent selon tab

### Pins de commentaires
- Position ABSOLUE dans `.content` — suivent le scroll
- Clic simple = ouvre/ferme thread (toggle)
- Drag uniquement si déplacement > 8px (évite les déplacements accidentels)
- Cursor crosshair en mode commentaire, normal si thread ouvert
- Impossible de poser un pin si thread ouvert

### Outil Retours PO
- **Sébastien uniquement sur localhost** — invisible sur GitHub Pages
- Bouton jaune bulle bas-gauche
- Archives ON : masque Claude + Commentaires équipe, affiche Journal des modifs
- Un brief = `done:true` SEULEMENT si envoyé via Claude (claudeSelection)
- Badges en mode normal = éléments actifs / en mode Archives = éléments archivés

## Flows utilisateur

### Flow Night Audit (cas typique)
1. Se connecte sur Odyssey
2. S'assure que toutes les caisses sont fermées
3. Va dans Cash register → Télécollecte
4. Sélectionne TPE 1, saisit Visa/Amex/WeChat + n° remise
5. Navigue via tabs TPE vers TPE 2, 3...
6. Clique "Valider la saisie" → confirmation

### Flow collaboration PO
1. Sébastien crée le wireframe et partage le lien GitHub
2. PO (Julie, Nelly...) se connecte avec son ID/mdp
3. PO active le mode commentaire (bulle jaune bas-droite)
4. PO clique sur une zone → popover avec choix de type + texte
5. Pin ancré à l'endroit exact, numéroté et coloré
6. Sébastien voit le pin dans sa session (Firebase sync 5s)
7. Sébastien ouvre sa modale Retours PO → catégorise, sélectionne pour Claude
8. Génère prompt → envoie → Claude modifie le wireframe
9. Brief passe en Archives avec texte narratif généré

## Anti-patterns UX identifiés

- ❌ Afficher "Régularisation" sans montrer clairement que c'est profil financier
- ❌ Laisser la corbeille accessible sans confirmation de suppression définitive
- ❌ Marquer des briefs comme traités sans action Claude explicite
- ❌ Ouvrir la sidebar par défaut (trop envahissant sur l'écran de saisie)
- ❌ Utiliser un texte barré pour indiquer le statut "traité" (peu lisible)
