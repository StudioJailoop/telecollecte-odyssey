#!/usr/bin/env python3
import http.server, subprocess, json, os, time, threading

REWRITE_REQUEST  = '/tmp/wf_rewrite_request.json'
REWRITE_RESPONSE = '/tmp/wf_rewrite_response.json'

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        # Polling : le navigateur demande si la réponse est prête
        if self.path == '/rewrite-result':
            if os.path.exists(REWRITE_RESPONSE):
                with open(REWRITE_RESPONSE, 'r') as f:
                    data = f.read()
                os.remove(REWRITE_RESPONSE)
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(data.encode('utf-8'))
            else:
                self.send_response(204)  # Pas encore prêt
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
        elif self.path.startswith('/get-journal-text/'):
            brief_id = self.path.split('/')[-1]
            import json as _json, os
            fpath = f'/tmp/journal_{brief_id}.json'
            if os.path.exists(fpath):
                with open(fpath) as jf:
                    data = jf.read()
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(data.encode())
            else:
                self.send_response(204)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
        else:
            super().do_GET()

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8')
        data = json.loads(body)

        if self.path == '/send-to-claude':
            prompt = data.get('prompt', '')
            proc = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            proc.communicate(prompt.encode('utf-8'))
            with open('/tmp/claude_prompt.txt', 'w') as f:
                f.write(prompt)
            script = '''
            tell application "System Events"
                set appList to {"Terminal", "iTerm2", "iTerm", "Warp", "Hyper"}
                repeat with appName in appList
                    if exists (processes where name is appName) then
                        tell process appName
                            set frontmost to true
                        end tell
                        exit repeat
                    end if
                end repeat
            end tell
            delay 0.3
            tell application "System Events"
                keystroke "v" using {command down}
            end tell
            '''
            subprocess.run(['osascript', '-e', script], capture_output=True)
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"ok": true}')

        elif self.path == '/rewrite-request':
            # Le navigateur envoie le texte à réécrire
            text = data.get('text', '')
            brief_id = data.get('id', '')
            # Nettoyer l'ancienne réponse
            if os.path.exists(REWRITE_RESPONSE):
                os.remove(REWRITE_RESPONSE)
            # Écrire la demande
            with open(REWRITE_REQUEST, 'w') as f:
                json.dump({'text': text, 'id': brief_id, 'ts': time.time()}, f)
            # Coller le prompt dans le terminal Claude Code
            prompt = f"Réécris ce texte en une phrase courte, précise et professionnelle pour un contexte design produit. Reformule librement. Réponds UNIQUEMENT avec la phrase finale sans guillemets.\n\nTexte : \"{text}\"\n\n(Quand tu as réécris, colle le résultat dans le terminal avec: ! echo '{{ta phrase}}' > /tmp/wf_rewrite_response.json_tmp && python3 -c \"import json; f=open('/tmp/wf_rewrite_response.json_tmp'); t=f.read().strip(); f.close(); open('/tmp/wf_rewrite_response.json','w').write(json.dumps({{'result':t,'id':'{brief_id}'}}))\")"
            proc = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            proc.communicate(prompt.encode('utf-8'))
            # Basculer sur Claude Code
            script = '''
            tell application "System Events"
                set appList to {"Terminal", "iTerm2", "iTerm", "Warp", "Hyper"}
                repeat with appName in appList
                    if exists (processes where name is appName) then
                        tell process appName
                            set frontmost to true
                        end tell
                        exit repeat
                    end if
                end repeat
            end tell
            delay 0.3
            tell application "System Events"
                keystroke "v" using {command down}
            end tell
            '''
            subprocess.run(['osascript', '-e', script], capture_output=True)
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"ok": true, "waiting": true}')


        elif self.path == '/save-journal-text':
            brief_id = data.get('id', '')
            text = data.get('text', '')
            # Écrire dans un fichier que le navigateur peut poller
            import json as _json
            with open(f'/tmp/journal_{brief_id}.json', 'w') as jf:
                _json.dump({'id': brief_id, 'text': text}, jf)
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"ok": true}')

        elif self.path == '/reset-briefs-done':
            # Retourner le script JS à exécuter
            script = 'var b=JSON.parse(localStorage.getItem("wf_briefs_telecollecte")||"[]");b.forEach(x=>x.done=false);localStorage.setItem("wf_briefs_telecollecte",JSON.stringify(b));location.reload();'
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(script.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Serveur démarré sur http://localhost:8765")
http.server.HTTPServer(('', 8765), Handler).serve_forever()
