import json
from MongoDbConnector import MongoDbConnectorFn
import Faker

# load config file for connection string
with open("config.json", "r") as f:
    config = json.load(f)

# client related variables
env = "local"
db_name = config[env]["db_name"]
collection_name = config[env]["collection_name"]
# connect to client
client = MongoDbConnectorFn(env)
db = client[db_name]
collection = db[collection_name]
guid = Faker.Guid()


def main():
    print("DataScriptForProjectsCollection.py main() called")

    # create test data for mongodb collection using the class found in the ProjectModel.py file
    from ProjectModel import ProjectModel

    client.close()


main()
