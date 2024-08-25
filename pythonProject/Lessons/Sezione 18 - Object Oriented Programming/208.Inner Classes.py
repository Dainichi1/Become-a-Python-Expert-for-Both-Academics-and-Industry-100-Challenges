

class Customer:

    def __init__(self, id, name, billingDoorNumber, billingStreet, billingCity, billingCountry, billingPin, shippingDoorNumber, shippingStreet, shippingCity, shippingCountry, shippingPin):
        self.custid = id
        self.name = name
        self.billingAddress = self.Address(billingDoorNumber, billingStreet, billingCity,billingCountry, billingPin)
        self.shippingAddress = self.Address(shippingDoorNumber, shippingStreet, shippingCity, shippingCountry, shippingPin)

    class Address:
        def __init__(self, doorNumber, street, city, country, pin):
            self.doorNumber = doorNumber
            self.street = street
            self.city = city
            self.country = country
            self.pin = pin

        def display(self):
            print(self.doorNumber)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)

c = Customer(10, 'John', 101,'abc', 'delhi', 'india',1001, 200, 'fssf','mumbai','india',4001)

c.billingAddress.display()
c.shippingAddress.display()