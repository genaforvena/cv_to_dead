import argparse
from mdpdf import converter
from roles.job_description_extractor import JobDescriptionExtractor as extractor
from roles.cv_form_filler import CvFormFiller as filler
from roles.recruiter import Recruiter as recruiter


def make_cv(job_description_html: str, cv_template: str) -> str:
    job_description = extractor().extract(job_description_html)
    cv = filler().fill(cv_template, job_description)
    return cv


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--job", type=str, required=True)
    args.add_argument("--template", type=str, required=True)
    args.add_argument("--output", type=str, default="resources/cv.md")
    args = args.parse_args()

    job_description = open(args.job).read()
    cv_template = open(args.template).read()
    review_passed = False
    cv = None
    while not review_passed:
        cv = make_cv(job_description, cv_template)
        print(cv)
        review_passed = recruiter().review_cv(job_description, cv)
    if cv is not None:
        md_file_name = "resources/cv.md"
        with open(md_file_name, "w") as f:
            f.write(cv)
        converter.Converter(args.output).convert(md_file_name)
    else:
        print("No CV generated")
