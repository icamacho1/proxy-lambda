# Description:
The following project is a proxy to be used in a AWS Lambda Function. The idea is to handle http requests from a web client to avoid CORS.

# Installation:
Once cloned, you will first need to link the .githooks folder:
```bash
cd proxy-lambda
ln -s $(pwd)/.githooks/commit-msg $(pwd)/.git/hooks/commit-msg
```
You will also need to use the serverless configuration resource.

To test and use the project locally you will need to work with a local environment.
* Create a virtual environment
```bash
python3 -m venv venv
```
* Upgrade pip to the highest version.
```bash
pip3 install --upgrade pip
```
* Install the required python modules:
```bash
pip3 install -r requirements.txt 
```
* Install the serverless-python-requirements in the project:
```bash
npm install serverless-python-requirements
```

# Working in the project:
Just need to work on the **src** directory. For every class or module created inside it, remmember to build the required tests.

# Documentation:
The built project works as an API.
* The allowed methods at the moment are: GET, POST, PATCH as they are the only ones I will be using in the project I built the proxy for.
* To make any successfull api call you need to pass the http values as a querystring as follows
    http://API_ENDPOINT?*url=*&*params=*&*headers=*&*cookies=*
* The values passed to each parameter must be base 64 encoded.
* The request method must be handled by the client in use.
* Payloads will be passed by the client.

![Tests](https://github.com/icamacho1/proxy-lambda/actions/workflows/main.yml/badge.svg)