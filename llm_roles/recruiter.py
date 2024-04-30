from llm_utils.ollama import Ollama


class Recruiter:
    def __init__(self):
        self._ollama = Ollama()

    def review_cv(self, job_description: str, cv: str) -> bool:
        response = self._ollama.chat(
            "Review the CV of a candidate for the following job description: "
            + job_description
            + "\nThe CV is: "
            + cv
            + ". If the CV is suitable for the job, please responsd with 'yes' otherwise 'no'."
        )
        response = response["content"]["message"]
        return "yes" in response.lower()
