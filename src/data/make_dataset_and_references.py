import requests
import progressbar
from pathlib import Path
from yaml import safe_load as load
with open("config.yaml") as obj:
    config = load(obj)

# todo: add nifty progress bar
# see: https://stackoverflow.com/questions/41827963/track-download-progress-of-s3-file-using-boto3-and-callbacks

def get_bucket_name(config=config):
    return config['s3']['bucket']

def get_external_data_config(key="external_data", config=config):
    return config[key]

def download_from_s3_and_save(config=config,
                              file_path="./data/external/",
                              file_name=None):
    file_name = Path(file_name)
    save_to_path = Path(file_path)
    save_to_path.mkdir(
        parents=True,
        exist_ok=True
    )

    s3 = config['s3']
    fetch_data_from =\
        s3['scheme']\
        + '.'.join([s3['bucket'],
                    s3['region'],
                    s3['domain']])\
        + "/"\
        + str(file_name)

    print("\t downloading from {}".format(fetch_data_from))

    with requests.get(url=fetch_data_from) as obj:
        open(str(save_to_path/file_name), "wb").write(obj.content)

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