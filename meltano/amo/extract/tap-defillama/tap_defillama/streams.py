"""Stream type classes for tap-defillama."""

from pathlib import Path


from tap_defillama.clients.pool import PoolClient
from tap_defillama.clients.yields import YieldsClient

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class PoolStream(PoolClient):
    """Define custom stream."""
    name = "pool"
    path = "/pools"
    primary_keys = ["pool"]
    replication_key = None
    records_jsonpath = "$.data[*]"

    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema_filepath = SCHEMAS_DIR / "pool.json"


class YieldStream(YieldsClient):
    """Define custom stream."""
    name = "yield"
    path = "/chart"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.data[*]"

    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "yield.json"
