#!/bin/sh

exec docker compose exec meltano meltano "$@"
