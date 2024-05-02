from llm.ollama import Ollama


class CvFormFiller:
    def __init__(self):
        self._ollama = Ollama()

    def fill(self, cv_template: str, job_description: str) -> str:
        cv = self._ollama.chat(
            "Replace [skills] and [experience] with relevant skills and experience keeping them aligned with job titles in the following cv template: "
            + cv_template
            + "\n to make a good match for the following job, avoid repeating description or already used phrases, make it short and informative, avoid using default and obvious things:\n"
            + job_description
        )
        return cv
