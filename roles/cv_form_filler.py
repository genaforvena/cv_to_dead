from llm.ollama import Ollama


class CvFormFiller:
    def __init__(self):
        self._ollama = Ollama()

    def fill(self, cv_template: str, job_description: str) -> str:
        cv = self._ollama.chat(
            "Fill the following cv template with skills and experience: "
            + cv_template
            + "\n to make a great fit for the following job description, but will not re-phrase it:\n"
            + job_description
        )
        return cv
