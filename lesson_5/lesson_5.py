from parents import Parents


grandma = Parents(name="Dasha", age=65, character='Nordic')
print(grandma.__dict__)
grandma.print_info()
print(grandma.age)
print("-"*20)
grandpa = Parents(name="Victor", age=70, character='Sanguine')
print(grandpa.__dict__)
grandpa.print_info()
