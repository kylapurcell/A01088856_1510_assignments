
def compound_interest(principal, annual_interest, number_per_year, years):
    """
     Calculate the compound interest

     PARAM: principal, a float
     PARAM: annual_interest, a float
     PARAM: number_per_year, an integer
     PARAM: years, an integer
     PRE-CONDITION: principal must be a float
     PRE-CONDITION: annual_interest must be a float
     PRE-CONDITION: number_per_year must be an integer
     PRE-CONDITION: years must be an integer
     POST-CONDITION: calculates the compound interest
     RETURN: the compound interest as a float
     """
    interest = principal*(1 + annual_interest/number_per_year)**(number_per_year*years)
    return interest


def main():
    """
    Drive the program
    """
    print(compound_interest(4.2, 1.36, 3, 9))


if __name__ == '__main__':
    main()


