FROM ghcr.io/sloretz/ros:humble-desktop-full

# Avoid warnings by switching to noninteractive for the build process
ENV DEBIAN_FRONTEND=noninteractive

ENV USER=root

# Install XFCE, VNC server, dbus-x11, and xfonts-base
RUN apt-get update && apt-get install -y --no-install-recommends \
    xfce4 \
    xfce4-goodies \
    tightvncserver \
    dbus-x11 \
    xfonts-base \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
#
RUN apt-get update \
    && apt-get install -y \
    nano \
    vim \
    && rm -rf /var/lib/apt/lists/*

#
ARG USERNAME=ros-humble
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
  && mkdir /home/$USERNAME/.config && chown $USER_UID:$USER_GID /home/$USERNAME/.config

#
RUN apt-get update \
  && apt-get install -y sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
  && chmod 0440 /etc/sudoers.d/$USERNAME \
  && rm -rf /var/lib/apt/lists/*
#
COPY entrypoint.sh /entrypoint.sh
COPY bashrc /home/${USERNAME}/.bashrc

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["bash"]

# Setup VNC server
RUN mkdir /root/.vnc \
    && echo "password" | vncpasswd -f > /root/.vnc/passwd \
    && chmod 600 /root/.vnc/passwd

# Create an .Xauthority file
RUN touch /root/.Xauthority

# Set display resolution (change as needed)
ENV RESOLUTION=1920x1080

# Expose VNC port
EXPOSE 5901

# Set the working directory in the container
WORKDIR /app

# Copy a script to start the VNC server
COPY start-vnc.sh start-vnc.sh
RUN chmod +x start-vnc.sh

# List the contents of the /app directory
RUN ls -a /app