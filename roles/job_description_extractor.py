from llm.ollama import Ollama


class JobDescriptionExtractor:
    def __init__(self):
        self._ollama = Ollama()

    def extract(self, job_description_html: str) -> str:
        job_description = self._ollama.chat(
            "Extract in job description string from html: " + job_description_html
        )
        return job_description
