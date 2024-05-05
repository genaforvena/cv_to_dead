from llm.ollama import Ollama


class CvFormFiller:
    def __init__(self, model_name: str):
        self._ollama = Ollama(model_name)

    def fill(self, cv_template: str, job_description: str) -> str:
        chunks = cv_template.split("\n")
        cv = ""
        for chunk in chunks:
            if "[" in chunk and "]" in chunk:
                prompt = f"Replace the placeholders in square brackets in the following CV template:\n\n'''{chunk}'''\n\nwith relevant skills and experience information to make the CV a good match for the job description:\n\n'''{job_description}'''\n\nHowever, avoid copying the job description verbatim and make the CV skills slightly different from the description. Each placeholder replacement should consist of at least three unique items. Only replace the placeholders and keep the rest of the CV intact."
                cv += "\n" + self._ollama.chat(prompt)
            else:
                cv += "\n" + chunk
        return cv

    def make_similar(self, cv: str) -> str:
        prompt = f"Add different sets of experiences to each position while keeping positions intact to this CV:\n\n'''{cv}'''"
        cv = self._ollama.chat(prompt)
        return cv
