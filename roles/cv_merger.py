from llm.ollama import Ollama


class CvMerger:
    def __init__(self, model_name: str):
        self._ollama = Ollama(model_name)

    def merge(self, cvs: list[str]) -> str:
        merged = self._ollama.chat(
            "Merge these CVs into one by merging experiences, but there should be no duplicates: "
            + "\n\n\n\n".join(cvs)
        )

        return merged
