#!/usr/bin/python3
""" City class that inherits from BaseModel"""

BaseModel = models.base_model.BaseModel


class City(BaseModel):
    """City class
    Attributes:
        state_id (str): state identifier
        name (str): name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, state_id=None, name=None):
        self.state_id = state_id
        self.name = name

    @property
    def state(self):
        return (self.name + '(' + self.state_id + ')')