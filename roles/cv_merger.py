from llm.ollama import Ollama


class CvMerger:
    def __init__(self, model_name: str):
        self._ollama = Ollama(model_name)

    def merge(self, cvs: list[str]) -> str:
        merged = self._ollama.chat(
            "Merge these CVs into one, trying to pick the best parts and avoiding duplicate experience entries: "
            + "\n\n\n\n".join(cvs)
        )

        return merged
