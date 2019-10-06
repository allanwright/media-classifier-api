## Introduction
Media-Classifier-Api is an azure functions app providing model prediction for [Media-Classifier](https://github.com/allanwright/media-classifier) trained models.

## Status
![Github Actions Badge](https://github.com/allanwright/media-classifier-api/workflows/azure%20functions/badge.svg)

Media-Classifier-Api is automatically deployed to azure functions when code is pushed to master.

## Usage
The api is deployed at [https://media-classifier-api.azurewebsites.net](https://media-classifier-api.azurewebsites.net) and at present is subject to constant breaking changes.  The following call is currently supported:

* **GET api/classify** - Accepts a *name* query string parameter, eg:
`https://media-classifier-api.azurewebsites.net/api/classify?name=Dark%20s01e01.mp4`