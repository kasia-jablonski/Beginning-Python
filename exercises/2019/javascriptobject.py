class JavaScriptObject(dict):
    def __getattribute__(self, item):           
        try:
            return self[item]
        except KeyError:            # if key doesn't exist
            return super().__getattribute__(item)

jso = JavaScriptObject({'name': 'Kenneth'})
jso.language = 'Python'
jso.name            # returns 'Kanneth'
jso.language        # returns 'Python'
#jso.fake            # returns AttributeError