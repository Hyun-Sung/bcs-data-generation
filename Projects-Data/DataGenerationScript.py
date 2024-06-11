import json
from MongoDbConnector import MongoDbConnectorFn
import faker
from ProjectModel import ProjectModel
from VersionModel import VersionModel
from ContactModel import ContactModel

# load config file for connection string
with open("C:\\Users\\hsung1a\\PycharmProjects\\bcs-data-generation\\config.json", "r") as f:
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

    for i in range(1000):

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
            alternate=fake.boolean(chance_of_getting_true=50),
            revision=fake.random_number(digits=2),
            name=fake.company(),
            notes=fake.text(),
            isPrimary=fake.boolean(chance_of_getting_true=50),
            isActive=fake.boolean(chance_of_getting_true=50),
        )

        # create a project model object. Should be 36 fields.
        project = ProjectModel(
            guid=fake.uuid4(),
            aliasof=fake.uuid4(),
            name=fake.building_name(),
            projectNumber=fake.random_number(digits=7),
            opportunityId=fake.random_number(digits=18),
            status=ProjectModel.validStatusValues[fake.random_int(min=0, max=3)],
            repNumber=fake.random_number(digits=7),
            repName=fake.company(),
            specPosition=ProjectModel.validSpecPositionValues[fake.random_int(min=0, max=16)],
            wsApprovedEqual=fake.boolean(chance_of_getting_true=50),
            verticalMarket=ProjectModel.validVerticaMarketValues[fake.random_int(min=0, max=7)],
            verticalMarketSubsegment=ProjectModel.validVerticalMarketSubsegmentValues[fake.random_int(min=0, max=8)],
            specifierId=fake.random_string(length=18),
            specifierName=fake.company(),
            createdBy=fake.company_id(),
            createdByName=fake.full_name(),
            createdDate=fake.date_this_year(before_today=True, after_today=False),
            lastModifiedBy=fake.company_id(),
            lastModifiedByName=fake.full_name(),
            lastModified=fake.date_this_year(before_today=True, after_today=False),
            closeDate=fake.date_this_year(before_today=False, after_today=True),
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

    client.close()


main()
