
total = input("How much was your bill: ")
tip_percent = input("What percentage would you like to tip: ")
tip = float(tip_percent) * int(total)
final_bill = int(total) + float(tip_percent)

if float(tip_percent) <= .14:
	print("Your tip percentage is %{}, which is below 14%, you are a cheap ass!".format(tip_percent))
	print("Your total bill is ${}".format(final_bill))
elif (float(tip_percent) > .15) and (float(tip_percent) <= .2):
	print("Your tip percentage ${}, which is good and proper.".format(tip_percent))
	print("Your total bill is ${}".format(final_bill))
else:
	print("Your tip percentage ${}, you are very very generous. Spectacular".format(tip_percent))
	print("Your total bill is ${}".format(final_bill))


