from pathlib import Path

from pytest import fixture

from constants import CONFIGURATION_FILE

@fixture
def configuration(request):
    """Support test setup and teardown.

       Setup
       -----
       Create test configuration file,
       passing in YAML via @mark.parametrize.

       Teardown
       --------
       Delete test configuration file."""

    # Setup

    yaml = request.param

    path = Path(CONFIGURATION_FILE)

    with path.open("w") as writer:
        writer.write(yaml)

    yield

    # Teardown

    path.unlink()
