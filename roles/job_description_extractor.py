from llm.ollama import Ollama


class JobDescriptionExtractor:
    def __init__(self, model_name: str):
        self._ollama = Ollama(model_name)

    def extract(self, job_description_html: str) -> str:
        job_description = self._ollama.chat(
            "Extract in job description and key requirements for the role with description, squash skills that are similar and return only the key requirements: "
            + job_description_html
        )
        return job_description
