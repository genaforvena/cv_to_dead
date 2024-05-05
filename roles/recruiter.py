from llm.ollama import Ollama


class FriendlyRecruiter:
    def __init__(self):
        self._ollama = Ollama()

    def review_cv(self, job_description: str, cv: str) -> str:
        response = self._ollama.chat(
            "Review the CV of a candidate for the following job description: "
            + job_description
            + "\nThe CV is: "
            + cv
            + ". If the CV is suitable for the job, please respond with CV as it was. 
            * " otherwise respond with an updated CV, that would have a missing pieces."
        )
        return response