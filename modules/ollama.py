import ollama


class Ollama:
    def __init__(self):
        self._history = []

    def _ask(self, command_for: str, text: str) -> str:
        print()
        message = {"role": "user", "content": command_for + " " + text}
        self._history.append(message)
        resp = ollama.chat(model="phi3mini", messages=self._history, stream=True)
        msg = ""
        for chunk in resp:
            p = chunk["message"]["content"]
            print(p, end="", flush=True)
            msg += p
        self._history.append({"role": "assistant", "content": msg})
        return self._history[-1]["content"]
