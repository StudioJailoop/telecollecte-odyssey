# CURRENT_STATE.md — État actuel du produit

**Version active : V4** | Commit : `6f07285` | Date : 2026-05-19

---

## Ce qui fonctionne parfaitement

### Wireframe — 3 onglets
- **Télécollecte** : tableau par TPE (5 TPE), modes interfacé/non-interfacé, validation montant+remise, bouton "Valider la saisie" (Saffran yellow DS)
- **Date antérieure** : tableau avec colonnes régularisation séparées, validation montant+remise, bouton "Valider la saisie" en footer
- **Régularisation** : total écart + 3 champs MDP, calcul auto, bouton "Faire une régularisation" (gris si total ≠ écart, navy si OK)

### Navigation
- Tabs principales : pills navy actif
- Tabs TPE Tertiary : sticky au scroll, fond transparent → blanc
- Bouton "Valider la saisie" sticky dans la barre TPE
- Sidebar fermée par défaut (94px), toggle cercle

### Système de commentaires (PO)
- Pins ancrés dans `.content` (px absolus, scrollent avec le contenu)
- Couleur par auteur : Sébastien=#1E2643, Julie=#7C3AED, Nelly=#059669, Jérôme=#DC2626, Kirsty=#0891B2, Laurent=#D97706
- Label : NombreInitiale (1S, 2L, 3J...)
- Clic = ouvre thread, reclique = ferme (toggle)
- Drag volontaire uniquement (>8px mouvement)
- Pas de sélection texte pendant drag
- Thread : réponses, catégorisation, zone "Dernières modifs" pour Sébastien
- Firebase sync toutes les 5s

### Outil Retours PO (Sébastien uniquement — localhost)
- Bouton jaune bulle bas-gauche
- **Ligne 1** : ⚡ Claude | 💬 Commentaires équipe | switch "Archivés"
- **Ligne 2** : 💬 Retour | 💡 Idée | 📋 Règle de gestion | ❓ Question
- Switch Archivés ON : masque Claude+Commentaires équipe, affiche pill "📋 Journal des modifs"
- Par carte : ⚡ éclair Claude + ↻ réécriture IA + ✏️ édition + ⇄ reclassification + ✓ check bulle + 🗑 poubelle
- Corbeille 30j avec restauration
- Section Claude : sélection → prompt structuré → envoi
- Journal des modifs : format éditorial, numérotation, texte narratif généré par IA

### Archivage (RÈGLE CRITIQUE)
- `done=true` **uniquement** sur les briefs dans `claudeSelection` après envoi Claude réussi
- JAMAIS `briefs.forEach(b => b.done=true)`
- Badges en mode Archives comptent les `done=true`, en mode normal les `done=false`

---

## Ce qui est en cours / incomplet

- **Bouton "Faire une régularisation"** : visible mais grisé par défaut (normal — activé uniquement quand total = écart). Bug possible d'affichage selon le cache.
- **Reformulation journal IA** : fonctionne via pont server.py → Claude Code mais nécessite intervention manuelle. Sera automatique avec crédit Anthropic.
- **Commentaires PO partagés** : Firebase sync côté Sébastien OK. Côté PO sur GitHub Pages : localStorage local seulement (pas de sync cross-device sans Firebase côté PO).

---

## Versions sauvegardées

| Version | Fichier | Description |
|---------|---------|-------------|
| V1 | `wireframe-telecollecte-cas1-V1.html` | Structure de base |
| V2 | `wireframe-telecollecte-cas1-V2.html` | Tabs TPE + validation |
| V3 | `wireframe-telecollecte-cas1-V3.html` | Outil PO complet |
| **V4** | `wireframe-telecollecte-cas1-V4.html` | **Version active** |
| V4-REF | `wireframe-telecollecte-cas1-V4-REF.html` | **Référence immuable** |
