import boto3
import progressbar
from pathlib import Path
from yaml import safe_load as load
with open("config.yaml") as obj:
    config = load(obj)

# todo: add nifty progress bar
# see: https://stackoverflow.com/questions/41827963/track-download-progress-of-s3-file-using-boto3-and-callbacks

s3 = boto3.client('s3', region_name="us-east-2")

def get_bucket_name(config=config):
    return config['s3']['bucket']

def get_external_data_config(key="external_data", config=config):
    return config[key]

def download_from_s3_and_save(s3_obj=s3,
                              file_path="./data/external/",
                              file_name=None):
    file_name = Path(file_name)
    save_to_path = Path(file_path)
    save_to_path.mkdir(
        parents=True,
        exist_ok=True
    )

    s3.download_file(get_bucket_name(),
                     str(file_name),
                     str(save_to_path/file_name))

def download_reference_and_save(references=None):
    external_config = get_external_data_config(key="references")
    for reference in references:
        download_from_s3_and_save(file_name=external_config[reference],
                                  file_path="./references/")    

def download_external_data_and_save(dataset=None):
    external_config = get_external_data_config()
    download_from_s3_and_save(file_name=external_config[dataset])

print("\t ... about to download several files, this may take a moment...")
download_external_data_and_save("adult_training_and_education")
download_reference_and_save(references=["ates_variables", "ates_codebook"])
print("\t successfully downloaded the files!")