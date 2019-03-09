FROM ubuntu:16.04
MAINTAINER Allyson Ramkissoon <allys-99.github.io>

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates  python3-pip && \
    apt-get install -y libxss1 desktop-file-utils xdg-utils and libgtk2.0-bin &&\
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    pip3 install numpy pandas

#RUN pip3 install numpy pandas

ENV PATH /opt/conda/bin:$PATH
RUN conda install -c plotly  plotly && \
    conda install -c plotly plotly-orca psutil && \
    conda install -c anaconda pandas && \
    conda install -c anaconda ipython-notebook && \
    conda install -c mw gtk2

ADD wine.py /
