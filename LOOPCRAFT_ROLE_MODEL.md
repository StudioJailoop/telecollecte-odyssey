# LOOPCRAFT — MODÈLE DE RÔLES

---

## Calcul du rôle

```javascript
const params = new URLSearchParams(location.search);
const role = params.get('role');
const isDesigner = role === 'designer' || params.get('designer') === '1';
const isPO = role === 'po';
const CURRENT_USER = decodeURIComponent(params.get('user') || 'Sébastien');
```

**Jamais :** `isDesigner = location.hostname === 'localhost'`

---

## role = designer

| Permission | Valeur |
|---|---|
| canAccessDashboard | true |
| canOpenDesignZone | true |
| canRequalifyComments | true |
| canArchive | true |
| canSendToClaude | true |
| canEditDocumentation | true |
| canEditRules | true |
| canViewDesignerPanel | true |
| canViewPoPanel | false |
| canComment | true |
| canViewDashboardBtn | true |

**Éléments affichés :**
- Bouton retour dashboard (`#back-dashboard-btn`)
- Bouton Design Zone jaune (`#briefs-nav-btn`)
- Panel Designer (`#wf-panel` version designer)
- Tous les outils de la Design Zone

---

## role = po

| Permission | Valeur |
|---|---|
| canAccessDashboard | false |
| canOpenDesignZone | false |
| canRequalifyComments | false |
| canArchive | false |
| canSendToClaude | false |
| canEditDocumentation | false |
| canEditRules | false |
| canViewDesignerPanel | false |
| canViewPoPanel | true |
| canComment | true |
| canViewDocumentation | true |
| canViewRules | true |
| canViewDashboardBtn | false |

**Éléments affichés :**
- Panel PO (`#wf-panel` version PO — lecture seule)
- Bouton commentaire PO (bas-droite, via `createPoPanel()`)
- Règles de gestion (lecture seule)
- Documentation (lecture seule)
- Propositions visibles (lecture seule)

**Éléments masqués :**
- `#back-dashboard-btn`
- `#briefs-nav-btn`
- Tout le contenu de la Design Zone
