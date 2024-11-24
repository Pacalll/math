def compound_interest(annual_saving_rate, interest, years):
    """
        Calculates and prints the compound interest for a savings plan over a specified number of years.

        Args:
            annual_saving_rate (float or int): The amount of money saved annually.
            interest (float or int): The annual interest rate (in percentage).
            years (int): The number of years for which the interest is calculated.

        Returns:
             None: The function prints the results directly.

        Example:
        1. Year Total Sum:  3,210.00     Total Savings: 3,000.00     Interest: 210.00
        2. Year Total Sum:  6,586.70     Total Savings: 6,000.00     Interest: 586.70
        ...
    """
    if not isinstance(years, int) or  not isinstance(interest, (float, int)) or not isinstance(annual_saving_rate, (int, float)):
        print(f"Error: No correct init of variables")
        return -1
    total_sum = 0
    for x in range(1,years+1):
        total_sum = (total_sum + annual_saving_rate) * ((interest + 100) / 100)
        total_savings = annual_saving_rate * x
        interest_sum = total_sum - total_savings
        print(f"{x:>{len(str(years))}}.Year Total Sum: {total_sum:<{len(str(years))+20},.2f} Total Savings: {total_savings:<{len(str(years))+20},.2f} Interest: {interest_sum:<{len(str(years))},.2f}")

if __name__ == "__main__":
    compound_interest(1200, 7, 18)