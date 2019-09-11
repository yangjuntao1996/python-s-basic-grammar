#4-10

piazas = ['1','2','3','4','5']
print('The first time items in the list are:' + str(piazas[:3]))
print('Three items from the middle of the list are:' + str(piazas[1:4]))
print('The last three items in the list are:' + str(piazas[2:5]))

#4-11

piazas = ['1','2','3','4','5']
friend_piazas = piazas[:]
piazas.append('6')
friend_piazas.append('7')
print('My favorite pizzas are:'+str(piazas))
print("My friend's favorite pizzas are:" + str(friend_piazas))
for friend_piaza in friend_piazas:
	print(friend_piaza)


#4-12

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

for my_food in my_foods:
	print(my_food)
for friend_food in friend_foods:
	print(friend_food)
