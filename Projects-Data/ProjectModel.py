import random
import string


class ProjectModel:
    def __init__(self, guid, aliasof, name, projectNumber, opportunityId, status, repNumber, repName, specPosition,
                 wsApprovedEqual, verticalMarket, verticalMarketSubsegment, specifierId, specifierName, createdBy,
                 createdByName, createdDate, lastModifiedBy, lastModifiedByName, lastModified, closeDate, notes, description,
                 sequenceOfOperations, sqFootage, defaultSpaceColor, showProductsFromFloorplan, tenantId, city, state,
                 zipCode, country, primaryContact, secondaryContact, tertiaryContact, version):
        self._id = guid
        self.AliasOf = aliasof
        self.Name = name
        self.ProjectNumber = projectNumber
        self.OpportunityId = opportunityId
        self.Status = status
        self.RepNumber = repNumber
        self.RepName = repName
        self.SPECPosition = specPosition
        self.WSApprovedEqual = wsApprovedEqual
        self.VerticalMarket = verticalMarket
        self.VerticalMarketSubsegment = verticalMarketSubsegment
        self.SpecifierId = specifierId
        self.SpecifierName = specifierName
        self.CreatedBy = createdBy
        self.CreatedByName = createdByName
        self.CreatedDate = createdDate
        self.LastModifiedBy = lastModifiedBy
        self.LastModifiedByName = lastModifiedByName
        self.LastModified = lastModified
        self.CloseDate = closeDate
        self.Notes = notes
        self.Description = description
        self.SequenceOfOperations = sequenceOfOperations
        self.sqFootage = sqFootage
        self.DefaultSpaceColor = defaultSpaceColor
        self.ShowProductsFromFloorplan = showProductsFromFloorplan
        self.TenantId = tenantId
        self.City = city
        self.State = state
        self.ZipCode = zipCode
        self.Country = country
        self.PrimaryContact = primaryContact
        self.SecondaryContact = secondaryContact
        self.TertiaryContact = tertiaryContact
        self.Version = version

    validVerticaMarketValues = ["Education", "Healthcare", "Hospitality", "Office", "Public Space", "Residential", "Retail", "Other"]
    validVerticalMarketSubsegmentValues = ["Education", "Industrial", "Healthcare", "Hospitality", "Office", "Public Space", "Residential", "Retail", "Other"]
    validStatusValues = ["Testing", "Closed", "New", "Pending"]
    validSpecPositionValues = ["Clipsal", "Lutron", "Encelium", "Wattstopper", "Cooper/Greengate",
                               "Encillium", "Unknown","Enlighted", "Hubbell", "LC&D", "Crestron",
                               "Acuity/nLight/Sensor Switch", "CP Electronics", "Douglas", "ETC",
                               "Other", "Leviton"]
    validSequenceOfOperationsValues = ["Unknown", "Wattstopper", "basic standalone switching",
                                       "Multi-floor linking", "None", "Emergency auto reporting",
                                       "Room based multiple zones", "Other"]
    validTenantIdValues = [0, 2]

    def CreateStringId(length):
        N = length
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        return str(ran)
