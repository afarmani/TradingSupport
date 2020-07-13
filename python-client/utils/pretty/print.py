import json


def ppjson(value):
    # clean up JSON Response
    json_data = str(value)
    json_data = json_data.replace('\'', '\"')
    json_data = json_data.replace("True", "true")
    json_data = json_data.replace("False", "false")

    data = json.loads(json_data)
    json_formatted_str = json.dumps(data, indent=2)
    print(json_formatted_str)
