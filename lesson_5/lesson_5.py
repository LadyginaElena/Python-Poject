from parents import Parents
from children import Children
from grandchildren import Grandchildren

grandma = Parents(name="Dasha", age=65, character='Nordic')
print(grandma.__dict__)
grandma.print_info()
print(grandma.age)
print("-"*20)
grandpa = Parents(name="Victor", age=70, character='Sanguine')
print(grandpa.__dict__)
print(grandpa.name)
grandpa.print_info()
print("-"*20)
mother = Children(name='Angela', age=38, character='Phlegmatic person')
print(mother.__dict__)
print("-"*20)
sun = Grandchildren(name='Stepa', age=5, character='Cheerful')
sun.print_info()
