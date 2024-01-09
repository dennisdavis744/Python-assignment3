class person:
    def init(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def updation(self,name=None,age=None,address=None):
        if name:
            self.name=name
        if age:
            self.age=age
        if address:
            self.address=address
    def display(self):
        print('Name :',self.name)
        print('Age :',self.age)
        print('Address :',self.address)
person1=person(name='John Doe',age=23,address='300-b Wimbelton street')
print('Intial Information :')
person1.display()
person1.updation(age=24,address='125-c Manhaten')
print('\nUpdated Information :')
person1.display()