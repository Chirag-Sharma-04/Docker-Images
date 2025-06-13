FROM arm64v8/ros:melodic


# Example of installing programs
RUN apt-get update \
    && apt-get install -y \
    nano \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y \
    ros-melodic-roscpp-tutorials \
    ros-melodic-rviz 

CMD ["bash"]