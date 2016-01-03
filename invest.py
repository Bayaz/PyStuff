def invest(p_amount, a_interest_rate, y):
	p = y
	print("initial amount invested = ", '${:,.2f}'.format(p_amount))
	print("annual interest rate =",  '{:.0%}'.format(a_interest_rate))
	for i in range(1, p + 1):
		p_amount = p_amount * a_interest_rate + p_amount
		print("Year", i, " = ", '${:,.2f}'.format(p_amount))

def start():
	principal_amount = input("Enter amount to invest> ")
	principal_amount = float(principal_amount)
	annual_interest_rate = input("Enter the annual interest rate > ")
	annual_interest_rate = float(annual_interest_rate)
	annual_interest_rate = annual_interest_rate / 100
	years = input("Enter the numbers of years of the investment > ")
	years = int(years)
	invest(principal_amount, annual_interest_rate, years)


start()


