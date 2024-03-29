class Person:
    def __eq__(self,person):
        """Override for ==
        
        Arguments:
            person {Person} -- The the object being compared with
        
        Returns:
            bool -- If person == self
        """
        return self.guid.lower() == person.guid.lower()
    def __init__(self,guid,name,deleted=False):
        self.guid = guid
        self.name = name
        self.deleted = deleted
    
    @classmethod
    def from_json(self,json,**kwargs):
        if json == None:
            return Person.none()
        person_json = json.copy()
        for key in kwargs:
            person_json[key] = kwargs[key] # Allows to override
        return Person(
            guid=person_json["guid"],
            name=person_json["name"],
            deleted=person_json.get("deleted",False)
        )

    
    @classmethod
    def none(self):
        return Person(None,None,None)