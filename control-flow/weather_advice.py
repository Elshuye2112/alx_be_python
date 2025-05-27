# weather_advice.py

# Ask the user about the weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Provide clothing recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")


response= input("Are you satisfied? (yes/no)").strip().lower()

if response=="yes":
    print("Great I would say thank you. I have eaten the fruit!!!")

elif response=="no":
    print("Thank you for your dedicate attention. I will help you more")

else :
  print("Please select one to know your understanding")