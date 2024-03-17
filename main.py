#Maru Puran
#October 12
#modify a function and add code to a program to understand more about how functions and subroutines work as well as how they're able to be used in a program


def origin_country(country): #changed function name from "my_function" to "origin_country"
  print("I am from " + country+ "!") #prints the words "I am from" and the country inputted into the parameter #I also changed and made it add an exclamation mark to the end because it is very happy :)


origin_country("Sweden") #changed argument "Brazil" to "Sweden"; will now output "I am from Sweden" instead of "I am from Brazil"


# # # # # # # # # # # # # 

#get the user to input a country and call the function with it as the parameter

user_country = input("\nHello! Please enter a country: ") #ask the user to enter a country, store it in a variable called user_country

origin_country(user_country) #call the function origin_country using the country the user has inputted