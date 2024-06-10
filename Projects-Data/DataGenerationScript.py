import json
from MongoDbConnector import MongoDbConnectorFn
import Faker
from ProjectModel import ProjectModel
from VersionModel import VersionModel

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


def main():
    print("DataScriptForProjectsCollection.py main() called")

    # create test data for mongodb collection using the class found in the ProjectModel.py file

    guid = Faker.Guid()

    client.close()


main()
