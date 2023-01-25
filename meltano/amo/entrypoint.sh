#!/bin/sh

# Create local gcp credentials from base64 env var
echo $GOOGLE_CREDENTIALS | base64 --decode > client_secrets.json

export MELTANO_DATABASE_URI=postgresql://$DB_USER:$DB_PASS@$DB_HOST:$DB_PORT/$DB_DB

exec meltano "$@"
