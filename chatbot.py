from openai import OpenAI
from config import MODEL, GROQ_API_KEY, PRIVATE_EXPENSES

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


def ask_chatbot(question):

    prompt = f"""
You are a simple personal expense chatbot.

Here is the private expense data:

{PRIVATE_EXPENSES}

Answer the question using the private data.

Question:
{question}

Give a simple and clear answer.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


question1 = "How much did I spend on food?"
question2 = "What is my total spending?"
question3 = "Which category did I spend the most on?"
question4 = "Give me a general tip to save money."


print("===== PLAIN CHATBOT =====\n")

print("Question 1:", question1)
print("Answer:", ask_chatbot(question1))
print()

print("Question 2:", question2)
print("Answer:", ask_chatbot(question2))
print()

print("Question 3:", question3)
print("Answer:", ask_chatbot(question3))
print()

print("Question 4:", question4)
print("Answer:", ask_chatbot(question4))