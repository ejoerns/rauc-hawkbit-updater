import pytest
import sys, os, subprocess
import re

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/build"
os.environ["PATH"] = here + ":" + os.environ["PATH"]

@pytest.fixture
def hawkbit_running():
    pass

def run(command):
    proc = subprocess.Popen(command,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            )
    out,err = proc.communicate()
    return out, err, proc.returncode

def test_rauc_hawkbit_version():
    command = ["rauc-hawkbit-updater", "-v"]
    out, err, exitcode = run(command)
    assert exitcode == 0
    assert re.match(b'Version ?.?', out)
    assert err == b''

def test_rauc_hawkbit_invalid_arg():
    command = ["rauc-hawkbit-updater", "--invalidarg"]
    out, err, exitcode = run(command)
    assert exitcode == 1
    assert out == b''
    assert err == b'option parsing failed: Unknown option --invalidarg\n'

def test_rauc_hawkbit_no_config_file():
    command = ["rauc-hawkbit-updater"]
    out, err, exitcode = run(command)
    assert exitcode == 2
    assert out == b''
    assert err == b'No configuration file given\n'

def test_rauc_hawkbit_non_existing_config_file():
    command = ["rauc-hawkbit-updater", "-c", "does-not-exist.conf"]
    out, err, exitcode = run(command)
    assert exitcode == 3
    assert out == b''
    assert err == b'No such configuration file: does-not-exist.conf\n'
