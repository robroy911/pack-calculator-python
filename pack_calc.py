#Programming Merit Badge Python Program

print('Welcome to Pack Weight Calculator!')

userName = input('To begin, what is you name?')

userWeight = input('Ok ' + userName + ', how much do you weigh?')

print('Choose your build type:')
print('------------------------')
print('Skinny')
print('Average')
print('Athletic')
print('Large')


userBuild = input('Choose your build type:')

print( userName + ' weighs ' + userWeight + ' Lbs and has a ' + userBuild + ' build.')


if userBuild == 'Skinny':

	packWeightLow = int(userWeight) * .17
	packWeightHigh = int(userWeight) * .20
	print(userName + ', your pack should between '+ str(packWeightLow) + ' and '+ str(packWeightHigh))

elif userBuild == 'Average':

	packWeightLow = int(userWeight) * .19
	packWeightHigh = int(userWeight) * .23
	print(userName + ', your pack should between '+ str(packWeightLow) + ' and '+ str(packWeightHigh))

elif userBuild == 'Athletic':

	packWeightLow = int(userWeight) * .25
	packWeightHigh = int(userWeight) * .30
	print(userName + ', your pack should between '+ str(packWeightLow) + ' and '+ str(packWeightHigh))


elif userBuild == 'Large':

	packWeightLow = int(userWeight) * .20
	packWeightHigh = int(userWeight) * .25
	print(userName + ', your pack should between '+ str(packWeightLow) + ' and '+ str(packWeightHigh))

else: 

	print('Invalid build type entry!')
	


