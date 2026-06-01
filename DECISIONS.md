# DECISIONS.md — Décisions importantes

## Design

| Décision | Raison | Alternative rejetée |
|----------|--------|---------------------|
| Sidebar fermée par défaut | L'écran de saisie doit être maximisé | Sidebar ouverte |
| Tabs TPE en Tertiary DS (underline) | Moins envahissant que les pills | Tabs pills |
| Bouton Valider sticky dans barre TPE | Toujours accessible sans scroller | Footer seul |
| Pins en position absolue dans .content | Restent à leur position même au scroll | Position fixed |
| Drag uniquement si >8px | Évite les déplacements accidentels | Drag immédiat |
| Archives via switch (pas onglet) | Plus élégant, ne change pas la structure | 5e onglet |
| Journal des modifs format éditorial | Lisibilité, sentiment de newsletter | Liste simple |
| Bouton check bulle vert | Plus clair qu'un texte barré | Texte barré |
| Corbeille 30j | Éviter les suppressions accidentelles | Suppression directe |

## Technique

| Décision | Raison |
|----------|--------|
| HTML/CSS/JS inline (zero deps) | Portabilité maximale, pas de build |
| Firebase pour les pins (pas localStorage cross-device) | Sync temps réel entre POs |
| server.py comme pont IA | Pas de clé API Anthropic disponible côté Club Med |
| launchd pour auto-restart serveur | Plus jamais "le serveur a sauté" |
| `style.setProperty('display','flex','important')` | Contourne les styles inline récalcitrants |

## Produit

| Décision | Raison |
|----------|--------|
| Accès PO via portail avec mdp | Protection minimale, simple pour les POs |
| Bouton Retours PO uniquement sur localhost | Les POs ne doivent pas voir l'outil designer |
| Couleur pin par auteur (pas par type) | Identifier rapidement qui a commenté |
| Prompt structuré avec contexte DS | Claude doit respecter Trident 2.0 sans rappel |
| "Faire une régularisation" (pas "Valider") | Sémantique métier correcte pour ce profil financier |
| "Valider la saisie" sur Date antérieure | Cohérent — c'est bien une saisie de données |

## Ce qui a été rejeté

- ❌ Drag des pins → trop de déplacements accidentels → drag volontaire (>8px)
- ❌ Badge compteur sur Archives → inutile, pollue visuellement → supprimé
- ❌ Text barré pour les traités → peu lisible → bulle check verte
- ❌ Reset forcé à chaque chargement → efface les vrais archivés → reset one-time avec flag
- ❌ Tab "Archives" séparée → mélange les catégories → switch + mêmes tabs
