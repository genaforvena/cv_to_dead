import os
import time
import argparse
from roles.cv_form_filler import CvFormFiller as Filler
from roles.job_description_extractor import JobDescriptionExtractor as Describer
from roles.experience_expander import ExperienceExpander as Expander
from roles.cv_merger import CvMerger as Merger

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs-folder", type=str, required=True)
    parser.add_argument(
        "--template",
        type=str,
        required=True,
        help="Path to the CV template to be filled, please note that cv_header.md and cv_footer.md should be in the same directory as the template and will be added to the beginning and end of the filled CV.",
    )
    parser.add_argument("--model", type=str, default="llama3")
    args = parser.parse_args()
    model_name = args.model

    with open(args.template, "r") as template_file:
        cv_template = template_file.read()
        template_directory = os.path.dirname(template_file.name)

    describer_instance = Describer(model_name)
    filler_instance = Filler(model_name)
    expander_instance = Expander(model_name)
    merger_instance = Merger(model_name)

    for job_filename in os.listdir(args.jobs_folder):
        if not job_filename.endswith(".txt"):
            continue
        job_filepath = os.path.join(args.jobs_folder, job_filename)
        with open(job_filepath, "r") as job_file:
            job_description = job_file.read()
        abridged_description = describer_instance.extract(job_description)
        filled_cv = filler_instance.fill(cv_template, abridged_description)
        expanded_cv = expander_instance.expand(filled_cv)
        similar_cv = filler_instance.make_similar(expanded_cv)
        merged_cv = merger_instance.merge([expanded_cv, similar_cv])
        timestamp = str(int(time.time()))
        cv_filename = (
            f"{job_filename.replace('.txt', '')}_cv_{model_name}_{timestamp}.md"
        )
        cv_filepath = os.path.join(args.jobs_folder, cv_filename)
        with open(cv_filepath, "w") as cv_file:
            cv_file.write(open(template_directory + "/cv_header.md", "r").read())
            cv_file.write(merged_cv)
            cv_file.write(open(template_directory + "/cv_footer.md", "r").read())
