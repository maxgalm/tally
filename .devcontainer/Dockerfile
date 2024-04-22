FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Europe/Berlin \
    LANG=C.UTF-8

RUN echo ${TZ} > /etc/timezone \
    && apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    && rm /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

RUN apt-get install -y --no-install-recommends \
    bash \
    curl \
    direnv \
    gawk \
    git \
    jq \
    python3 \
    python3-pip \
    sudo \
    unzip \
    wget \
    zip \
    zsh \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip --no-cache-dir install --upgrade pip && \
    pip3 install --no-cache-dir \
    black==23.11.0 \
    django==5.0.4 \
    isort==5.12.0 \
    flask==3.0.0 \
    pipdeptree==2.2.1 \
    pipenv==2022.7.4 \
    pymongo==4.6.0 \
    regex==2023.10.3 \
    ruff==0.1.6 \
    pre-commit==3.5.0 \
    yamllint==1.33.0 \
    && pipdeptree -w fail

ARG DOCKER_USER=dockeruser
ARG DOCKER_UID=1000
ARG DOCKER_GID=${DOCKER_UID}
ENV XDG_CACHE_HOME="/home/${DOCKER_USER}/.cache" \
    XDG_CONFIG_HOME="/home/${DOCKER_USER}/.config" \
    XDG_DATA_HOME="/home/${DOCKER_USER}/.local/share"

RUN groupadd --gid ${DOCKER_GID} ${DOCKER_USER} && \
    useradd -s /bin/bash --uid ${DOCKER_UID} --gid ${DOCKER_GID} -m ${DOCKER_USER} && \
    echo ${DOCKER_USER} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${DOCKER_USER}

USER ${DOCKER_USER}

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" \
    && git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "/home/${DOCKER_USER}/powerlevel10k" \
    && git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git "/home/${DOCKER_USER}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting" \
    && git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions.git "/home/${DOCKER_USER}/.oh-my-zsh/custom/plugins/zsh-autosuggestions" \
    && "/home/${DOCKER_USER}/powerlevel10k/gitstatus/install"

USER root

COPY configurations/.bashrc \
     configurations/.zshrc \
     configurations/.p10k.zsh \
     /home/${DOCKER_USER}

COPY configurations/git-prompt.sh /home/${DOCKER_USER}/.scripts

# create user dirs and set permissions
RUN mkdir -p \
    /home/${DOCKER_USER}/.vscode-server/extensions \
    ${XDG_CACHE_HOME} \
    ${XDG_CONFIG_HOME} \
    ${XDG_DATA_HOME} \
    && chown -R ${DOCKER_USER}:${DOCKER_USER} /home/${DOCKER_USER}

ARG USERNAME
ARG UID=1001
ARG GID=1001
USER root
RUN groupadd -g ${UID} docker && \
    usermod -u ${UID} -l ${USERNAME} -a -G docker -s /bin/zsh dockeruser && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL >/etc/sudoers.d/$USERNAME && \
    chown -R $UID:$GID /home/dockeruser
USER $USERNAME
