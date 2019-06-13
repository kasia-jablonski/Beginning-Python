class ReversedStr(str):
    def __new__(*args, **kwargs):           # new is used for immutable objects; new doesn't use self in arguments
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self

