#!/usr/bin/python3
import json
def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelguesian"}, {"name": "Arthur Dent", "species": "Human"}]
    for character in hitchhikers:
        print(character.get("name"))
    hitchhikers.append({"name": None, "species": "human"})
    with open("galaxyguide.json", "w") as jfile:
        json.dump(hitchhikers, jfile)
    jsonstring = json.dumps(hitchhikers)
    print(jsonstring)
    with open("datacenter.json") as jread:
        dc_str = jread.read()
        print(type(dc_str))
    dc_json = json.loads(dc_str)
    print(type(dc_json))
if __name__ == "__main__":
    main()
