#List of employee objects
class Product:
    def __init__(self, pid, pname,price,  mname):
        self.pid = pid
        self.pname = pname
        self.price=price
        self.mname=mname
        print("This is Product constructor")

    def met(self):
        print("This is met in Product class"+str(self.pid)+" "+str(self.pname)+" "+str(self.price)+" "+str(self.mname))

    def __hash__(self):
        return hash((self.pid, self.pname,self.price,self.mname))

    def __eq__(self, obj):
        return isinstance(obj, Product) and obj.pid == self.pid and obj.pname==self.pname and obj.price==self.price and obj.mname==self.mname

    def __ne__(self, other):
        return not self == obj


# creating list
list1 = []

# appending instances to list
list1.append( Product(1,"Product 1",5000,"M1") )
list1.append( Product(2,"Product 2",2000,"M2") )
list1.append( Product(3,"Product 3",3000,"M3") )
list1.append( Product(4,"Product 4",4000,"M4") )

#sorting the products based on price
list1.sort(key=lambda x: x.price,reverse=True)

#list1 after sorting but before extending
for obj in list1:
    print(obj.pid,obj.pname,obj.price,obj.mname)
    
    
list2=[Product(5,"Product 5",600,"M5"),Product(6,"Product 6",700,"M6")]
list1.extend(list2)
#printing the list of products
for obj in list1:
    print(obj.pid,obj.pname,obj.price,obj.mname)