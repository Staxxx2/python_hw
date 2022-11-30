# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"


x = [True, False]
y = [True, False]
z = [True, False]

for a in x:
    for b in y:
        for c in z:
            print(a, b, c)
            r1 = not (a or b or c)
            r2 = (not a) and (not b) and (not c) 
            print(r1 == r2)
