# WAP to create a class for employee having member data: empid, name, basic_py, ta, da, gros_py and member function, disp(), calc() using parametrical constructor to input the simple data. calc() to find gross py = basic_py + 10% of ta + 40% of da. disp() to display the information implement destructor to releasing memory once use is over. Input an employee details & print.

class employee:
    def __init__(self, empid, name, basic_py):
        self.e = empid
        self.n = name
        self.bp = basic_py
        self.t = 0
        self.d = 0
        self.gp = 0

    def calc(self):
        self.gp = self.bp + 0.1 * self.bp + 0.4 * self.bp

    def disp(self):
        print("The gross py", self.gp)

emp1 = employee(285, "soubhagya", 35000)
emp1.calc()
emp1.disp()