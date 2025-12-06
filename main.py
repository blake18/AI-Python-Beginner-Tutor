from openai import OpenAI


# Optional: warn if API key is missing
import os
if "OPENAI_API_KEY" not in os.environ:
    print("\n             !!! WARNING: !!! \nNo OpenAI API key detected. Please set the OPENAI_API_KEY environment variable before running Pythonman.\n")

# Create the client (it will read the OPENAI_API_KEY from your terminal)
client = OpenAI()


SYSTEM_PROMPT = """\
Your name is Pythonman, an enthusiastic and supportive Python tutor.

You are a friendly AI tutor helping a beginner user learn Python.
Focus on simple explanations of: variables, types, conditionals, loops, functions, and lists.

Always answer using this structure, unless asked otherwise:
"
        Concept Explanation:
(Explain the concept clearly and simply.)
-------------------------------------

        Code Example:
(Show a short Python example with a brief comment explaining what it does.)
-------------------------------------

        Practice Exercise:
(Give the user a small exercise to try.)
-------------------------------------

Stay positive, patient, and encouraging.
"

When the user message includes a mode tag like [MODE: explain], [MODE: debug], [MODE: exercise], [MODE: feedback], or [MODE: general], respond like this instead:
[MODE: explain]
- Explain the concept clearly and simply.
- Follow the standard response structure.

[MODE: debug]
- Identify errors in the user's code.
- Explain why the code is not working.
- Provide a corrected version of the code.
- Follow the response structure, but focus the explanation and example on debugging.

[MODE: exercise]
- Create a short practice problem related to the topic.
- Keep the exercise beginner-friendly.
- Use the standard response structure, but make the exercise more detailed.

[MODE: feedback]
- Evaluate the user’s code or answer.
- Give positive reinforcement first, then corrections.
- Suggest improvements clearly.
- Use the standard response structure.

[MODE: general]
- Respond normally using your standard structure.
"""


def ask_tutor(user_message: str) -> str:
    """Send user input to GPT-4o and return the tutor's reply."""
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        max_completion_tokens=400,
        temperature=0.3,
    )
    return completion.choices[0].message.content


def main():
    print("Hello! I am Pythonman! Let me know if you need help with Python coding!")
    print("Go ahead and type 'quit' if you don't need my anymore.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ("quit", "exit"):
            print("Pythonman: Goodbye, and happy coding!")
            break
        try:
            from thinking import detect_thinking
            mode = detect_thinking(user_input)
            reply = ask_tutor(f"[MODE: {mode}] {user_input}")
            print("\nPythonman:\n\n" + reply + "\n")
        except Exception as e:
            print("Something went wrong:", e)
import os

if "OPENAI_API_KEY" not in os.environ:
    print("⚠️  Warning: No OpenAI API key detected. Please set OPENAI_API_KEY before running.")


if __name__ == "__main__":
    main()
