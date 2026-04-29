import json
import sys
import os
def load_config(environment)->dict:
    # print("file path ",__file__)
    # print(os.path.dirname(__file__))
    try:
     with open(os.path.join(os.path.dirname(__file__),'config.json'),'r') as jsfile:
        data=json.load(jsfile)
    except FileNotFoundError:
        print("config.json file is not available")
        sys.exit(1)
    except json.JSONDecodeError:
        print("The file does not contain valid json data")
        sys.exit(1)
    return data[environment]
       
    

