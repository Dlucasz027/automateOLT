# OLTs (Optical Line Terminals)

OLTs (Optical Line Terminals) are essential devices in fiber optic networks, commonly used in GPON (Gigabit Passive Optical Network) systems. They are located at the central office and are responsible for managing communication between the fiber optic backbone and end users.

In other words, the OLT connects the high-capacity core network to the customers' ONUs (Optical Network Units). It controls, manages, and distributes network traffic, delivering internet, TV, and voice services.

OLTs are fundamental for high-speed, high-capacity communication networks, ensuring service efficiency, stability, and reliability.

---

# Connecting to an OLT Using Telnet and SSH

## Telnet

Telnet is a communication protocol that allows remote access to devices, such as OLTs, through a command-line interface.
To connect to an OLT via Telnet, you must use a terminal application (such as PuTTY or a Linux terminal), provide the OLT IP address, and authenticate with the configured username and password.

Basic command:

```
telnet [OLT_IP]
```

Default port: **23**

---

## SSH

SSH (Secure Shell) is a more secure version of Telnet because it encrypts data during communication.

SSH is preferred in most environments, especially corporate networks, due to its higher level of security. To connect via SSH, the OLT must have SSH enabled, and you must provide the correct IP address and authentication credentials.

Basic command:

```
ssh [username]@[OLT_IP]
```

Default port: **22**

---

Both Telnet and SSH are important for remote OLT management, allowing administrators to configure, monitor, and maintain the network efficiently.

However, SSH is strongly recommended in critical or production environments due to its encryption and enhanced security.

---

# Project Purpose

The purpose of this project is to simplify the process of configuring an OLT (Optical Line Terminal) from scratch.

It provides a clear and practical guide for performing both initial and advanced configurations, making the workflow more efficient and accessible — especially during the installation and setup of new units.

With ready-to-use commands and well-defined steps, the project helps reduce configuration errors and speeds up deployment.

When configuring models such as **ZTE C300, C320, or C350**, this project serves as a structured and reliable reference to complete the setup process smoothly and with greater confidence.