import re
import ollama


class Ollama:
    def __init__(self, model_name: str = "llama3:text"):
        self._history = []
        self._model_name = model_name

    def chat(self, prompt: str) -> str:
        print()
        message = {"role": "user", "content": prompt}
        self._history.append(message)
        msg = ""
        if ":text" in self._model_name:
            resp = ollama.generate(model=self._model_name, prompt=prompt, stream=True)
            for chunk in resp:
                p = chunk["response"]
                print(p, end="", flush=True)
                msg += p
        else:
            resp = ollama.chat(
                model=self._model_name, messages=self._history, stream=True
            )
            for chunk in resp:
                p = chunk["message"]["content"]
                print(p, end="", flush=True)
                msg += p
        self._history.append({"role": "assistant", "content": msg})
        return self._history[-1]["content"]
