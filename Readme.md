# Image Upload to S3 Bucket using Boto3


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install project dependencies.

**Project Name: Image Upload**

This is a POC for, How to upload an image to S3 Bucket using Boto3.

---

**Project Setup**
1. Make a Python3.x virtual environment using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
Use the package manager  to install foobar.
2. ```git clone https://github.com/ongraphpythondev/image-upload-boto3.git```
3. ```cd image_upload```

4. ```pip install -r requirements.txt```

5. Configure the S3 bucket settings in settings.py
    * AWS_S3_HOST = ' '
    * AWS_ACCESS_KEY_ID = ' '
    * AWS_SECRET_ACCESS_KEY = ' '
    * AWS_STORAGE_BUCKET_NAME = ' '

5. ```python manage.py runserver```


Now you can access the server at localhost:8000



