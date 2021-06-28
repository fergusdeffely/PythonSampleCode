
class Customer:

    # class-level variable (shared between all instances)
    next_id = 0

    def __init__(self, name):
        self.name = name

        self.id = Customer.next_id
        
        # update next_id at the class-level
        Customer.next_id = Customer.next_id + 1

    def __repr__(self):
        return f"Customer: id = {self.id}, name = {self.name}"


a = Customer("Alice")
b = Customer("Bob")
c = Customer("Charles")

print(a)
print(b)
print(c)
