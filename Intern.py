class Intern():
    number_of_interns = 0

    def __init__(self,name):
        self.name = name

    def Name(self):
        print(self.name)

class CTO_Intern(Intern):
    def __init__(self,name):
        Intern.__init__(self,name)

Intern1 = CTO_Intern('Ammad')

print(CTO_Intern.Name(Intern1))

# Intern.name = 'Ammad'
# intern1 = Intern()
# intern2 = Intern("Mateen")
# intern1.Name()
# intern2.Name()
# No_of_instances = Intern.number_of_interns
# print(No_of_instances)
# print(intern2.name)
print(Intern1.__class__.__mro__)

