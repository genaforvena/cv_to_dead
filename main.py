from roles.job_description_extractor import JobDescriptionExtractor as extractor
from roles.cv_form_filler import CvFormFiller as filler


def make_cv(job_description_html: str, cv_template: str) -> str:
    job_description = extractor().extract(job_description_html)
    cv = filler().fill(cv_template, job_description)
    return cv


if __name__ == "__main__":
    job_description_html = open("resources/job_description.html").read()
    cv_template = open("resources/cv_template").read()
    print(
        make_cv(
            job_description_html,
            cv_template,
        )
    )
