def borsh(volume, *toppings): #if I will add regular parameter for regular argument
    # the arbitrary pararameter should be placed last like def sss(sdds, sdds, *dssdd)
    # so it's for LISTS - arbitrary with 1 asteriks
    print(f"Making a {volume} borsh with: ")
    for topping in toppings:
        print(topping)