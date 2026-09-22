from config import PRIVATE_EXPENSES


def get_expenses_by_category(category):
    total = 0

    for expense in PRIVATE_EXPENSES:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    return total


def get_total_expenses():
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


def calculator(expression):
    try:
        return eval(expression)
    except Exception:
        return "Invalid calculation"


print("===== TOOLS TEST =====\n")

print("Food expense:")
print("₹", get_expenses_by_category("Food"))

print("\nTotal expenses:")
print("₹", get_total_expenses())

category, amount = get_highest_category()

print("\nHighest spending category:")
print(category, "₹", amount)

print("\nCalculator:")
print(calculator("550 + 900 + 1200"))