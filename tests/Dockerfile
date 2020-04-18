FROM ubuntu:18.04

ENV LANG C.UTF-8

RUN apt-get update && apt-get install --no-install-recommends -y \
    gir1.2-gtk-3.0 \
    python3 \
    python3-gi \
    python3-gi-cairo \
    xauth \
    xvfb \
    openvpn

RUN dpkg -i /shared/openvpn-icon_0.1.0.deb && apt install -f

RUN cd /shared && openvpn-icon myconf.ovpn


