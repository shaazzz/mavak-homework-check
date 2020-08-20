import json


class FileDict:
    def __init__(self, address, dictionary=None):
        if dictionary is None:
            self.address = address
            with open(self.address, 'r') as file:
                self.dict = json.loads(file.read())
        else:
            self.address = address
            self.set_dict(dictionary)

    def set_dict(self, dictionary):
        self.dict = dictionary
        with open(self.address, 'w') as file:
            file.write(json.dumps(self.dict, indent=4, sort_keys=True))

    def __setitem__(self, key, value):
        self.dict[key] = value
        with open(self.address, 'w') as file:
            file.write(json.dumps(self.dict, indent=4, sort_keys=True))

    def __getitem__(self, item):
        return self.dict[item]
