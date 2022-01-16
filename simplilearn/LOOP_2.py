rows=int(input("Enter number of rows"))
colomns=int(input("Enter number of colomns"))
x=[]
val=[]
for i in range(0,rows): #-> Vamos inserir um range, um indica que começa com 0
    for j in range(0,colomns):
        val.insert(j,int(input("Enter the %d * %d element" %(i,j))))#-> Tem que adicionar um int para guardar como número
    x.insert(i,val)
    val=[]

y=[]
for i in range(0,rows):
    for j in range(0,colomns):
        val.insert(j,int(input("Enter the %d * %d element" %(i,j)))) #-> Tem que adicionar um int para guardar como número
    y.insert(i,val)
    val=[]
sum=[]

for i in range(0,rows):
    for j in range(0,colomns):
        val.insert(j, x[i][j]+y[i][j])
    sum.insert(i,val)
    val=[]
print(sum)