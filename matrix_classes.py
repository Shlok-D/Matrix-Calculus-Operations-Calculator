import random
import numpy as np

class Matrix:
    def init(self):
       pass

    def input1(self): 
        f1 = int(input("Enter number of rows of matrix : "))
        f2 = int(input("Enter number of columns of matrix : "))
        x = [[]]
        for q in range(0,f1):
            for w in range(0,f2):
                x[q].append(int(input(f"Enter first matrix element ({q + 1},{w + 1}) : ")))
            if q < (f1 - 1):
                x.append([])
        return x
    
    def addition(self,x,y):
        a = [[]]
        print("Addition :", end=" ")
        for q1 in range(0,len(x)):
            for w1 in range(0,len(x[0])):
                a[q1].append(x[q1][w1] + y [q1][w1])
            if q1 < (len(x) - 1):
                a.append([])
        return a
    
    def subtraction(self,x,y):
        a = [[]]
        print("Subtraction :", end=" ")
        for q1 in range(0,len(x)):
            for w1 in range(0,len(x[0])):
                a[q1].append(x[q1][w1] - y [q1][w1])
            if q1 < (len(x) - 1):
                a.append([])
        return a

    def multiplication(self,x,y):
        m = [[]]
        print("Multiplication :", end=" ")
        for i in range(0,len(x)):
            for j in range(0,len(y[0])):
                c = 0
                for k in range(0,len(x[0])):
                    c += x[i][k]*y[k][j]
                m[i].append(c)
            if i < (len(x) - 1):
                m.append([])
        return m
    
    def determinant(self,l):
        if len(l) == len(l[0]):
            if len(l) == 1:
                return l[0][0]
            if len(l) == 2:
                return (l[0][0] * l[1][1] - l[0][1] * l[1][0])
            else:
                d = 0
                for a in range(0,len(l)):
                    d += ((-1) ** (a)) * (l[0][a]) * (self.determinant1(l, a))
                return d
    
    def determinant1(self,l, a):
        z = [[]]
        q = 0
        for i in range(0,len(l)):
            for j in range(0,len(l)):
                if i != 0 and j != a:
                    z[q].append(l[i][j])
            q += 1
            if i < (len(l) - 1):
                z.append([])
        z.remove([])
        return (self.determinant(z))

    def transpose(self,l):
        l1 = []
        for i in range(len(l)):
            l1.append([])
            for j in range(len(l)):
                l1[i].append(l[j][i])
        return l1

    def inverse(self,l):
        if len(l) == len(l[0]):
            if len(l) == 1:
                return round(l[0][0],5)
            if len(l) == 2:
                det = self.determinant(l)
                q = [[l[1][1]/det,-1*(l[0][1]/det)],[-1*(l[1][0]/det),l[0][0]/det]]
                q1 = self.transpose(q)
                q2 = self.round_matrix(q1)
                return q2
            else:
                d = []
                det1 = self.determinant(l)
                for b in range(0,len(l)):
                    d.append([])
                    for a in range(0,len(l)):
                        d[b].append((((-1) ** (a+b)) * (self.inverse1(l, a, b))))
                for i in range(len(l)):
                    for j in range(len(l)):
                        d[i][j] = d[i][j]/det1
                d1 = self.transpose(d)
                d2 = self.round_matrix(d1)
                return d2

    def inverse1(self, l, a, b):
        z = [[]]
        q = 0
        for i in range(0,len(l)):
            for j in range(0,len(l)):
                if i != b and j != a:
                    z[q].append(l[i][j])
            q += 1
            if i < (len(l) - 1):
                z.append([])
        z.remove([])
        return (self.determinant(z))

    def random(self,f1,f2):
        x = []
        for q in range(0,f1):
            for w in range(0,f2):
                x[q].append(random.randint(0,100))
            if q < (f1 - 1):
                x.append([])
    
    def power_off(self, l, n):
        z = l
        a = []
        if(n==0):
            for k in range(len(l)):
                a.append([])
                for m in range(len(l[0])):
                    a[k].append(1)
            return a
        for i in range(1,n):
            z = self.multiplication(z,l)
        return z

    def display(self,l):
        print(l)
    
    def operations(self):
        a = int(input("Enter Operation : (1-Add),(2-Mul),(3-Mul),(4-Determinant),(5-Inverse),(6-Transpose),(7-Power of) : "))
        b1 = self.input1()
        if a == 1 or a == 2 or a == 3:
            b2 = self.input1()
            if(a == 1 or a== 2):
                if(len(b1) == len(b2) and len(b1[0]) == len(b2[0])):
                    if(a == 1):
                        c1 = self.addition(b1,b2)
                        self.display(c1)
                    if(a == 2):
                        c2 = self.addition(b1,b2)
                        self.display(c2)
                else:
                    print("Error")
            if(a == 3):
                if(len(b1[0]) == len(b2)):
                    c3 = self.multiplication(b1,b2)
                    self.display(c3) 
                else:
                    print("Error M")

        if a == 4:
            d2 = self.determinant(b1)
            self.display(d2)

        if a == 5:
            d4 = self.inverse(b1)
            self.display(d4)
        
        if a == 6:
            d6 = self.transpose(b1)
            self.display(d6)
        
        if a == 7:
            n = int(input("Enter Power of Matrix you want to find : "))
            d7 = self.power_off(b1,n)
            self.display(d7)

    def round_matrix(self, b):
        for i in range(len(b)):
            for j in range(len(b[0])):
                b[i][j] = round(b[i][j],5)
        return b


class Polynomial:
    def __init__(self) -> None:
        pass

    def calculate(self,l):
        p = np.poly1d(l)
        a = []
        for i in p.roots:
            a.append(np.round(i,5))
        return a
    