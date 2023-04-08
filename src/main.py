import weaviate

def create_id(obj):
    return weaviate.util.generate_uuid5(obj)
