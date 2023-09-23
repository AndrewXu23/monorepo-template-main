import json

class MyClass:
    def __init__(self, attribute):
        self.attribute = attribute

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MyClass):
            return {"type": "MyClass", "attribute": obj.attribute}
        elif isinstance(obj, complex):
            return {"type": "complex", "real": obj.real, "imag": obj.imag}
        elif isinstance(obj, range):
            return {"type": "range", "start": obj.start, "stop": obj.stop, "step": obj.step}
        return super().default(obj)

class CustomJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if "type" in dct:
            if dct["type"] == "MyClass":
                return MyClass(dct["attribute"])
            elif dct["type"] == "complex":
                return complex(dct["real"], dct["imag"])
            elif dct["type"] == "range":
                return range(dct["start"], dct["stop"], dct["step"])
        return dct

def dumps(obj, *args, **kwargs):
    return json.dumps(obj, cls=CustomJSONEncoder, *args, **kwargs)

def loads(s, *args, **kwargs):
    return json.loads(s, cls=CustomJSONDecoder, *args, **kwargs)
