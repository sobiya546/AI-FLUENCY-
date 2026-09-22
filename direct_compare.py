"""Day 2: Demonstrate Direct Prompting for expense-related questions."""

from config import client, MODEL, banner


QUESTIONS = [
    "I spent ₹1200 on Food, ₹800 on Travel and ₹1000 on Shopping. What is my total spending?",

    "I have ₹5000 and spend ₹1250. How much money do I have left?",

    "Ravi spends more than Kumar. Kumar spends more than Arun. Who spends the most?",
]


DIRECT_PROMPT = (
    "You are a helpful assistant. "
    "Answer the question directly. "
    "Give only the final answer. "
    "Do not show reasoning."
)


def ask(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": DIRECT_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    banner("DIRECT PROMPTING")

    for number, question in enumerate(QUESTIONS, start=1):
        print("=" * 72)
        print(f"QUESTION {number}: {question}")
        print()

        print("ANSWER:")
        print(ask(question))
        print()