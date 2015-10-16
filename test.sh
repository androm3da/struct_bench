#!/bin/bash

set -euo pipefail

PYTHONS="python3 python2 pypy"

for PY in $PYTHONS
do
    $PY --version
    $PY types_c_def.py # build the c_struct extension
    $PY types_c.py # test that the FFI works for this interp
    $PY comparison.py | sort
done
