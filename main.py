from roles.job_description_extractor import JobDescriptionExtractor as extractor
from roles.cv_form_filler import CvFormFiller as filler
from roles.recruiter import Recruiter as recruiter


def make_cv(job_description_html: str, cv_template: str) -> str:
    job_description = extractor().extract(job_description_html)
    cv = filler().fill(cv_template, job_description)
    return cv


if __name__ == "__main__":
    job_description = open("resources/job_description.txt").read()
    cv_template = open("resources/cv_template").read()
    review_passed = False
    while not review_passed:
        cv = make_cv(job_description, cv_template)
        print(cv)
        review_passed = recruiter().review_cv(job_description, cv)
