---
name: project-loopcraft-prop-b-c-pending
description: "Prop_B et Prop_C — à designer lors de la prochaine session, placeholders statiques actuellement en place"
metadata: 
  node_type: memory
  type: project
  originSessionId: a4b5600a-4d06-4dda-88d0-d5e60db2c5b9
---

## Prop_B et Prop_C — travail en suspens (reprise prévue 2026-05-28)

Après validation de Prop_A et Prop_Abis (commit `764cced`, 2026-05-27), le travail restant porte sur :

### Prop_B — KPI Card (grand format)
- Actuellement : bloc HTML statique avec 3 colonnes (Attendu / Saisi / Écart) en grand format
- À faire : design propre, données dynamiques, intégration cohérente dans le bloc-date

### Prop_C — Badge statut (minimal)
- Actuellement : bloc HTML statique avec une pill "Écart détecté : -5,00 €"
- À faire : design propre, intégration cohérente

### Règle absolue avant tout travail sur B et C
Respecter le **protocole 3 screenshots** (voir [[project-loopcraft-proposals-locked]]) :
1. Screenshot En cours
2. Screenshot Prop_A
3. Screenshot Prop_Abis

→ Si un de ces 3 états change alors qu'il ne devait pas → annuler immédiatement.

**Why:** La zone bloc-date est fragile — Prop_A et Prop_Abis partagent le même DOM parent et ont été validées après une longue boucle de régressions. B et C partagent ce même parent.

**How to apply:** Démarrer la session en prenant les 3 screenshots de référence, puis travailler B et C comme des blocs HTML isolés dans leur `id="proposal-b"` et `id="proposal-c"` respectifs.
