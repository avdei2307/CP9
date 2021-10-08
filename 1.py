x = 0
y = 0
z = 0
def pr(a,b,c):
    if (a < b + c) and (b < c + a) and (c < b + a):
      print('Треугольник существует')
      return True
    else:
      print('Треугольник не существует')
      return False
def pr2(a,b,c):
        if (a**2 == c**2 + b**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
            print('он прямоугольный')
        else:
            print('он не прямоугольный')
try:
  print('Введите первую сторону')
  x = int(input())
  if x <= 0:
      raise ValueError
  print('Введите вторую сторону')
  y = int(input())
  if y <= 0:
      raise ValueError
  print('Введите третью сторону')
  z = int(input())
  if z <= 0:
      raise ValueError
except ValueError:
  print('Ошибка! Стороны могут принимать только положительные численные значения!')
else:
    if pr(x,y,z):
        pr2(x,y,z)
    

