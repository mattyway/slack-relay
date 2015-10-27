import json
import os
import pprint
import requests
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

url = os.environ['SLACK_HOOK']
port = int(os.environ['RELAY_PORT'])
docker_icon_url = 'https://pbs.twimg.com/profile_images/378800000124779041/fbbb494a7eef5f9278c6967b6072ca3e_200x200.png'
headers = {'content-type': 'application/json'}

def make_slack_post(docker_data):
    repo = docker_data['repository']
    return {
        'username': 'Docker Hub',
        'text': '<{}|{}> built successfully.'.format(repo['repo_url'], repo['repo_name']),
        'icon_url': docker_icon_url
    }

class Relay(Resource):
    def render_GET(self, request):
        return '<html><body>Relay is running.</body></html>'

    def render_POST(self, request):
        print request.args
        payload = make_slack_post(json.loads(request.content.read()))
        pprint.pprint(payload)
        return requests.post(url, data=json.dumps(payload), headers=headers)

root = Resource()
root.putChild('relay', Relay())
factory = Site(root)
reactor.listenTCP(port, factory)
reactor.run()