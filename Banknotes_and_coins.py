notes=[100, 50, 20, 10, 5, 2]
coins=[1, 0.50, 0.25, 0.10, 0.05,0.01]
amount=float(input())
print("NOTAS:")
if amount>=0 and amount<= 1000000.00:
    for i in notes:
        if amount>=i:
            x=int(amount//i)
            amount=amount-(i*x)
            print("{} nota(s) de R$ {:.2f}".format(int(x),i))
        else:    
            print("0 nota(s) de R$ {:.2f}".format(i))
print("MOEDAS:")
for j in coins:
        if amount>=j:
            y=int(amount//j)
            amount=round(amount-(j*y),4)
            
            print("{} moeda(s) de R$ {:.2f}".format(int(y),j))
        else:    
            print("0 moeda(s) de R$ {:.2f}".format(j))
        
