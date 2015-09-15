# Flickr Fetch

This script grabs some basic information about photos in a
Flickr album and saves a json file with that information into
an S3 bucket.

## Usage

Sign up for a [Flickr API](https://www.flickr.com/services/api/) key.

Sign up for [AWS](https://aws.amazon.com).

Create an S3 bucket.

Use IAM to create an AWS user.

Set up your AWS credentials and config (I used
[AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)).

Install the requirements (preferably from within a virtualenv):

    pip install -r requirements.txt


Make a copy of `fetch_config_sample.py` and name it `fetch_config.py`.

Edit `fetch_config.py` to match your needs.

**Caution:** The `fetch_config.py` file contains secrets. Do NOT make it public.
The file is already included in `.gitignore` but **be careful**.

With configuration in place, run the script when you want to update the file in your
S3 bucket with information from Flickr.
