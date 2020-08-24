import pytest
import sys, os, subprocess
import re
import logging

import hawkbit
from hawkbit import HawkbitTestClient
from hawkbit import HawkbitError

from tempfile import NamedTemporaryFile

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/build"
os.environ["PATH"] = here + ":" + os.environ["PATH"]

@pytest.fixture(scope="session")
def hawkbit_configured():
    hawkbit = HawkbitTestClient("localhost", "8080", username="admin", password="admin")

    filename_a = os.path.dirname(os.path.abspath(__file__)) + "/dummy-bundle.raucb"

    # Set config parameters
    hawkbit.set_config("pollingTime", "00:00:30")
    hawkbit.set_config("pollingOverdueTime", "00:03:00")
    
    # Add expected target
    hawkbit.add_target("test-controller", "bhVahL1Il1shie2aj2poojeChee6ahShu")

    # Create modules with artifacts
    module_id_a = hawkbit.add_swmodule('Test module')
    hawkbit.add_artifact(module_id_a, filename_a)

    # Create distributions of it
    dist_id = hawkbit.add_distributionset(module_id_a, name="Poky-Test")
    logging.info("Added demo distributions")

    hawkbit.assign_target(dist_id, "test-controller")

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

def test_rauc_hawkbit_register_and_check_valid_auth(hawkbit_configured):
    with NamedTemporaryFile(mode="w", delete=False) as tmp_source:
        with open("test-config.conf") as source:
            for line in source.readlines():
                tmp_source.write(re.sub(r'TEST_TOKEN', r'bhVahL1Il1shie2aj2poojeChee6ahShu', line))
    command = ["rauc-hawkbit-updater", "-c", tmp_source.name, "-r"]
    print(command)
    out, err, exitcode = run(command)
    assert exitcode == 0
    assert re.match(b'MESSAGE: Checking for new software....*', out)
    assert err == b''

def test_rauc_hawkbit_register_and_check_invalid_auth(hawkbit_configured):
    with NamedTemporaryFile(mode="w", delete=False) as tmp_source:
        with open("test-config.conf") as source:
            for line in source.readlines():
                tmp_source.write(re.sub(r'TEST_TOKEN', r'ahVahL1Il1shie2aj2poojeChee6ahShu', line))
    command = ["rauc-hawkbit-updater", "-c", tmp_source.name, "-r"]
    print(command)
    out, err, exitcode = run(command)
    assert exitcode == 1
    assert re.match(b'MESSAGE: Checking for new software....*', out)
    assert err == b'CRITICAL: Failed to authenticate. Check if auth_token is correct?\n'
