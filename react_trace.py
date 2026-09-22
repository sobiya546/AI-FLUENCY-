"""Day 2: Print a ReAct-style trace for the expense agent."""

from tools import (
get_expenses_by_category,
get_total_expenses,
get_highest_category,
calculator
)

QUESTION = "Which category has the highest spending, and what is the total spending?"

print("QUESTION:", QUESTION)
print("\n--- the agent's actions and observations ---")

# Step 1: Get the highest spending category

category, amount = get_highest_category()
print(
f"step 1: get_highest_category() "
f"-> {category}, ₹{amount}"
)

# Step 2: Get total spending

total = get_total_expenses()
print(
f"step 2: get_total_expenses() "
f"-> ₹{total}"
)

# Step 3: Calculate the percentage of total spending

percentage = calculator(f"({amount} / {total}) * 100")
print(
f"step 3: calculator("
f"'({amount} / {total}) * 100') "
f"-> {percentage:.2f}%"
)

print("\nFINAL ANSWER:")
print(
f"You spent the most on {category}, with ₹{amount}. "
f"Your total spending is ₹{total}. "
f"{category} accounts for approximately {percentage:.2f}% "
f"of your total spending."
)
