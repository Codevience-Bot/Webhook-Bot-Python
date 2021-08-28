import os
from flask import Flask, request
from .requests.github_request import GithubRequest
from .hooks import HOOKS_LIST

app = Flask(__name__)

async def dispatch(target, event, action):
    if target in HOOKS_LIST and \
       event in HOOKS_LIST[target] and \
       action in HOOKS_LIST[target][event]:
        return HOOKS_LIST[target][event][action]
    else:
        print(f'Target: {target}, Event: {event}, action {action} not support!')
        return None, False

@app.route("/github", methods=['GET', 'POST'])
async def github_webhook():
    print(request.method)
    if request.method == 'POST':
        req = GithubRequest(request, os.environ.get("github_secret"))
        event = req.event()
        action = req.action()
        router, enabled = await dispatch('github', event, action)
        if enabled:
            router(event, action, req).execute()
    else:
        pass
    return "Codevience GitHub Webhook"

if __name__ == '__main__':
    app.run(port=8080, debug=True)
