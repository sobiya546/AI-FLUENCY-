"""Day 2: Compare the same questions WITHOUT and WITH Chain-of-Thought."""

from config import client, MODEL, banner


QUESTIONS = [

    # 1. Multi-step arithmetic
    (
        "A student spends ₹1200 on Food, ₹800 on Travel and ₹1000 on Shopping. "
        "If the student reduces total spending by 10%, how much will the student spend?"
    ),

    # 2. Percentage calculation
    (
        "A person spends ₹4000 on Food out of a total monthly spending of ₹10000. "
        "What percentage of the total spending is used for Food?"
    ),

    # 3. Ordering / logic
    (
        "Ravi spends more than Kumar. Kumar spends more than Arun. "
        "Priya spends less than Arun. Who spends the most and who spends the least?"
    ),
]


DIRECT_PROMPT = (
    "You are a helpful assistant. "
    "Give only the final answer. "
    "Do not explain."
)


COT_PROMPT = (
    "You are a helpful assistant. "
    "Solve the problem step by step. "
    "Number each step and show the calculation in that step. "
    "After the steps, write the last line exactly as: "
    "Final Answer: <answer>"
)


def ask(system_prompt, question):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
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

    banner("CHAIN-OF-THOUGHT COMPARISON")

    for number, question in enumerate(QUESTIONS, start=1):

        print("=" * 72)
        print(f"QUESTION {number}: {question}")
        print()

        print("--- WITHOUT CoT ---")
        print(ask(DIRECT_PROMPT, question))
        print()

        print("--- WITH CoT ---")
        print(ask(COT_PROMPT, question))
        print()