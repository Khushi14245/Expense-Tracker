from ex import Expense
import calendar
import datetime


def main():
    
    expense_file_path = "expenses.csv"
    budget = float(input("What is your budget? "))
    expense = how_much_expense()
    save_to_file(expense, expense_file_path)
    summarising_expenses( budget, expense_file_path)

   
   
   
   


def how_much_expense():
    print("How much u have spent!!! ")
    expense_name = input("Where have u spent?")
    expense_amount = float(input("How much u have spent?"))
    print(f" Expense name is {expense_name}, {expense_amount}")    

                                     
    expense_categories = ["Food", "Home", "Work", "Fun", "Miscelleanous"]

    while True:
      print("In which category u are spending?")
      for i, category_name in enumerate(expense_categories):
         print(f"{i+1}.{category_name}")


      value_range = f"[1-{len(expense_categories)}]"
      selected_index = int(input(f"In which category u are spending??? {value_range}")) -1

      if selected_index in range(len(expense_categories)):
          selected_category = expense_categories[selected_index]
          print(selected_category)

          new_expense = Expense(name= expense_name, category= selected_category, amount = expense_amount)
          print(f"Expense name is {new_expense.name}\n",f"Expense category is {new_expense.category}\n", f"Expense amount is {new_expense.amount}")
          return new_expense

          
      else:
          print(f"Please select the valid category {value_range}")

      break


def save_to_file(expense: Expense, expense_file_path):
    print(f"Saving the expense to file :{expense} to {expense_file_path}")
    with open(expense_file_path, "a") as file:
        file.write(f"{expense.name},{expense.category}, {expense.amount}\n")
    

def summarising_expenses(budget, expense_file_path):
    print("Summarizing expenses...")
    expenses=[]
    with open(expense_file_path, "r") as file:
        lines= file.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            print(f" {expense_name} {expense_category} {expense_amount}")
            expenses_in_line= Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
            #print(f"Expense name is {expenses_in_line.name}")
            expenses.append(expenses_in_line)
            #print(expenses)

    amount_by_category = {}
    for expense in expenses:
        if expense.category in amount_by_category:
            amount_by_category[expense.category] += expense.amount
        else:
            amount_by_category[expense.category] = expense.amount

    print("Total amount spent by category:")
    for category, total_amount in amount_by_category.items():
      print(f"{category}: ${total_amount:.2f}")


    total_amount = sum(expense.amount for expense in expenses)
    print(f"Total amount spent: ${total_amount:.2f}")

    
    remaining_budget = budget - total_amount
    print(f"Remaining budget: ${remaining_budget:.2f}")
 
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print("Remaining days in month: ", remaining_days)

    Daily_budget = remaining_budget / remaining_days
    print("Daily budget is: ", Daily_budget)




if __name__ == "__main__":
    main()