import json
import bson
from MongoDbConnector import MongoDbConnectorFn
import faker
from ProjectModel import ProjectModel
from VersionModel import VersionModel
from ContactModel import ContactModel
import datetime
import uuid
import base64


# load config file for connection string
with open("pathToConfigFile\\config.json", "r") as f:
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
    # create a faker object
    fake = faker.Faker()
    listOfProjects = []

    for i in range(40000):
        if i % 1000 == 0:
            print("Creating project number: " + str(i))

        fakePrimaryContact = ContactModel(
            firstName=fake.first_name(),
            lastName=fake.last_name(),
            phone=fake.phone_number(),
            email=fake.email(),
            fax=fake.phone_number(),
        )

        fakeSecondaryContact = ContactModel(
            firstName=fake.first_name(),
            lastName=fake.last_name(),
            phone=fake.phone_number(),
            email=fake.email(),
            fax=fake.phone_number(),
        )

        fakeTertiaryContact = ContactModel(
            firstName=fake.first_name(),
            lastName=fake.last_name(),
            phone=fake.phone_number(),
            email=fake.email(),
            fax=fake.phone_number(),
        )

        fakeVersion = VersionModel(
            stage=fake.random_int(min=0, max=3),
            alternate=VersionModel.validAlternateValues[fake.random_int(min=0, max=13)],
            revision=fake.random_number(digits=2),
            name=fake.company(),
            notes=fake.text(),
            isPrimary=fake.boolean(chance_of_getting_true=50),
            isActive=fake.boolean(chance_of_getting_true=50),
        )

        # Generate a guid for both the _id and aliasId

        guidID = bson.binary.Binary(uuid.uuid4().bytes, 3)
        aliasGuid = bson.binary.Binary(uuid.uuid4().bytes, 3)

        # create a project model object. Should be 36 fields.
        project = ProjectModel(
            guid=guidID,
            aliasof=aliasGuid,
            name=fake.street_name(),
            projectNumber=fake.random_number(digits=7),
            opportunityId=ProjectModel.CreateStringId(18),
            status=ProjectModel.validStatusValues[fake.random_int(min=0, max=3)],
            repNumber=fake.random_number(digits=7),
            repName=fake.company(),
            specPosition=ProjectModel.validSpecPositionValues[fake.random_int(min=0, max=16)],
            wsApprovedEqual=fake.boolean(chance_of_getting_true=50),
            verticalMarket=ProjectModel.validVerticaMarketValues[fake.random_int(min=0, max=7)],
            verticalMarketSubsegment=ProjectModel.validVerticalMarketSubsegmentValues[fake.random_int(min=0, max=8)],
            specifierId=ProjectModel.CreateStringId(18),
            specifierName=fake.company(),
            createdBy=fake.user_name(),
            createdByName=fake.name(),
            createdDate= fake.date_this_year(before_today=True, after_today=False).strftime("%Y-%m-%d %H:%M:%S"),
            lastModifiedBy=fake.user_name(),
            lastModifiedByName=fake.name(),
            lastModified=fake.date_this_year(before_today=True, after_today=False).strftime("%Y-%m-%d %H:%M:%S"),
            closeDate=fake.date_this_year(before_today=False, after_today=True).strftime("%Y-%m-%d %H:%M:%S"),
            notes=fake.text(),
            description=fake.text(),
            sequenceOfOperations=ProjectModel.validSequenceOfOperationsValues[fake.random_int(min=0, max=7)],
            sqFootage=fake.random_number(digits=4),
            defaultSpaceColor=fake.color_name(),
            showProductsFromFloorplan=fake.boolean(chance_of_getting_true=50),
            tenantId=ProjectModel.validTenantIdValues[fake.random_int(min=0, max=1)],
            city=fake.city(),
            state=fake.state(),
            zipCode=fake.zipcode(),
            country=fake.country(),
            primaryContact=fakePrimaryContact,
            secondaryContact=fakeSecondaryContact,
            tertiaryContact=fakeTertiaryContact,
            version=fakeVersion
        )

        # Convert the ProjectModel instance to a dictionary
        project_dict = project.__dict__

        # Convert the ContactModel and VersionModel instances to dictionaries
        fakePrimaryDict = fakePrimaryContact.__dict__
        fakeSecondaryDict = fakeSecondaryContact.__dict__
        fakeTertiaryDict = fakeTertiaryContact.__dict__
        fakeVersionDict = fakeVersion.__dict__

        project_dict["PrimaryContact"] = fakePrimaryDict
        project_dict["SecondaryContact"] = fakeSecondaryDict
        project_dict["TertiaryContact"] = fakeTertiaryDict
        project_dict["Version"] = fakeVersionDict

        # Append the project dictionary to the list
        listOfProjects.append(project_dict)

    # insert the list of projects into the collection
    collection.insert_many(listOfProjects)

    # Convert the project dictionary to a JSON string.
    # Creating a mongo importable file requries a different structure for binary uuid than
    # an insert many operation. Will need to convert first. Then make a json file
    projectJson = ConvertUuidfromGUIDToBase64String(listOfProjects)
    projectJson = json.dumps(project_dict)
    print(projectJson)


    dateToday = str(datetime.date.today())
    fileName = "projectsData_" + dateToday + ".json"
    CreateFileFn(fileName, listOfProjects)

    # close the client

    client.close()


def CreateMongoIdObjectFn(guidString):
    return {"$binary": {"base64": guidString, "subType": "03"}}


def CreateFileFn(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def ConvertUuidfromGUIDToBase64String(projectList):
    for project in projectList:
        project["_id"] = CreateMongoIdObjectFn(base64.b64encode(project["_id"]).decode('utf-8'))
        project["AliasOf"] = CreateMongoIdObjectFn(base64.b64encode(project["AliasOf"]).decode('utf-8'))


    return projectList


main()
