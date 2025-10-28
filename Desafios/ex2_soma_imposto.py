
def somaImposto(taxaImposto, custo):
    return(1 + taxaImposto/100)*custo
a = float(input("digite a taxa de imposto: "))
b=float(input("digite o custo: "))
print("valor com imposto:",somaImposto(a,b))
    

