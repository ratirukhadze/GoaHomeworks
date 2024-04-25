import json
x = {
    "name": "Rati",
    "age": 11,
    "married": False,
    "divorced": False,
    "children": False,
    "pets": "cat",
    "cars": [
        {"model": "FIAT BRAVA", "mpg": 27.5}#my parents car
 ]
}


#convert into JSON:
y = json.dumps(x)

# შედეგი არის JSON სტრიქონი:
print(y)

#გამოიყენე. და სივრცე ობიექტების განცალკევებისთვის, და სივრცე, a = და სივრცე გასაღებების მათი მნიშვნელობებისგან გამოსაყოფად:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

    
