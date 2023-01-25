"""DefiLllama tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_defillama.streams import (
    PoolStream,
    YieldStream,
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    PoolStream,
    YieldStream
]


class TapDefiLllama(Tap):
    """DefiLllama tap class."""
    name = "tap-defillama"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_url",
            th.StringType,
            default="https://yields.llama.fi",
            description="The url for the Defi LLama service"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapDefiLllama.cli()
