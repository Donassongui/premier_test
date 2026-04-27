name: "Docker Build"

on:
  workflow_dispatch:
    inputs:
      service:
        description: "Quel service builder ?"
        required: true
        type: choice
        options:
          - api
          - worker
          - frontend
      tag:
        description: "Tag de l'image (ex: 1.0.0)"
        required: false
        default: "latest"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Login Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build & Push
        uses: docker/build-push-action@v5
        with:
          context: ./services/${{ inputs.service }}   # ← dossier du service choisi
          push: true
          tags: monuser/${{ inputs.service }}:${{ inputs.tag }}
