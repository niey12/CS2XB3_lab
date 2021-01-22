def are_valid_groups(students, groups):
	for i in students:
		for j in groups:
			if i in j:
				break
			if j == groups[-1]:
				return False
		if i == students[-1]:
			return True
	return False 
