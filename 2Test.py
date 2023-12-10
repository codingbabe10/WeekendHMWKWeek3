def calculate_roi():
    
    monthly_rental_income = float(input("Enter monthly rental income: $"))
    taxes = float(input("Enter monthly taxes: $"))
    insurance = float(input("Enter monthly insurance: $"))
    vacancy = float(input("Enter monthly vacancy: $"))
    repairs = float(input("Enter monthly repairs: $"))
    property_management = float(input("Enter monthly property management: $"))
    mortgage = float(input("Enter monthly mortgage: $"))

    
    total_expenses = taxes + insurance + vacancy + repairs + property_management + mortgage

   
    total_monthly_cash_flow = monthly_rental_income - total_expenses

   
    down_payment = float(input("Enter down payment: $"))
    closing_costs = float(input("Enter closing costs: $"))
    repair_budget = float(input("Enter repair budget: $"))
    misc_other = float(input("Enter misc. other expenses: $"))
    total_investment = down_payment + closing_costs + repair_budget + misc_other

   
    cash_on_cash_roi = (total_monthly_cash_flow * 12) / total_investment * 100

    return total_monthly_cash_flow, cash_on_cash_roi

def main():
    total_monthly_cash_flow, cash_on_cash_roi = calculate_roi()

    
    print(f"Total Monthly Cash Flow: ${total_monthly_cash_flow:.2f}")
    print(f"Cash on Cash ROI: {cash_on_cash_roi:.2f}%")

if __name__ == "__main__":
    main()
