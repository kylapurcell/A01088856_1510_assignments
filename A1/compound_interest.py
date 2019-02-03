
def compound_interest(principal, annual_interest, number_per_year, years):
    """
     Calculate the compound interest

     PARAM: principal, a float
     PARAM: annual_interest, a float
     PARAM: number_per_year, an integer
     PARAM: years, an integer
     PRE-CONDITION: principal must be a float
     PRE-CONDITION: annual_interest must be a float
     PRE-CONDITION: number_per_year must be an integer and > 0
     PRE-CONDITION: years must be an integer
     POST-CONDITION: calculates the compound interest
     RETURN: the compound interest as a float

     >>> compound_interest(0.0 , 0.0, 1, 0)
     0.0
     >>> compound_interest(4.5, 0.7, 3, 7)
     368.0462271001469

     """
    interest = principal*(1 + annual_interest/number_per_year)**(number_per_year*years)
    return interest


def main():
    """
    Drive the program
    """
    import doctest
    doctest.testmod()
    print(compound_interest(4.2, 1.36, 3, 9))


if __name__ == '__main__':
    main()


