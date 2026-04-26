#!/bin/bash

set -e

virtualenv --without-pip virtualenv
pip install --target virtualenv/lib/python3.13/site-packages