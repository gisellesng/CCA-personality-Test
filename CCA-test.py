print("Title of program: CCA Matching Personality test")
print()
print("Welcome to DHS! Please answer the following questions truthfully and we'll suggest a CCA for you!")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

sports1 = input("I love being outdoors, and do not like it indoors at all.")

outdoor1 = input("I am pysically strong, and have a interest in sports")

music1 = input("I can see colours in my mind when i hear music, and feel very energised.")

sports2 = input("I like to sweat")

outdoor2 = input("I like the sun!!!")

music2 = input("I play a musical instrument well, and like it a lot.")

sports3 = ("I like to exercise.")

outdoor3 = ("I like nature.")

music3 = ("I like music.")

sports_final = int(sports1) + int(sports2) + int(sport3)
outdoor_final = int(outdoor1) + int(outdoor2) + int(outdoor3)
music_final = int(music1)+ int(music2) + int(music3)

print()

if sports_final > outdoor_final and sports_final > music_final:
  print("You might be suitable for Sports club!")
elif outdoor_final > music_final:
  print("You might be stuiable for ODAC!")
else:
  print("You might be suitable for Band!")
