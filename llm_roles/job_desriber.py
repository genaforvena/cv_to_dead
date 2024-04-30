from llm_utils.ollama import Ollama


class JobDescriber:
    def create_job_description(self, job_description_html: str) -> str:
        ollama = Ollama()
        job_description = ollama.chat(
            "Extract job description from the following HTML: " + job_description_html
        )
        return job_description
