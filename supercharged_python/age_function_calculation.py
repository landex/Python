# Function to calculate the age of person
def age():
    # The variables that function use
    age = int(input( 'Enter your age: '))
    name = input( 'Enter you name: ')

    # The Stantement to verify the age
    if age < 30:
        print (' Hello ' , name)
        print (' I see you are less than 30. ')
        print (' You are so young. ')
    else:
        print (' Hello ' , name)
        print (' I see you are more than 30. ')
        print (' You are so old. ')
