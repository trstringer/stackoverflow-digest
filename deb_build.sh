#!/bin/bash

VERSION=$(python3 -c "from sodigest.version import VERSION; print(VERSION, end='')")

echo "$(date) - Building version $VERSION"
dch --release bionic --newversion "$VERSION" ""

debuild -i -us -uc -S
