## Introduction
Media-Classifier-Api is an azure functions app providing model prediction for [Media-Classifier](https://github.com/allanwright/media-classifier) trained models.

## Status
![Github Actions Badge](https://github.com/allanwright/media-classifier-api/workflows/azure%20functions/badge.svg)

Media-Classifier-Api is automatically deployed to azure functions when code is pushed to master.

## Usage
The api is deployed to [https://media-classifier-api.azurewebsites.net](https://media-classifier-api.azurewebsites.net). At present, a single GraphQL endpoint exists at [api/gql](https://media-classifier-api.azurewebsites.net) and implements the following schema:

```graphql
type Class {
    id: Int!,
    name: String!
}

type Classification {
    class: Class!,
    confidence: float!
}

type Entity {
    type: String!,
    value: String!
}

type Media {
    name: String!,
    classification: Classification!,
    entities: [Entity]
}

type Query {
    classes: [Class]
    media(name: String!): Media
}
```