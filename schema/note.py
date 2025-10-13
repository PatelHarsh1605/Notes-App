def noteEntitey(item) -> dict :
    return {
        "id" : str(item["_id"]),
        "title" : item["title"],
        "desc" : item["desc"],
        "importent" : item["important"]
    }

def notesEntitey(items) -> list :
    return [noteEntitey(item) for item in items]