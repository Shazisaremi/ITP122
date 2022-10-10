speed=int(input('Enter speed'))
if speed <= 70:
	print('Ok')
elif speed >= 70:
	points = (speed - 70) // 5
	print('points = {}'.format(points))
	if points >= 12:
		print('License suspended')