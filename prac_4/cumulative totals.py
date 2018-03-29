"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = get_months()
    month_order = 0


    for month in range(1, months + 1):
        month_order = month_order + 1
        income = float(input("Enter income for month {}:".format(month_order)))
        incomes.append(income)

    total_incomes(incomes, months)


def total_incomes(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def get_months():
    months = int(input("How many months? "))
    return months


main()