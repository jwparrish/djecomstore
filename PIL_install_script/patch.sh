#!/bin/sh
# Ref: http://ubuntuforums.org/showthread.php?t=1751455
# Install required libs
yes | apt-get install build-essential python-dev libjpeg62-dev zlib1g-dev libfreetype6-dev liblcms1-dev
# Link to correct location
if [ -d /usr/lib/x86_64-linux-gnu ]; then
    # Ubuntu 11.04 64bit
    ln -sf /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/
    ln -sf /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/
    ln -sf /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/
elif [ -d /usr/lib/i386-linux-gnu ]; then
ln -sf /usr/lib/i386-linux-gnu/libfreetype.so /usr/lib/
    ln -sf /usr/lib/i386-linux-gnu/libz.so /usr/lib/
    ln -sf /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib/
fi
