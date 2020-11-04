total_cost = float(input('What is the cost of your dream home?'))
annual_salary = float(input('What is your annual salary?'))
portion_saved = float(input('What portion of your salary will you save?'))
semi_annual_raise = float(input('What is your semi annual raise?'))

portion_down_payment = total_cost * float(0.25)
monthly_salary = int(annual_salary / 12)
current_savings = 0
r = float(0.04)
months = 0


while current_savings < portion_down_payment:
    saved_this_month = ((current_savings*r)/12)
    current_savings += saved_this_month
    current_savings += ((monthly_salary * portion_saved))
    months += 1
    if months % 6 == 0:
        annual_salary += (annual_salary * semi_annual_raise)
        monthly_salary = int(annual_salary / 12)

print(months)