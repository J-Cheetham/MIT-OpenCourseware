total_cost = int(100000000)
initial_annual_salary = (int(input('What is your annual salary?'))*100)
annual_salary = initial_annual_salary
# portion_saved = float(input('What portion of your salary will you save?'))
semi_annual_raise = int(700)

portion_down_payment = int(total_cost / int(25))
down_payment_upper = int(portion_down_payment + 10000)
down_payment_lower = int(portion_down_payment - 10000)

monthly_salary = int(annual_salary / 12)
r = int(4)
total_months = int(36)
current_savings = int(0)


lower_bound = int(0)
upper_bound = int(10000)


counter = 0
while current_savings < down_payment_lower or current_savings > down_payment_upper:
    current_savings_rate = int(((upper_bound - lower_bound) / 2)) # adjust savings rate to be within upper and lower bound
    print('Bisection search step:', counter, '\n Savings rate:', current_savings_rate)

    # reset all necessary values to zero in prep for another run
    months_elapsed = int(0)
    current_savings = int(0)
    annual_salary = initial_annual_salary
    monthly_salary = int(annual_salary / 12)

    while months_elapsed < total_months:
        current_savings += ((current_savings*r)/12) # interest earnt from savings
        current_savings += (monthly_salary * current_savings_rate / int(100)) # amount of salary added to savings
        months_elapsed += 1
        if months_elapsed % 6 == 0: # increase salary every 6 months
            annual_salary += (annual_salary * (semi_annual_raise / int(100)))
            monthly_salary = int(annual_salary / 12)
    if current_savings > down_payment_lower and current_savings < down_payment_upper:
        print('Best savings rate:', float(current_savings_rate) / 100, '\n Steps in Bisection Search:', counter)
        break
    elif counter > 20:
        break
    elif current_savings > down_payment_upper:
        upper_bound = current_savings_rate
        counter += 1
        print('Savings rate too large.')
        print('Current savings:', current_savings)
        print('Down payment:', portion_down_payment)
    elif current_savings < down_payment_lower:
        lower_bound = current_savings_rate
        counter += 1
        print('Savings rate too small')





