import json

j = '{"images":[{"in_use":true,"parts":{"registry":"registry-1.docker.io","repository":"triliumnext/notes","tag":"latest"},"reference":"triliumnext/notes:latest","result":{"error":null,"has_update":false,"info":null},"server":null,"time":155,"url":"https://github.com/TriliumNext/Notes"},{"in_use":true,"parts":{"registry":"registry-1.docker.io","repository":"vaultwarden/server","tag":"latest"},"reference":"vaultwarden/server:latest","result":{"error":null,"has_update":false,"info":null},"server":null,"time":333,"url":"https://github.com/dani-garcia/vaultwarden"},{"in_use":true,"parts":{"registry":"ghcr.io","repository":"sergi0g/cup","tag":"latest"},"reference":"ghcr.io/sergi0g/cup:latest","result":{"error":null,"has_update":false,"info":null},"server":null,"time":149,"url":"https://github.com/sergi0g/cup"},{"in_use":true,"parts":{"registry":"registry-1.docker.io","repository":"jc21/nginx-proxy-manager","tag":"latest"},"reference":"jc21/nginx-proxy-manager:latest","result":{"error":null,"has_update":false,"info":null},"server":null,"time":369,"url":null}],"metrics":{"major_updates":0,"minor_updates":0,"monitored_images":4,"other_updates":0,"patch_updates":0,"unknown":0,"up_to_date":4,"updates_available":0}}'

jsonDump = json.loads(j)

class Image:
    in_use = False
    parts = []
    reference = ""
    result = []
    server = ""
    time = 0
    url = ""

    def __init__(self, imageJson):
        self.in_use = imageJson['in_use']
        self.parts = imageJson['parts']
        self.reference = imageJson['reference']
        self.result = imageJson['result']
        self.server = imageJson['server']
        self.time = imageJson['time']
        self.url = imageJson['url']

    def updateable(self):
        if self.result['has_update']:
            return True
        else:
            return False

containers = []
updates_available = 0

for x in jsonDump['images']:
    imageObj = Image(x)
    containers.append(imageObj)

for c in containers:
    c.updateable()


    