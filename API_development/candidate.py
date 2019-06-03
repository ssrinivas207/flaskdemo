import uuid

class Candidate:
    __id = None
    __first_name = ""
    __last_name =""
    __experience = []

    def __init__(self, first_name, last_name, experience =[]):
        self.__id = uuid.uuid4()
        self.first_name=first_name
        self.last_name=last_name
        self.experience=experience

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self,value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
    
    @property
    def experience(self):
        return self.__experience
    
    @experience.setter
    def experience(self, value):
        self.__experience=value
    
    @property
    