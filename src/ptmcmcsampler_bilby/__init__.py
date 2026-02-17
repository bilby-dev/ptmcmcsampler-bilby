"""Interface and plugin for using PTCMCMSampler in bilby."""

from importlib.metadata import PackageNotFoundError, version

from .sampler import PTMCMCSampler

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"


__all__ = ["PTMCMCSampler"]
