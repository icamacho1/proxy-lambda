# Description:
The following project is a proxy to be used in a AWS Lambda Function. The idea is to handle http requests from a web client to avoid CORS.

# Installation:
Once cloned, you will first need to link the .githooks folder:
```bash
cd proxy-lambda
ln -s $(pwd)/.githooks/commit-msg $(pwd)/.git/hooks/commit-msg
```

# TODO:
* Finish the unit-tests to secure a stable API
* Learn how to use Cloud Formation to deploy the whole infrastructure to AWS from a single command.
* Set all the hooks neccesary to build a pipeline that will automatically deploy the project to AWS.
