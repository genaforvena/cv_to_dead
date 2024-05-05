from llm import ollama

class ExperienceExpander:
    def __init__(self, model: str):
        self._ollama = ollama.Ollama(model)

    def expand(self, cv: str) -> str:
        prompt = "Please add more unique work experiences and achievements to enhance the CV. Avoid duplications. Here is the CV to update:\n\n"
        return self._ollama.chat(prompt + cv)
