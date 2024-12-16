# Use the ARM64v8 Ubuntu base image for compatibility with M1 Macs
FROM arm64v8/ubuntu:20.04

# Prevent interactive prompts like the one for timezone selection
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages for the desktop environment and VNC server
RUN apt-get update && \
    apt-get install -y xfce4 xfce4-goodies tightvncserver dbus-x11 x11-xserver-utils && \
    apt-get clean

# Set VNC password (change 'yourpassword' to your actual password)
RUN mkdir -p ~/.vnc && \
    echo "yourpassword" | vncpasswd -f > ~/.vnc/passwd && \
    chmod 600 ~/.vnc/passwd

# Create a script to start the VNC server and the XFCE desktop environment
RUN echo '#!/bin/bash\n\
xrdb $HOME/.Xresources\n\
startxfce4 &\n\
tightvncserver -fg :1 -geometry 1280x800 -depth 24' > /usr/local/bin/start-vnc.sh && \
    chmod +x /usr/local/bin/start-vnc.sh

# Expose the VNC port (5901)
EXPOSE 5901

# Set the entrypoint to the VNC start script
CMD ["/usr/local/bin/start-vnc.sh"]
