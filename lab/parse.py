"""Parses a CSV-ish row."""


def parse_row(line: str) -> dict[str, str]:
    """Split `key=value,key=value` into a dict."""
    fields: dict[str, str] = {}
    for part in line.split(","):
        key, _, value = part.partition("=")
        fields[key.strip()] = value.strip()
    return fields
