#!/usr/bin/env bash
#

set -e

linkdir=defs

if [ ! -e "$linkdir" ];
then

    echo "Library path is broken.  Relinking..."
    rm -f "$linkdir"
    apidir=`find ~/Library/Application\ Support/Autodesk/webdeploy/production -name "_fusion.so" -depth 6 -exec dirname {} \;`

    ln -s "$apidir/defs" $linkdir
fi

echo "Library path: $(readlink $linkdir)"
