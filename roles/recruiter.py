from llm.ollama import Ollama


class FriendlyRecruiter:
    def __init__(self, model_name: str):
        self._ollama = Ollama(model_name)

    def review_cv(self, cv: str, job_description: str) -> str:
        response = self._ollama.chat(
            "Review the experience of a candidate for the following job description: \n\n"
            + job_description
            + "\n\nThe experience is: \n\n"
            + cv
            + "\n\n If the experience is suitable for the job, please respond with CV as it was."
            + " Otherwise respond with an updated experiences, that would make the experience suitable."
        )
        return response

