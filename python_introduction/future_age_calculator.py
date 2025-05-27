#future_age_calculator.py

from datetime import datetime
current_age=int(input("How old are you now?"))


years_to_add=2050-datetime.now().year

calculated_age=current_age+years_to_add

print(f"In 2050, you are {calculated_age} years old ")