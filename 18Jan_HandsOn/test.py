import matplotlib.pyplot as plt

def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)

    if monthly_rate == 0:
        return principal / tenure_months

    emi = principal * monthly_rate * (1 + monthly_rate) ** tenure_months / \
          ((1 + monthly_rate) ** tenure_months - 1)
    return emi


def generate_amortization_schedule(principal, annual_rate, tenure_months, emi):
    monthly_rate = annual_rate / (12 * 100)

    balance = principal
    months = []
    emis = []
    principal_paid = []
    interest_paid = []
    remaining_balance = []
    cumulative_interest = []

    total_interest = 0

    for month in range(1, tenure_months + 1):
        interest = balance * monthly_rate
        principal_component = emi - interest
        balance -= principal_component

        total_interest += interest

        months.append(month)
        emis.append(emi)
        principal_paid.append(principal_component)
        interest_paid.append(interest)
        remaining_balance.append(balance if balance > 0 else 0)
        cumulative_interest.append(total_interest)

    return (months, emis, principal_paid, interest_paid,
            remaining_balance, cumulative_interest, total_interest)


def plot_charts(months, emis, principal_paid, interest_paid,
                remaining_balance, cumulative_interest,
                principal, total_interest):

    # 1. EMI vs Month
    plt.figure()
    plt.plot(months, emis)
    plt.xlabel("Month")
    plt.ylabel("EMI Amount")
    plt.title("EMI vs Month")
    plt.show()

    # 2. Remaining Loan Balance vs Month
    plt.figure()
    plt.plot(months, remaining_balance)
    plt.xlabel("Month")
    plt.ylabel("Remaining Loan Balance")
    plt.title("Remaining Loan Balance vs Month")
    plt.show()

    # 3. Principal vs Interest per Month
    plt.figure()
    plt.plot(months, principal_paid, label="Principal")
    plt.plot(months, interest_paid, label="Interest")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.title("Principal vs Interest per Month")
    plt.legend()
    plt.show()

    # 4. Cumulative Interest Paid vs Time
    plt.figure()
    plt.plot(months, cumulative_interest)
    plt.xlabel("Month")
    plt.ylabel("Cumulative Interest Paid")
    plt.title("Cumulative Interest Paid vs Time")
    plt.show()

    # 5. Pie Chart – Principal vs Total Interest
    plt.figure()
    plt.pie(
        [principal, total_interest],
        labels=["Principal", "Total Interest"],
        autopct="%1.1f%%"
    )
    plt.title("Principal vs Total Interest")
    plt.show()


def main():
    print("====== Loan Calculator with Graphs ======")

    principal = float(input("Enter loan amount (Principal): "))
    annual_rate = float(input("Enter annual interest rate (%): "))

    tenure_type = input("Is tenure in Years or Months? (Y/M): ").strip().upper()
    tenure_value = int(input("Enter loan tenure: "))

    if tenure_type == "Y":
        tenure_months = tenure_value * 12
    elif tenure_type == "M":
        tenure_months = tenure_value
    else:
        print("Invalid tenure type.")
        return

    emi = calculate_emi(principal, annual_rate, tenure_months)

    (months, emis, principal_paid, interest_paid,
     remaining_balance, cumulative_interest,
     total_interest) = generate_amortization_schedule(
        principal, annual_rate, tenure_months, emi
    )

    print("\n====== Loan Summary ======")
    print(f"Monthly EMI         : ₹{emi:,.2f}")
    print(f"Total Payment       : ₹{emi * tenure_months:,.2f}")
    print(f"Total Interest Paid : ₹{total_interest:,.2f}")

    plot_charts(
        months, emis, principal_paid, interest_paid,
        remaining_balance, cumulative_interest,
        principal, total_interest
    )


if __name__ == "__main__":
    main()
