# Image Upload to S3 Bucket using Boto3


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install project dependencies.

**Project Name: Image Upload**

This is a POC for, How to upload an image to S3 Bucket using Boto3.

---

**Project Setup**
1. Make a Python3.x virtual environment using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
Use the package manager  to install foobar.
2. ```cd e-learning```
3. ```pip install -r requirements/dev.txt```
4. Configure .env file with required credentials. (Take help from .env.example file)

4. To run the celery Server

    ```celery -A e_learning  worker -l info```
5. To run the flower to check status of celery
   
   ```celery -A e_learning flower```   (Optional) 

7. ```python manage.py runserver```


Now you can access the server at localhost:8000


API Doc Link: [Click Here](https://docs.google.com/document/d/1BmbiwA2dfqbhpu5e6tYdlr4CiSnFUTfn3mIDhIkfAeA/edit)

User Roles Description: [Click Here](https://docs.google.com/document/d/1Oa7kxCy_Ob90oIxWwEETIHapMGV_mRswFq0P905bXKo/edit)

AWS Live Video Setup: [Click Here](https://docs.google.com/document/d/1qQfNUZVfZtAavHBkCJ05yTD8nq5qiIle5B5t7Tv4n0k/edit)