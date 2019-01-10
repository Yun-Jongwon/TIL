class Circle():
    pi=3.14
    x=0
    y=0
    r=0

    def area(self):
        return self.pi*self.r*self.r
    def circumference(self):
        return 2*self.pi*self.r
    def center(self):
        return(self.x,self.y)
    def move(self,x,y):
        self.x=x
        self.y=y
    
my_circle=Circle()
my_circle.x=2
my_circle.y=4
my_circle.r=3

print(my_circle.area())

print(my_circle.circumference())
