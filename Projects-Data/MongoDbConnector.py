import json
import pymongo

def MongoDbConnectorFn(env_name):
    print("MongoDbConnectorFn Called with parameter: " + env_name)
    default_env = "dev"
    env = env_name
    if not env or env is None:
        env = default_env
    with open("config.json", "r") as f:
        config = json.load(f)

    # choose environment
    # region environment-related variables
    connection_string = config[env]["connection_string"]
    db_name = config[env]["db_name"]
    collection_name = config[env]["collection_name"]
    # endregion

    # region Connect to Mongodb
    print("Environment = " + env)
    print("Connecting to mongodb...")
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    collection = db[collection_name]
    print("Connected to: " + db_name + "." + collection_name)
    # endregion

    return client
