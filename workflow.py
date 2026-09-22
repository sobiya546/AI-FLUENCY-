from config import PRIVATE_EXPENSES


def get_food_expense():
    total = 0

    for expense in PRIVATE_EXPENSES:
        if expense["category"] == "Food":
            total += expense["amount"]

    return total


def get_total_expense():
    total = 0

    for expense in PRIVATE_EXPENSES:
        total += expense["amount"]

    return total


def get_highest_category():
    category_totals = {}

    for expense in PRIVATE_EXPENSES:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]

    highest_category = max(
        category_totals,
        key=category_totals.get
    )

    return highest_category, category_totals[highest_category]


def workflow(question):

    question = question.lower()

    if "food" in question:
        return f"You spent ₹{get_food_expense()} on food."

    elif "total" in question:
        return f"Your total spending is ₹{get_total_expense()}."

    elif "most" in question or "highest" in question:
        category, amount = get_highest_category()
        return f"You spent the most on {category}, with ₹{amount}."

    elif "save" in question:
        return "Track your daily expenses and set a monthly spending limit."

    else:
        return "Sorry, I don't have a rule for this question."


# Questions

question1 = "How much did I spend on food?"
question2 = "What is my total spending?"
question3 = "Which category did I spend the most on?"
question4 = "Give me a general tip to save money."


# Output

print("===== RULE-BASED WORKFLOW =====\n")

print("Question 1:", question1)
print("Answer:", workflow(question1))
print()

print("Question 2:", question2)
print("Answer:", workflow(question2))
print()

print("Question 3:", question3)
print("Answer:", workflow(question3))
print()

print("Question 4:", question4)
print("Answer:", workflow(question4))