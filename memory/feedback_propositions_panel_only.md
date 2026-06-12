---
name: feedback-propositions-panel-only
description: Le switcher de propositions doit être UNIQUEMENT dans le wf-panel, jamais dans le corps de la maquette
metadata:
  type: feedback
---

Le switcher de propositions (Prop A / B / C) doit toujours être dans la section PROPOSITIONS du wf-panel — jamais dans le corps du wireframe.

**Why:** Le client voit le wireframe sans le panel. Si le switcher est dans la maquette, il apparaît devant le client lors des présentations, ce qui est inacceptable.

**How to apply:** Tout nouveau wireframe avec plusieurs propositions → switcher exclusivement dans `wf-panel > section Propositions`. Jamais de `prop-switcher-bar` ou équivalent dans le contenu visible.
