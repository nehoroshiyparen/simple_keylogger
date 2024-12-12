#!/bin/bash

install_mac() {
    if ! command -v python3 &> /dev/null
    then 
        if ! command -v brew &> /dev/null
        then 
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi

        brew install python
    fi

    if ! python3 -m pip &> /dev/null
    then
        python3 -m unsurepip --upgrade
    fi

    python3 -m pip install pynput
}

install_linux() {
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip

    pip3 install pynput
}

install_windows() {
    if ! command -v choco &> /dev/null
    then 
        powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; \
            [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; \
            iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    fi

    choco install python -y

    python -m pip install pynput
}

OS="$(uname -s)"
case "${OS}" in
    Darwin*) install_mac ;;
    Linus*) install_linux ;;
    CYGWIN*|MINGW*|MSYS*) install_windows;;
    *)
        exit 1
        ;;
esac


if [[ "$OS" == *MINGW* || "$OS" == *CYGWIN* || "$OS" == MSYS ]]; then
    pythonw client.py
else
    python3 client.py || python client.py
fi