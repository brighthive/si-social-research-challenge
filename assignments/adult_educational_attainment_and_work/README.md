# Assignment A
# Adult Educational Attainment and Work Outcomes

## Overveiew
This is one of the two take home data challenges and this challenge focuses on Adult Education attainment and their work outcomes. This assignment will ask you to explore how education, in adults, relates to work outcomes as well as the question of impact in this space. This challenge is fictional.

## Introduction
Welcome to your first day in Strategic Initiatives (SI)! The SI team has been callaborating with a national partner, ACME Education, that focuses on workforce training and readiness in the 21st century.

After a quick round of negotioation, our Product & Engineering got the go ahead to store national survey data regarding education in adults and their work outcomes, including whether they work full-time, part-time or if they are underemployed. This data is stored in S3 for now but will be moved to a _data trust_ after your analysis.

To increase velocity and collaboration between SI and Engineering, the friendly engineering folks have created this entire repository for you to work from. By sticking to the project layout and placing some of your code in certain files you enable engineering to quickly productize your work while reducing time to insight for our partner, ACME Education.

Note: Throughout this excercise we assume that the data and any findings are still general applicable even though it was created in 2016.

## Task 0: Setting Things Up

* First, create a Python virtual environment to work within, if you have not already.
* Activate that virtual environment and run `pip install -r requirements.txt`. At BrightHive we typically use `pipenv` but most data scientist are familar with `pip` so we use that throughout.
* Then, download the data by running the `make_dataset_and_references.py` script found in `./src/data`. Some of the files are large (99 mb) and might take a moment to download, depending on your internet connetion.

## Task 1:

ACME Education created a national survey, derived from the National Center for Education Statistics, to measure work outcomes and education among adults. However, a recent report, found in `./references/2016_ATES_Derived_Variables.pdf` notes some issues in `./data/external/ates_pu.csv`, including that several measure of work underutilization, underemployment are missing. To better understand both the new measures and to dig deeper into what questions ACME education, you've been asked to do the following:

* The following asks for written justifications, please save your justifications in the file format of your choice in the `reports` folder and under a file named `assignment_A_task_1` with the appropriate file extension.
* Review both `./references/2016_ATES_Derived_Variables.pdf` and `./references/cbook_ates_pu.pdf` and write up a brief (1-2 paragraph) summary of the work outcome variables found in `./data/external/ates_pu.csv` and any derived (new) work outcome measures that you think could inform a policy discussion around work, education for adults in a metropolition area of your choice (e.g. Chicago).
* Given that SI generally knows that ACME wants to investigate work outcomes by education, select an additional derived outcome measures beyond `UNDEREMP` and write a brief paragraph justifying your choice and contrasting it against other choices. Consider topics like statistical validity, understandability, replicabilty, cost to measure, etc.

## Task 2:
ACME likes your justifications for using both `UNDERMP` and your derived measure! In this task you will be asked to modify the data set to include your derived measure withiin a repeatable process. You will be making changes to `make_dataset_and_reference.py`

* Modify the download methods in `make_dataset_and_reference.py` to accept an True/False argument on whether to `overwrite` any exsting data. If `overwrite` is set to False and the data exists then the function shall not overwrite the data. This will allow anyone to run that file without having to redownload existing data.
* With `overwrite` set to False in the various download functions, add _a new function_ that processes the `ates_pu.csv` file and adds your new derived measure. The resulting file should be written to `./data/processed`. 
  * The name of the file should be set in `config.yaml`, `processed_data` under the key `ates`.
  * The name set in `config.yaml` should be reflected as a file in `./data/processed`
  * The file should be of `.csv` type (comma seperated)

## Task 3
The start a general policy discussion with ACME, data collection and impact, you've been asked to start looking at education and work (or labor) outcome measures. SI has a big meeting next week with ACME and would like a first look at labor outcomes by eductional level. This will be used to drive a 1 pager to be circulated among senior ACME staff and drive data collection efforts down the road for Product & Engineering. Things to consider are overall trends, variances, groups, subgroups, significance, etc.

* Add _a new function_ in `./src/models/model_summary.py` that analyzes the dataset you created in the previous step. Your analysis should examine any trends among education levels, work outcome measures. Are there any subgroups to consider? If you wish to create any visualizations, you may modify `./src/visualization/visualize.py`. Ensure that you update `requirements.py` with any required libaries.
* Any numerical results should be written to `./data/processed` and prefixed with `assignment_A_task_3`
* Any visual results should be written to `./reports/figures` and prefixed ith  `assignment_A_task_3`

## Task 4
SI has asked you to lead the techincal dicussion of the meeting next week. To help prepare the team, Natalie Evan Harris has asked you to write up a brief, but techincal, 1 pager.

* The following asks for written justifications, please save your justifications in the file format of your choice in the `reports` folder and under a file prefixed with `assignment_A_task_4` and ending with the appropriate file extension.
* Using any outputs from Task 3 above, create a brief one pager explaining implications, policy, cost, statistical or otherwise of how education impacts labor outcomes.
* If you could only measure a subset of variables in the file, which variables would you measure and why?