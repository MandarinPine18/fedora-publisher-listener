# Fedora Messaging Publisher and Listener

## Overview

These are two simple scripts to utilize Fedora Messaging with a locally hosted RabbitMQ server. There is a publish script and a listen script.

## Installation

Please refer to https://fedora-messaging.readthedocs.io/en/stable/tutorial/installation.html for instructions on the installation of fedora-messaging. After installing RabbitMQ, return to this file.

(optional) if you would like the browser interface of RabbitMQ, run the following command. It is not necessary, but may be useful to monitor the system.
```sh
  $ rabbitmq-plugins enable rabbitmq_management
```

Change the directory of your terminal where you would like this repository cloned. Replace "/this/is/a/path" with the desired path. Clone the repository and cd into it.
```sh
    cd /this/is/a/path
    git clone https://github.com/ethanparab/fedora-publisher-listener.git
    cd fedora-publisher-listener
```

Included is a configuration file. Copy it to the directory /etc/fedora-messaging/. Alternatively, you can place this file anywhere or not move it if you set the environment variable FEDORA_MESSAGING_CONF to the path to the file.
```sh
  $ mkdir /etc/fedora-messaging
  $ cp config.toml /etc/fedora-messaging/config.toml
```

## Usage

Enter the repository directory and run the listener.
```sh
    cd /this/is/a/path/fedora-publisher-listener
    python3 -m consume.py
```

In a new terminal window, enter the same directory and run the publisher.
```sh
    cd /this/is/a/path/fedora-publisher-listener
    python3 -m publish.py
```

Included is an mp4 video showing the sctipts and RabbitMQ in action.

## Credits

To use these scripts, code from Fedora was used. In addition, the official documentation was followed.

## License

This is licensed under GNU AGPL v3. This is included in the file titled LICENSE.
