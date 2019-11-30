#___Functions___
def heading():
  print("\n________________________________________________________________ \n\n               Billy The Cat. Made by Muhfasul A.\n________________________________________________________________ \n" )
def greeting():
  print ("\nBilly: Meeooow.")
  print ("Billy: I'm cat. I'm hungry.")
  print ("Billy: Give me food")
  print ("\n      *Billy likes fish*     ")
def farewell():
  print('\nBilly:')
  print('')
  print('  _  ,/|')
  print(" '\`o.O' ")
  print('  =(_ _)=')
  print('    |U|')
  print('   /  |     ** Hav a great day and thanks fur the fish **')
  print('  //|  \ ')
def eating():
  print ("\n      *nom nom nom*   ")
  print ("\nBilly: Now you may talk.")

#___Variables___
greetings = ("hello", "hi", "what's up", "hey", "hola", "sup", "yo", "what's up", "sup bro", "whats good", "yerrr", "hiii", "meow")
farewell = ("bye","see ya")
foods = ("fish", "milk", "wetfood", "water")

#___chat begins___
heading()
print("   *Type Something*  ")
chat = 0
x = 0
while not chat in farewell:
  chat = input("\n You: ")
  chat = chat.lower()

  if chat in greetings:
    greeting()

  elif chat in foods:
    x =  x + 1
    if (0<x<2):
      eating()
    elif (1<x<3):
      print("\nBilly: Fuck yeah")
    elif (x==3 or 3<x<9):
      print("\nBilly: God bless you.")
    else:
      print("\nBilly: ...ok. Stop now. >:(")

print ("bye")
print (x)