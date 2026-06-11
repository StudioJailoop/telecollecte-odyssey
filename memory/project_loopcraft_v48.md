---
name: project-loopcraft-v48
description: État V4.8 du wireframe Télécollecte — features stables avant nouvelles évolutions
metadata: 
  node_type: memory
  type: project
  originSessionId: a4b5600a-4d06-4dda-88d0-d5e60db2c5b9
---

Version de référence sauvegardée le 2026-06-03 : **wireframe-telecollecte-cas1-V4.8.html**

**Why:** Point de sauvegarde explicitement demandé par Sébastien avant d'ajouter de nouvelles features. "Revenir à V4.8" = restaurer ce fichier.

**How to apply:** Si régression → `cp wireframe-telecollecte-cas1-V4.8.html wireframe-telecollecte-cas1-V4.html && git add . && git commit && git push`

### Features stables dans V4.8

**Mode interfacé / non-interfacé**
- KPI dynamiques : Montant attendu (∑ c-amt), Montant saisi (attendu + corrections), Écart (∑ corrections)
- Mode non-interfacé : Montant attendu / Écart / badges masqués, Montant saisi = somme saisies manuelles
- Badge vert "Aucun écart" / rouge "Écart détecté" synchronisés en temps réel
- Pill sticky synchronisée avec l'état réel (masquée si écart = 0)
- Colonne renommée "Montant attendu" (ex "Montant calculé")

**Panel wf-panel (bouton +)**
- Section Documentation en bas, masquée quand panel fermé
- Entrée "📘 Règles de gestion →" → ouvre le drawer doc full-screen

**Drawer Documentation (full-screen)**
- Sommaire sticky à gauche : sections par écran, badge RG-01/02… violet + titre, clic → scroll smooth
- Intro générale : titre, date, contexte produit, badges nombre de RG / écrans
- Chaque bloc : `RG-01` numéroté, badges Onglet + Mode, Règle / Comportement (fond gris) / Critère (barre verte)
- Bouton "📋 Copier pour Jira" par bloc → texte structuré dans le presse-papier

**Blocs RG pré-chargés**
- RG-01 : Logique des montants en mode interfacé (Télécollecte · Interfacé)
- RG-02 : Logique des montants en mode non interfacé (Télécollecte · Non interfacé)

**Panel Design Zone (briefs)**
- Titre renommé "Design Zone"
- Onglet PRD supprimé
- Header "Documentation fonctionnelle" supprimé du tab Documentation

**Règle fondatrice mise à jour**
- Tous les commentaires (designer inclus) arrivent dans Commentaires équipe — filtre `author !== DESIGNER` retiré
