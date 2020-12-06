import uuid, re

def strip_payload(payload, strip_ids=False):
    stripped_payload = {}
    for key in payload:
        if payload[key] is not None:
            if not strip_ids or (strip_ids and not re.search("_id", key)):
                stripped_payload[key] = payload[key]
    return stripped_payload

def is_valid_uuid(id_string):
    try:
        return uuid.UUID(id_string)
    except ValueError:
        return False
