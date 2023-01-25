"""REST client handling, including DefiLllamaStream base class."""

import requests
from pathlib import Path
from typing import Any, Optional
try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable


from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


SCHEMAS_DIR = Path(__file__).parent / Path("../schemas")


class YieldsClient(RESTStream):
    """YieldsClient stream class."""

    current_index = 0
    pools = []
    records_jsonpath = "$.data[*]"  # Or override `parse_response`.

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        r = requests.get(self.config["api_url"] + "/pools")
        self.pools = r.json()["data"]

    def get_url(self, dict) -> str:
        url = "".join([self.url_base, self.path or "", "/", self.pools[self.current_index]["pool"]])
        return url

    @property
    def url_base(self) -> str:
        return self.config["api_url"]

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

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        if self.current_index + 1 >= len(self.pools):
            return None
        pool = self.pools[self.current_index]["pool"]
        self.current_index += 1
        return pool

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records."""
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        if self.current_index > len(self.pools):
            return row
        """As needed, append or transform raw data to match expected structure."""
        row["id"] = self.pools[self.current_index]["pool"] + "-" + row["timestamp"]
        row["pool"] = self.pools[self.current_index]["pool"]
        row["chain"] = self.pools[self.current_index]["chain"]
        row["project"] = self.pools[self.current_index]["project"]
        row["symbol"] = self.pools[self.current_index]["symbol"]
        return row
