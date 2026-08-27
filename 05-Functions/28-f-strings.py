# f-strings in Python #

letter = "Hey my name is {} and I am from {}"              
country = "India"
name = "Devil"

print(letter.format(name, country))                        # simple
print(f"Hey my name is {name} and I am from {country}")    # f-string

print(letter.format(name, country))                        
print(f"We use f-strings like this: Hey my name is {name} and I am from {country}")

print(letter.format(name, country))                        
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

txt = "For only {price:.2f} dollars!"                      # simple
print(txt.format(price = 49.0999))

price = 49.0999                                            # f-string
txt = f"For only {price:.2f} dollars!"
print(txt)

print(f"{2 * 30}")
print(type(f"{2 * 30}"))