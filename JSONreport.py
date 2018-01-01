import json
from pprint import pprint

_author_ = 'Sarath'


class JSONreport:

    def readjson(self):
        data = json.load(open('sample.json'))
        # pprint(data)

JSONreport().readjson()
