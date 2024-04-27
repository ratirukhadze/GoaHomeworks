Score = int(input('Enter your Score: '))

if Score >= 90 <= 100:
    print('შენ სწავლა დაგიფინანსდება სრულიად')

elif Score >= 70 <= 80:
    print('შენ სწავლა დაგიფინანდება 1500 ლარით')

elif Score >= 40 <= 70:
    print('თქვენ სწავლა დაგიფინანსდება 500 ლარით')

elif Score <= 40:
    print('თქვენ სწავლა არ დაგიფინანსდებათ')