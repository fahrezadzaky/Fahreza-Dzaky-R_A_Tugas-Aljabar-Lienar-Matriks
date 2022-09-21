from locale import MON_2
import matrix as mat

def mulmatl (m,a):
    row = len(m)
    col = len(m[0])

    m2 = mat.newmat (row,col)
     for r in range (row) :
         for c in range (col) :
             m2 [r] [c] = m[r] [c] * a
    return m2 
    
m1 = [
    [1,2,3],
    [4,5,6],
    [77,8,9]
]
a=2
m2 = mulmatl(m1, a)

print ("m1 :")
mat.printmat(m1)
print("a:")
print("m2 * m1 . a:")
mat.printmat(m2)