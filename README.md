# Overview
An example to use Terraform to create an AWS Lambda function with an API gateway.

## Instructions

1. Create a `requirements.txt` file from pipenv

```bash
pipenv requirements > requirements.txt
```

2. Install the requests library to a new package directory.

```bash
pip install --target ./infrastructure/package -r requirements.txt
```

3. Create a deployment package with the installed library at the root.

```bash
cd infrastructure/package
zip -r ../my-deployment-package.zip .
```

4. Add the `main.py` file to the root of the zip file.

```bash
cd ..
zip my-deployment-package.zip main.py
```
5. Initialize Terraform

```bash
terraform init
```

6. Plan Terraform

```bash
terraform plan
```