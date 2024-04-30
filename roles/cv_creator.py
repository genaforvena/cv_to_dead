from llm.ollama import Ollama


class CvCreator:
    def __init__(self):
        self._ollama = Ollama()

    def create_cv(self, job_description: str, cv_template: str) -> str:
        cv = self._ollama.chat(
            "Fill out this CV: "
            + cv_template
            + "\n to make a great fit for the following job description:\n"
            + job_description
        )
        return cv
