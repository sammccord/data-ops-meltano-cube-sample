"""REST client handling, including DefiLllamaStream base class."""

import requests
from pathlib import Path
from typing import Optional
try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable


from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


SCHEMAS_DIR = Path(__file__).parent / Path("../schemas")


class PoolClient(RESTStream):
    """PoolClient stream class."""

    # OR use a dynamic url_base:
    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]

    records_jsonpath = "$.data[*]"  # Or override `parse_response`.

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")
        return headers

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records."""
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        pool = {**row}
        if "predictions" in pool:
            pool["predictedClass"] = row["predictions"]["predictedClass"]
            pool["predictedProbability"] = row["predictions"]["predictedProbability"]
            pool["binnedConfidence"] = row["predictions"]["binnedConfidence"]
            del pool["predictions"]
        return pool
