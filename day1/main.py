#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

print("Welcome to the band name generator.")

city_name = input("what's the name of city you grew up in? \n")
pet_name = input("What is your pet name? \n")
band_name = city_name + " " + pet_name

print("Your band name could be " + band_name)