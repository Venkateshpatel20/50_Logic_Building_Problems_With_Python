class myclass():
    def table_printer(n):
        for i in range(1,11):
            print("%d * %d = %d" %(n,i,n*i))
myclass.table_printer(5)
print("--------------")
myclass.table_printer(7)
print("--------------")
myclass.table_printer(12)
