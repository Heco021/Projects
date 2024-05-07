import json
with open("games.json", "r") as file:
	positions = json.loads(file.read())

oWin = 0

for position1, list1 in positions.items():
	state1 = []
	for position2, list2 in list1[1].items():
		state2 = []
		for position3, list3 in list2[1].items():
			state3 = []
			for position4, list4 in list3[1].items():
				state4 = []
				for position5, list5 in list4[1].items():
					if list5[1] == None:
						state4.append(1)
						continue
					state5 = []
					for position6, list6 in list5[1].items():
						if list6[1] == None:
							state5.append(-1)
							continue
						state6 = []
						for position7, list7 in list6[1].items():
							if list7[1] == None:
								state6.append(1)
								continue
							state7 = []
							for position8, list8 in list7[1].items():
								if list8[1] == None:
									state7.append(-1)
									continue
								state8 = []
								for position9, list9 in list8[1].items():
									state8.append(list9[0])
								if 1 in state8:
									positions[position1][1][position2][1][position3][1][position4][1][position5][1][position6][1][position7][1][position8][0] = 1
									state7.append(1)
								elif 0 in state8:
									positions[position1][1][position2][1][position3][1][position4][1][position5][1][position6][1][position7][1][position8][0] = 0
									state7.append(0)
								elif -1 in state8:
									positions[position1][1][position2][1][position3][1][position4][1][position5][1][position6][1][position7][1][position8][0] = -1
									state7.append(-1)
							if -1 in state7:
								positions[position1][1][position2][1][position3][1][position4][1][position5][1][position6][1][position7][0] = -1
								state6.append(-1)
							elif 0 in state7:
								positions[position1][1][position2][1][position3][1][position4][1][position5][1][position6][1][position7][0] = 0
								state6.append(0)
							elif 1 in state7:
								positions[position1][1][position2][1][position3][1][position4][1][position5][1][position6][1][position7][0] = 1
								state6.append(1)
						if 1 in state6:
							positions[position1][1][position2][1][position3][1][position4][1][position5][1][position6][0] = 1
							state5.append(1)
						elif 0 in state6:
							positions[position1][1][position2][1][position3][1][position4][1][position5][1][position6][0] = 0
							state5.append(0)
						elif -1 in state6:
							positions[position1][1][position2][1][position3][1][position4][1][position5][1][position6][0] = -1
							state5.append(-1)
					if -1 in state5:
						positions[position1][1][position2][1][position3][1][position4][1][position5][0] = -1
						state4.append(-1)
					elif 0 in state5:
						positions[position1][1][position2][1][position3][1][position4][1][position5][0] = 0
						state4.append(0)
					elif 1 in state5:
						positions[position1][1][position2][1][position3][1][position4][1][position5][0] = 1
						state4.append(1)
				if 1 in state4:
					positions[position1][1][position2][1][position3][1][position4][0] = 1
					state3.append(1)
				elif 0 in state4:
					positions[position1][1][position2][1][position3][1][position4][0] = 0
					state3.append(0)
				elif -1 in state4:
					positions[position1][1][position2][1][position3][1][position4][0] = -1
					state3.append(-1)
			if -1 in state3:
				positions[position1][1][position2][1][position3][0] = -1
				state2.append(-1)
			elif 0 in state3:
				positions[position1][1][position2][1][position3][0] = 0
				state2.append(0)
			elif 1 in state3:
				positions[position1][1][position2][1][position3][0] = 1
				state2.append(1)
		if 1 in state2:
			positions[position1][1][position2][0] = 1
			state1.append(1)
		elif 0 in state2:
			positions[position1][1][position2][0] = 0
			state1.append(0)
		elif -1 in state2:
			positions[position1][1][position2][0] = -1
			state1.append(-1)
	if -1 in state1:
		positions[position1][0] = -1
	elif 0 in state1:
		positions[position1][0] = 0
	elif 1 in state1:
		positions[position1][0] = 1
	print(positions[position1][0])
js = json.dumps(positions)
with open("games.json", "w") as file:
	file.write(js)