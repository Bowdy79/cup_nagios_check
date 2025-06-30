import json
import docker

# Connect to docker to load JSON
client = docker.DockerClient(base_url='unix://var/run/docker.sock')
v = {'/var/run/docker.sock': {'bind':'/var/run/docker.sock', 'mode':'ro'}}
e = {'CUP_IGNORE_UPDATE_TYPE': 'major'}
j = client.containers.run('ghcr.io/sergi0g/cup', volumes=v, environment=e, detach=False, stdout=True, command='check -r')

jsonDump = json.loads(j)

class Image:
    in_use = False
    parts = []
    reference = ""
    result = []
    server = ""
    time = 0
    url = ""
    nagios_exit_code = 3
    nagios_short_message = "UNKNOWN - Error while checking for updates!"
    nagios_long_message = ""

    def __init__(self, imageJson):
        self.in_use = imageJson['in_use']
        self.parts = imageJson['parts']
        self.reference = imageJson['reference']
        self.result = imageJson['result']
        self.server = imageJson['server']
        self.time = imageJson['time']
        self.url = imageJson['url']
        if self.result['has_update']:
            self.nagios_exit_code = 1
            self.nagios_short_message = "WARNING - Container image updates available!"
            self.nagios_long_message = f"{self.parts['repository']} - {self.url}"
        else:
            self.nagios_exit_code = 0
            self.nagios_short_message = "OK - All containers up to date."

containers = []
updates_available = 0

for i in jsonDump['images']:
    imageObj = Image(i)
    containers.append(imageObj)
   
highest_exit_code = 0
highest_short_message = "OK - All containers up to date."
highest_long_messages = []

for h in containers:
    if h.nagios_exit_code > highest_exit_code:
        highest_exit_code = h.nagios_exit_code
        highest_short_message = h.nagios_short_message
    if h.nagios_exit_code > 0:
        highest_long_messages.append(h.nagios_long_message)

print(highest_short_message)
for lm in highest_long_messages:
    print(lm)
exit(highest_exit_code)