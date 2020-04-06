#!/bin/bash

PACKAGE_NAME=openvpn_icon
VERSION=0.1.0

fpm \
    -s dir \
    -t deb \
    -n ${PACKAGE_NAME} \
    -v ${VERSION} \
    --iteration $(date +%s) \
    --description 'Simple icon for vpn control' \
    --maintainer 'Raphael Carmona-Hagelsteen <uncorporation@gmail.com>' \
    openvpn_icon.py=/bin/openvpn_icon \
    openvpn_icon.desktop=/usr/share/applications/openvpn_icon.desktop 
