from llm_utils.ollama import Ollama

class CvCreator:
    def __init__(self):
        self._ollama = Ollama()

    def create_cv(self, job_description: str) -> str:
