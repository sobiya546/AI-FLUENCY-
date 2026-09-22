from openai import OpenAI
from config import MODEL, GROQ_API_KEY
from tools import (
    get_expenses_by_category,
    get_total_expenses,
    get_highest_category
)

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


def agent(question):

    question_lower = question.lower()

    # Agent decides which tool to use
    if "food" in question_lower:
        result = get_expenses_by_category("Food")
        return f"You spent ₹{result} on food."

    elif "total" in question_lower:
        result = get_total_expenses()
        return f"Your total spending is ₹{result}."

    elif "most" in question_lower or "highest" in question_lower:
        category, amount = get_highest_category()
        return f"You spent the most on {category}, with ₹{amount}."

    else:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful personal expense assistant."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content


# Test questions

question1 = "How much did I spend on food?"
question2 = "What is my total spending?"
question3 = "Which category did I spend the most on?"
question4 = "Give me a general tip to save money."


print("===== AI AGENT =====\n")

print("Question 1:", question1)
print("Answer:", agent(question1))
print()

print("Question 2:", question2)
print("Answer:", agent(question2))
print()

print("Question 3:", question3)
print("Answer:", agent(question3))
print()

print("Question 4:", question4)
print("Answer:", agent(question4))