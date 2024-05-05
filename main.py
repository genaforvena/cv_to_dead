import os
import time
import argparse
from roles.cv_form_filler import CvFormFiller as Filler
from roles.job_description_extractor import JobDescriptionExtractor as Describer
from roles.experience_expander import ExperienceExpander as Expander

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs-folder", type=str, required=True)
    parser.add_argument("--template", type=str, required=True)
    parser.add_argument("--model", type=str, default="llama3")
    args = parser.parse_args()
    model_name = args.model

    with open(args.template, 'r') as template_file:
        cv_template = template_file.read()

    describer_instance = Describer(model_name)
    filler_instance = Filler(model_name)
    expander_instance = Expander(model_name)

    for job_filename in os.listdir(args.jobs_folder):
        if not job_filename.endswith(".txt"):
            continue
        job_filepath = os.path.join(args.jobs_folder, job_filename)
        with open(job_filepath, 'r') as job_file:
            job_description = job_file.read()
        abridged_description = describer_instance.extract(job_description)
        filled_cv = filler_instance.fill(cv_template, abridged_description)
        expanded_cv = expander_instance.expand(filled_cv)
        timestamp = str(int(time.time()))
        cv_filename = f"{job_filename.replace('.txt', '')}_cv_{model_name}_{timestamp}.md"
        cv_filepath = os.path.join(args.jobs_folder, cv_filename)
        with open(cv_filepath, 'w') as cv_file:
            cv_file.write(expanded_cv)