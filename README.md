## Introduction
Media-Classifier-Api is an azure functions app providing model prediction for [Media-Classifier](https://github.com/allanwright/media-classifier) trained models.

## Status
[![Github Actions Badge](https://github.com/allanwright/media-classifier-api/actions/workflows/main.yml/badge.svg)](https://github.com/allanwright/media-classifier-api/actions/workflows/main.yml)

Media-Classifier-Api was automatically deployed to azure functions when code is pushed to master.

## Usage
The api was deployed to [https://media-classifier-api.azurewebsites.net](https://media-classifier-api.azurewebsites.net). A single GraphQL endpoint existed at [api/gql](https://media-classifier-api.azurewebsites.net) and implemented the following schema:

```graphql
type Label {
    id: Int!,
    name: String!
}

type Classification {
    label: Label!,
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
    labels: [Label]
    media(name: String!): Media
}
```
