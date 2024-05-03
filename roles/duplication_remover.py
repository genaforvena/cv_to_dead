from llm.ollama import Ollama


class ExperienceDuplicationRemover:
    def __init__(self, model_name: str):
        self._ollama = Ollama(model_name)
        self._experiences = set()

    def replace_duplicates_with_something_better(self, cv: str) -> str:
        for line in cv.split("\n"):
            if line in self._experiences:
                replacement = self._ollama.chat(
                    "Come up with a better experience for this line: "
                    + line
                    + "\n\n and it should be impressive for this cv: "
                    + cv
                )

                cv = cv.replace(line, replacement)
            self._experiences.add(line)
        return cv
