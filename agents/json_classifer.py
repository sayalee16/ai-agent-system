import json
def process_json(json_text):
            data = json.loads(json_text)
            return {
                "type": "json",
                "keys": list(data.keys()),
                "data": data
            }