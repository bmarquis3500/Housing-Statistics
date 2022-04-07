'''
This is a command line driven menu to provide information about given
phone number zip code and matrices
'''
#import statements
import sys
import pandas as pd
import matplotlib.pyplot as plt
#get housing data
housing = pd.read_csv('Housing.csv')
#get population data
population = pd.read_csv('PopChange.csv')
#welcome message
print('Welcome to the statistics application')
#infinite loop gets choice
while True:
    print('\nSelect the file you want to analyze:\n')
    print('1. Population Data')
    print('2. Housing Data')
    print('3. Exit the program')
    #get user choice, ensure proper input
    while True:
        try:
            choice = input('\n')
            if not choice in ('1', '2','3'):
                raise ValueError
        except ValueError:
            print('\nSorry incorrect input, try again. Type 1, 2, or 3')
            continue
        break
    #Population Data
    if choice == '1':
        #get population choice
        while True:
            print('\nYou have entered Population Data.\n')
            print('Select the column you want to analyze:\n')
            print('1. Pop Apr 1')
            print('2. Pop Jul 1')
            print('3. Change Pop')
            print('4. Exit Population')
            #get user choice, ensure proper input
            while True:
                try:
                    pop_choice = input('\n')
                    if not pop_choice in ('1', '2','3','4'):
                        raise ValueError
                except ValueError:
                    print('\nSorry incorrect input, try again. Type 1, 2, 3, or 4')
                    continue
                break
            #population april 1
            if pop_choice=='1':
                print('Count = ', end='')
                print(population[population.columns[0]].count())
                print('Mean = ', end='')
                print(population['Pop Apr 1'].mean())
                print('Standard Deviation = ', end='')
                print(population['Pop Apr 1'].std())
                print('Min = ', end='')
                print(population['Pop Apr 1'].min())
                print('Max = ', end='')
                print(population['Pop Apr 1'].max())
                plt.hist(population['Pop Apr 1'])
                plt.show()
            #population July 1
            if pop_choice=='2':
                print('Count = ', end='')
                print(population[population.columns[0]].count())
                print('Mean = ', end='')
                print(population['Pop Jul 1'].mean())
                print('Standard Deviation = ', end='')
                print(population['Pop Jul 1'].std())
                print('Min = ', end='')
                print(population['Pop Jul 1'].min())
                print('Max = ', end='')
                print(population['Pop Jul 1'].max())
                plt.hist(population['Pop Jul 1'])
                plt.show()
            #population change
            if pop_choice=='3':
                print('Count = ', end='')
                print(population[population.columns[0]].count())
                print('Mean = ', end='')
                print(population['Change Pop'].mean())
                print('Standard Deviation = ', end='')
                print(population['Change Pop'].std())
                print('Min = ', end='')
                print(population['Change Pop'].min())
                print('Max = ', end='')
                print(population['Change Pop'].max())
                plt.hist(population['Change Pop'])
                plt.show()
            #exit
            if pop_choice=='4':
                break
    #Housing Data
    if choice == '2':
        #get housing choice
        while True:
            print('\nYou have entered Housing Data.\n')
            print('Select the column you want to analyze:\n')
            print('1. Age')
            print('2. Bedrooms')
            print('3. Built')
            print('4. Rooms')
            print('5. Utility')
            print('6. Exit Housing')
            #get user choice, ensure proper input
            while True:
                try:
                    house_choice = input('\n')
                    if not choice in ('1', '2','3','4','5','6'):
                        raise ValueError
                except ValueError:
                    print('\nSorry incorrect input, try again. Type 1, 2, 3, 4, 5, or 6')
                    continue
                break
            #Age
            if house_choice=='1':
                print('Count = ', end='')
                print(housing[housing.columns[0]].count())
                print('Mean = ', end='')
                print(housing['AGE'].mean())
                print('Standard Deviation = ', end='')
                print(housing['AGE'].std())
                print('Min = ', end='')
                print(housing['AGE'].min())
                print('Max = ', end='')
                print(housing['AGE'].max())
                plt.hist(housing['AGE'])
                plt.show()
            #Bedrooms
            if house_choice=='2':
                print('Count = ', end='')
                print(housing[housing.columns[0]].count())
                print('Mean = ', end='')
                print(housing['BEDRMS'].mean())
                print('Standard Deviation = ', end='')
                print(housing['BEDRMS'].std())
                print('Min = ', end='')
                print(housing['BEDRMS'].min())
                print('Max = ', end='')
                print(housing['BEDRMS'].max())
                plt.hist(housing['BEDRMS'], bins = housing['BEDRMS'].max())
                plt.show()
            #Year built
            if house_choice=='3':
                print('Count = ', end='')
                print(housing[housing.columns[0]].count())
                print('Mean = ', end='')
                print(housing['BUILT'].mean())
                print('Standard Deviation = ', end='')
                print(housing['BUILT'].std())
                print('Min = ', end='')
                print(housing['BUILT'].min())
                print('Max = ', end='')
                print(housing['BUILT'].max())
                plt.hist(housing['BUILT'])
                plt.show()
            #Rooms
            if house_choice=='4':
                print('Count = ', end='')
                print(housing[housing.columns[0]].count())
                print('Mean = ', end='')
                print(housing['ROOMS'].mean())
                print('Standard Deviation = ', end='')
                print(housing['ROOMS'].std())
                print('Min = ', end='')
                print(housing['ROOMS'].min())
                print('Max = ', end='')
                print(housing['ROOMS'].max())
                plt.hist(housing['ROOMS'], bins = housing['ROOMS'].max()-1)
                plt.show()
            #utilities
            if house_choice=='5':
                print('Count = ', end='')
                print(housing[housing.columns[0]].count())
                print('Mean = ', end='')
                print(housing['UTILITY'].mean())
                print('Standard Deviation = ', end='')
                print(housing['UTILITY'].std())
                print('Min = ', end='')
                print(housing['UTILITY'].min())
                print('Max = ', end='')
                print(housing['UTILITY'].max())
                plt.hist(housing['UTILITY'])
                plt.show()
            #exit
            if house_choice=='6':
                break
    #Exit program
    if choice == '3':
        print('Thank you, goodbye!')
        sys.exit(0)
