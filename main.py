import argparse
from roles.cv_form_filler import CvFormFiller as filler


def make_cv(job_description: str, cv_template: str) -> str:
    cv = filler().fill(cv_template, job_description)
    return cv


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--job", type=str, required=True)
    args.add_argument("--template", type=str, required=True)
    args = args.parse_args()

    job_description = open(args.job).read()
    cv_template = open(args.template).read()
    cv = make_cv(job_description, cv_template)
    print(cv)
