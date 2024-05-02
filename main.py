import os
import argparse
from roles.cv_form_filler import CvFormFiller as filler


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--jobs-folder", type=str, required=True)
    args.add_argument("--template", type=str, required=True)
    args = args.parse_args()

    cv_template = open(args.template).read()
    for job_file in os.listdir(args.jobs_folder):
        if not job_file.endswith(".txt"):
            continue
        job_description = open(os.path.join(args.jobs_folder, job_file)).read()
        cv = filler().fill(cv_template, job_description)
        cv_file = job_file.replace(".txt", "_cv.md")
        open(os.path.join(args.jobs_folder, cv_file), "w").write(cv)
