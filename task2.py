from math import pi
a = int(input("Введите угол в радианах: "))
while a<0 or a>2*pi:
  a = int(input("Значение угла лежит в пределах от 0 до 2*pi.\nВведите значение угла в радианах заново: "))
print("Значение угла в градусах: "+str(a*180/pi))