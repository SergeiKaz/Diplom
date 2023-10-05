class Tour:
    def __init__(self,name,street,price,date):
        name = name
        street = street
        price = price
        date = date
    def __repr__(self):
        return '<Tour %r>'% self.name