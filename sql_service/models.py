

class SqlParseRequest:
    query = ''


class SqlParseResponse:
    query = ''
    parameters = []

    def serialize(self):
        ser_params = []
        for p in self.parameters:
            ser_params.append(p.serialize())
        return {
            'query':self.query,
            'parameters':ser_params
        }


class Parameter:
    name = ''
    value = ''

    def __init__(self,name,value):
        self.name = name
        self.value = value

    def serialize(self):
        return {
            'name': self.name,
            'value':self.value
        }
