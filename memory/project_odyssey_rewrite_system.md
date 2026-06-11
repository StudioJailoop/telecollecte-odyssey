---
name: Système de réécriture IA via serveur local
description: Workflow validé pour réécrire les commentaires PO via Claude Code sans API externe
type: project
originSessionId: 9f8442c3-4d5c-4465-87b8-99549a3d219e
---
Le système de réécriture IA fonctionne via un pont local :

1. Clic ↻ dans la modale → POST /rewrite-request → prompt collé automatiquement dans Claude Code
2. Claude réécrit et exécute une commande python3 qui écrit dans /tmp/wf_rewrite_response.json
3. Le navigateur poll /rewrite-result toutes les 2s → champ mis à jour automatiquement

**Why:** Pas de clé API Anthropic disponible côté Club Med. Ce système utilise Claude Code directement comme moteur de réécriture via fichier de transit.

**How to apply:** Toujours utiliser server.py (pas python3 -m http.server). Ne jamais supprimer les routes /rewrite-request et /rewrite-result. La commande d'injection du résultat est : `python3 -c "import json; open('/tmp/wf_rewrite_response.json','w').write(json.dumps({'result':'TEXTE','id':'ID'}))"`
