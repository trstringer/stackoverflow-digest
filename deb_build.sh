#!/bin/bash

VERSION=$(python3 -c "from sodigest.version import VERSION; print(VERSION, end='')")

echo "$(date) - Building version $VERSION"
dch --newversion "$VERSION"

debuild
