from llm.ollama import Ollama


class CvFormFiller:
    def __init__(self):
        self._ollama = Ollama()

    def fill(self, cv_template: str, job_description: str) -> str:
        cv = self._ollama.chat(
            "Replace placeholders in square brackets in the following cv: \n\n''' "
            + cv_template
            + "'''\n\n with relevant skills and experience information to make the cv a good match for the following job description:\n\n'''"
            + job_description
            + "'''\n\n but avoid copying the job description verbatim and make CV skills a tiny bit different from the description."
            + " Each placeholder replacement should be at least three items and all items should be unique. Only replace placeholders, keep the rest intact. "
        )
        return cv
