class VersionModel:
    def __init__(self, stage, alternate, revision, name, notes, isPrimary, isActive):
        self.Stage = stage
        self.Alternate = alternate
        self.Revision = revision
        self.Name = name
        self.Notes = notes
        self.IsPrimary = isPrimary
        self.IsActive = isActive

    validAlternateValues = ["Alt A", "Alt T", "Alt C", "Alt H", "Alt P", "Alt Z", "Alt Y",
                            "Alt Q", "Alt X", "Alt K", "Alt D", "Alt E", "Base", "Alt B", None]