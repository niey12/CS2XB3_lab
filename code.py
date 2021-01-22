def are_valid_groups(students, groups):
	l = []
	a=0
	for i in students:
		a+=1
		if i in l:
			return False
		else:
			l.append(i)
			for j in groups:
				if len(j) == 2 or len(j) == 3:
					if i in j:
						break
					if j == groups[-1]:
						return False
				else:
					return False
		if len(students) == a:
			return True
	return False 