# Defi Data Ops Sample

This is a sample repository demonstrating a data ops pipeline loading DefiLlama data into BigQuery using Meltano and self-hosted [Cube](https://cube.dev/) for data visualization, with configuration for deployment to [Render](https://render.com/)

- [Meltano Documentation](https://docs.meltano.com/getting-started/)

## Dependencies

- [Docker Engine](https://docs.docker.com/engine/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3
- [Pipx](https://github.com/pypa/pi)

## Getting Started

For help setting up VSCode with poetry and singer tap development, see [this thread](https://stackoverflow.com/questions/59882884/vscode-doesnt-show-poetry-virtualenvs-in-select-interpreter-option) and [this thread on configuring your python interpreter](https://stackoverflow.com/questions/66266640/pylancereportmissingmodulesource-error-in-vs-code-while-using-django)

For an introduction to Meltano, see [this video](https://www.youtube.com/watch?v=sL3RvXZOTvE)

```sh
# For local python development
pipx install meltano
pipx install poetry
```

## Developing

```sh
# Run containerized meltano instance
docker compose up
```

This will expose the Meltano ui on `localhost:5001` and mount `./meltano` as a shared volume so you can develop locally and run pipelines in a containerized environment.

Next, install meltano dependencies. The `meltano.sh` script is the same as running `meltano`, but it executes in the meltano docker container conext, targeting `/project/amo` by default.


You can then either use the UI, or `./meltano.sh` to run additional commands, such as:

```sh
# Run a custom tap you're actively developing, printing output to stdout
./meltano.sh invoke tap-defillama
# Add a new loader
./meltano.sh add loader target-bigquery
# Run a pipeline
./meltano.sh elt tap-testapi target-jsonl

# ...etc
```
