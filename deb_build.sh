#!/bin/bash

set -e

VERSION=$(python3 -c "from sodigest.version import VERSION; print(VERSION, end='')")

echo "$(date) - Building version $VERSION"
dch --newversion "$VERSION" "New release"
dch --release bionic

debuild -i -us -uc -S

echo "$(date) - Making dist dir"
mkdir -p dist

echo "$(date) - Copying artifacts to dist"
cp "../stackoverflow-digest_$VERSION"* dist/
