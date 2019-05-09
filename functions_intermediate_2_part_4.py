def printInfo(some_dict):
    locationcount = len(dojo['locations'])
    instructorcount = len(dojo['instructors'])

    print(locationcount , 'LOCATIONS')
    for x in range(len(dojo['locations'])):
        print(dojo['locations'][x])

    print()

    print(instructorcount , 'INSTRUCTORS')
    for i in range(len(dojo['instructors'])):
        print(dojo['instructors'][i])
    
    
   


   

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)