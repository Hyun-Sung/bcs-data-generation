class VersionModel:
    def __init__(self, stage, alternate, revision, name, notes, isPrimary, isActive):
        self.Stage = stage
        self.Alternate = alternate
        self.Revision = revision
        self.Name = name
        self.Notes = notes
        self.IsPrimary = isPrimary
        self.IsActive = isActive