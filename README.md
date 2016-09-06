# Python Client library for OpenTMI

This library purpose is to provide simple interface for OpenTMI -backend.
For example this can fetch existing test case meta information from OpenTMI and upload results to it.

## installation

`python setup.py install`

## Command Line Interface

Purpose is to provide simple Command line Interface to communicate with OpenTMI -backend

```
/> opentmi --help
usage: opentmi [-h] [--version VERSION] [--host HOST] [-p PORT] [--list LIST]
               [--testcases TESTCASES]

optional arguments:
  -h, --help            show this help message and exit
  --version VERSION     Prints package version and exits
  --host HOST           OpenTMI host, default: localhost
  -p PORT, --port PORT  OpenTMI port
  --list LIST           List something
  --testcases TESTCASES
```

example:
```
opentmi --host localhost --port 3000 --list --testcases 1
```

## Python API

```
from opentmi_client.opentmi_client import OpenTmiClient
client = OpenTmiClient(host='127.0.0.1', port=3000) # defaults
campaigns = client.get_campaigns()
testcases = client.get_testcases()
result = {
  "tcid": "test-case",
  "campaign": "my-campaign",
  "exec": { 
    "verdict": "pass",
    "duration": "8",
  },
  "sut": {
    "gitUrl": "github.com/opentmi/opentmi",
    "commitId": "123",
  },
  "dut": {
    "type": "hw",
    "vendor": "ABC",
    "model": "platform#1",
    "sn": "123"
  }
}
client.upload_results(result) # require valid result json object, 
                              # alternative you can set result_converter for OpenTmiClient constructor.
                              # converter function will be used to convert application specific result object for opentmi suitable format. 
```

Suitable result schema is described [here](https://github.com/OpenTMI/opentmi/blob/master/app/models/results.js#L15).


LICENSE: GPLv3
