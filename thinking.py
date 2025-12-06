def detect_thinking(user_input: str) -> str:
    text = user_input.lower()

    # Debugging mode: if user gave code or asks "why doesn't this work?"
    if "def " in text or "print(" in text or "error" in text or "doesn't work" in text:
        return "debug"

    # Explanation mode
    if "explain" in text or "what is" in text or "how does" in text:
        return "explain"

    # Exercise mode
    if "exercise" in text or "practice" in text or "problem" in text:
        return "exercise"

    # Feedback mode
    if "did i do this right" in text or "check my answer" in text or "is this correct" in text:
        return "feedback"

    # Default
    return "general"