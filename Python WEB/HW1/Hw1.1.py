from abc import ABC, abstractmethod
import pickle
import json


class SerializationInterface(ABC):

    @abstractmethod
    def dump(self, data, name):
        pass

    @abstractmethod
    def load(self, name):
        pass


class JSONSerialization(SerializationInterface):

    def dump(self, data, name):
        with open(name, "w") as f:
            json.dump(data, f)

    def load(self, name):
        with open(name, "r") as f:
            data = json.load(f)
        return data


class BINSerialization(SerializationInterface):

    def dump(self, data, name):
        with open(name, "wb") as f:
            pickle.dump(data, f)

    def load(self, name):
        with open(name, "rb") as f:
            data = pickle.load(f)
        return data


bindoc = BINSerialization()
data_doc = [25, 25, 22, 25]
bindoc.dump(data_doc, "testbin")
print(bindoc.load("testbin"))
jsondoc = JSONSerialization()
jsondoc.dump(data_doc, "testjson")
print(jsondoc.load("testjson"))
