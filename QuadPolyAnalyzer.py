a = int(input('Enter value of A '))
b = int(input('Enter value of B '))
c = int(input('Enter value of C '))
d = int((b**2) - 4*a*c)

if (d > 0):
    roots = "Roots are real and distinct"
elif(d < 0):
    roots = "Roots are imaginary, and form a conjugate pair"
else:
    roots = "Roots are real and repeated"

if a > 0 :
    parabola = "Parabola opens upward"
else:
    parabola = "Parabola opens downward"

if (d >= 0):
    roots_val = ((d**0.5) - b )/2*a , -((d**0.5) + b )/2*a
else:
    roots_val = ('Roots are imaginary.')


print()
print(f'Quadriatic polynomial : {a}x^2 + {b}x + {c}')
print('Analysing...')
print(roots)
print(parabola)
print('Roots are: ' , roots_val)
print('Analysis Complete.')
