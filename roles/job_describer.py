from llm_utils.ollama import Ollama


class JobDescriber:
    def __init__(self):
        self._ollama = Ollama()

    def create_job_description(self, job_description_html: str) -> str:
        job_description = self._ollama.chat(
            "Extract job description from the following HTML in human readable format: "
            + job_description_html
        )
        return job_description
