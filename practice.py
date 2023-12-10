import property_information

def Property_information():
    
    api_url = "https://www.biggerpockets.com/analysis/rentals/new#"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching financial data: {e}")
        return None

def calculate_roi(income, expenses, total_investment):
    # Monthly Cash Flow
    total_monthly_cash_flow = income - expenses
    
    # Cash on Cash Return on Investment
    cash_on_cash_roi = (total_monthly_cash_flow * 12) / total_investment * 100
    
    return total_monthly_cash_flow, cash_on_cash_roi

def main():
    # Fetch financial data from the API
    financial_data = get_financial_data()
    
    if financial_data:
        # Example values
        monthly_rental_income = 2000
        taxes = 300
        insurance = 100
        vacancy = 100
        repairs = 100
        property_management = 200
        mortgage = 860
        
        # Calculate total monthly expenses
        total_expenses = taxes + insurance + vacancy + repairs + property_management + mortgage
        
        # Calculate total investment
        down_payment = 40000
        closing_costs = 3000
        repair_budget = 7000
        misc_other = 0
        total_investment = down_payment + closing_costs + repair_budget + misc_other
        
        # Calculate ROI
        total_monthly_cash_flow, cash_on_cash_roi = calculate_roi(
            monthly_rental_income, total_expenses, total_investment
        )
        
        # Display Results
        print(f"Monthly Rental Income: ${monthly_rental_income}")
        print(f"Total Monthly Expenses: ${total_expenses}")
        print(f"Total Monthly Cash Flow: ${total_monthly_cash_flow}")
        print(f"Cash on Cash ROI: {cash_on_cash_roi:.2f}%")

if __name__ == "__main__":
    main()
