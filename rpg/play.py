from thieves import Thief

kenneth = Thief(name="Kenneth", sneaky=False)
print(kenneth.sneaky)
print(kenneth.agile)
print(kenneth.hide(8))

# isinstance('a', str)   -> True
# isinstance(5.2, (str, bool, dict))    -> False

# issubclass(bool, int)    -> True
# issubclass(str, int)    -> False
# issubclass(Thief, Character)    -> True

type(kenneth)       # returns <class 'thieves.Thief'>
kenneth.__class__       # returns <class 'thieves.Thief'>
kenneth.__class__.__name__      # returns 'Thief'