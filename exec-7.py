7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.



print("Escreva sua idade")
Age=int(input("Idade :"))

print("Idade expressa em dias")
print("{}".format(Age*365))

print("Idade expressa em meses")
print("{}".format(Age*12))

print("idade expresa em anos")
print("{}".format(Age*1))
