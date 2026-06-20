from src.ingestion import load_faq_data, build_index
documents = load_faq_data()
index = build_index(documents)

INSTRUCTION = f"""
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
"""

USER_PROMPT_TEMPLATE = """
Question:
{question}

Context:
{context}
"""

def search(question, course = "llm-zoomcamp"):
    return index.search(question, boost_dict = {"question": 2, "section": 0.5}, 
                        filter_dict = {"course": course}, 
                        num_results = 5)

def build_context(search_results):
    lines = []

    for doc in search_results:
        lines.append(doc["section"])
        lines.append("Q: " + doc["question"])
        lines.append("A: " + doc["answer"])
        lines.append("")

    return "\n".join(lines).strip()

def build_prompt(question, search_results):
    context = build_context(search_results)
    prompt = USER_PROMPT_TEMPLATE.format(question = question, context = context)
    return prompt.strip()


def llm(instructions, user_prompt, model="llama-3.1-8b-instant"):
    message_history = [
        {"role": "developer", "content": INSTRUCTION},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=message_history
    )

    return response.choices[0].message.content