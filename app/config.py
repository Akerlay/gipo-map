import json


class Config:
    def __init__(self, json_path='config.json', required_fields=None):
        cf_map = json.load(open(json_path, 'r'))

        if required_fields:
            cf_changed = False
            for field in required_fields:
                if field not in cf_map:
                    cf_map[field] = input(field + ': ')
                    cf_changed = True

            if cf_changed:
                json.dump(cf_map, open(json_path, 'w'))

        self.__dict__ = cf_map

    def __getitem__(self, key):
        return self.__dict__.get(key)


