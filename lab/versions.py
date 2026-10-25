"""Version helpers, built on packaging."""

from packaging.version import LegacyVersion, parse


def is_legacy_version(spec: str) -> bool:
    """True when `spec` is not a PEP 440 version."""
    return isinstance(parse(spec), LegacyVersion)


def normalise(spec: str) -> str:
    return str(parse(spec))
