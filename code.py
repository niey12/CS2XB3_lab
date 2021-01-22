def are_valid_groups(litsOfStudent, listOfGroup):
    for i in litsOfStudent:
        for j in listOfGroup:
            if i in j:
                break
        print ("True") 
