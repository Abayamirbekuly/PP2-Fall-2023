Task1
# Эта программа считывает два числа и выводит их сумму:
a = int(input())
b = int(input())
c=int(input())
print(a + b+c)

2
b = int(input())
h=int(input())
s=0.5*b*h
print(s)
# Выводите результат через print()
3
n =int(input())
k=int(input())
print(k//n)
print(k%n)
4
n=int(input())
h=(n//60)%24
m=(n%60)
print(h, m)
5
n=str(input())
print('Hello, '+ n+'!')
6
n=int(input())
m=n+1
z=n-1
print('The next number for the number '+str(n)+' is '+str(m)+'.')
print('The previous number for the number '+str(n)+' is '+str(z)+'.')
7
import math
a=int(input("цифр:"))
b=int(input("цифр:"))
c=int(input("цифр:"))
print(a//2+b//2+c//2+a%2+b%2+c%2)
8
a = int(input("Введите расстояние между рядами дырочек (a): "))
b = int(input("Введите расстояние между дырочками в ряду (b): "))
l = int(input("Введите длину свободного конца шнурка (l): "))
N = int(input("Введите количество дырочек в каждом ряду (N): "))

length=(((N*2)-1)*a)+(((N-1)*b)*2)+(2*l)
print( length)
