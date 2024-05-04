from llm import ollama


class ExperienceExpander:
    def __init__(self, model):
        self._ollama = ollama.Ollama(model)

    def expand(self, cv: str) -> str:
        return self._ollama.chat(
            "Please add more experience details to make the cv more engaging and stand out, but avoid duplicated experiences. Return the full updated cv. Here is the cv to update:\n\n"
            + cv
        )
