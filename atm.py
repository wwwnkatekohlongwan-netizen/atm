def main():
	CORRECT_PIN = "1234"
	attempts = 0
	max_attempts = 3
	balance = 1000.0

	while attempts < max_attempts:
		pin = input("Enter your 4-digit PIN: ")
		if pin == CORRECT_PIN:
			break
		attempts += 1
		print(f"Incorrect PIN. {max_attempts - attempts} attempts remaining.")
	else:
		print("Maximum attempts reached. Card blocked.")
		return

	while True:
		print("\nChoose an option:")
		print("1. Check balance")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Exit")

		choice = input("Option: ").strip()
		if choice == "1":
			print(f"Current balance: R{balance:.2f}")
		elif choice == "2":
			try:
				amt = float(input("Amount to deposit: R"))
			except ValueError:
				print("Invalid amount.")
				continue
			balance += amt
			print(f"Deposited R{amt:.2f}. New balance: R{balance:.2f}")
		elif choice == "3":
			try:
				amt = float(input("Amount to withdraw: R"))
			except ValueError:
				print("Invalid amount.")
				continue
			if amt > balance:
				print("Insufficient funds.")
			else:
				balance -= amt
				print(f"Withdrew R{amt:.2f}. New balance: R{balance:.2f}")
		elif choice == "4":
			print("Thank you. Goodbye.")
			break
		else:
			print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
	main()



