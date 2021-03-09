import database

#database.add_one('Laura', 'Smith', 'laura@smith.com')


#   database.delete_one('6')

stuff = [
    ('Brenda', 'A', 'brenda@a.com'),
    ('Joshua', 'B', 'josh@b.com')
]
# database.add_many(stuff)
database.email_lookup('john@codemy.com')
#database.show_all()