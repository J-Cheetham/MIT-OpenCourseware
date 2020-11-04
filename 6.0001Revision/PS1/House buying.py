initial_salary = int(input('What is your salary?')) # salary with no dec places
monthly_salary = ((initial_salary * int(100)) / int(12))


savings_rate_upper_bound = int(100)
savings_rate_lower_bound = int(0)

semi_annual_raise = int(7) # 7% semi annual raise
investment_annual_return = int(4) # 4% investment return

cost_of_house = 100000000 # 1 million with 2 dec places
down_payment = cost_of_house * (int(25) / int(100))
down_payment_upper = down_payment + int(10000)
down_payment_lower = down_payment - int(10000)

total_months = int(36)
current_savings = int(0)

counter = 0
while current_savings < down_payment_lower or current_savings > down_payment_upper:

    current_savings_rate = int((savings_rate_upper_bound - savings_rate_lower_bound) / 2)
    current_savings = int(0)
    annual_salary = int(0)
    monthly_salary = ((initial_salary * int(100)) / int(12))
    months_elapsed = int(0)

    while months_elapsed < total_months:
        current_savings += ((current_savings * (investment_annual_return / int(100))) / int(12))
        current_savings += (monthly_salary * (current_savings_rate / int(100)))
        months_elapsed += 1
        if months_elapsed % 6 == 0:
            annual_salary += (annual_salary * (semi_annual_raise / int(100)))
            monthly_salary = int(annual_salary / int(12))

        if current_savings > down_payment_lower and current_savings < down_payment_upper:
            print('Best savings rate:', float(current_savings_rate) / 100, '\n Steps in Bisection Search:', counter)
            break
        elif counter > 20:
            break
        elif current_savings > down_payment_upper:
            savings_rate_upper_bound = current_savings_rate
            counter += 1
            print('Savings rate too large.')
            print('Current savings:', current_savings)
            print('Down payment:', down_payment)
        elif current_savings < down_payment_lower:
            savings_rate_lower_bound = current_savings_rate
            counter += 1
            print('Savings rate too small')

