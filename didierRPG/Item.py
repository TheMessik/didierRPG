class Item:
    def __init__(self, name: str, requirements: dict, type_of_item: str):
        # sanity checks
        assert isinstance(name, str), "name must be a string. We're not Nazis, we use strings for names"
        assert isinstance(requirements, dict), "requirements must be a dict. No requirements? So a baby can wear it?"
        assert isinstance(type_of_item, str), "type_of_item must be string. Can't use a number, can I?"

        assert type_of_item in ("helmet", "chestplate", "pants", "hand", "spell", "consumable"), \
            "unrecognized type of item"

        self.name = name
        self.requirements = requirements
        self.type_of_item = type_of_item

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
