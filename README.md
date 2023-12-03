# SENSI
Small Enterprise Network Security Infrastructure - Raspberry Pi 4 + Suricata + Telegram + Python VS The World


### NAME: SENSI - SMALL ENTERPRISE NETWORK SECURITY INFRASTRUCTURE

### BRIEF DESCRIPTION: 

Many SMEs in Malaysia hesitate to transition their businesses online, primarily due to concerns about cyber threats and a lack of budget or in-house expertise for establishing a cybersecurity foundation. However, by leveraging an affordable Raspberry Pi 4, employing Suricata IDPS, integrating Telegram, and utilizing custom Python 3 scripts, these businesses can develop a foundational Security Infrastructure. This approach can protect against common cybersecurity threats, potentially bolstering stakeholder confidence to expand their operations online.

**IMPORTANT: READ THE FULL DOCUMENTATION FOR MORE IN-DEPTH EXPLANATIONS AND PROCEEDURES**

### SYSTEM TYPE:

PORTABLE NETWORK INFRASTRUCTURE MODULE

### PRIMARY FUNCTION

The solution offers a fundamental level of network security by employing a Raspberry Pi and Suricata. It self-configures to align with the host network infrastructure using Python 3 scripts. Notifications and updates are efficiently delivered through the Telegram messaging platform, ensuring timely communication. The solution is catered towards non-technical users.

### PURPOSE & GOALS

#### Primary Goals:

1. This project's objective is to develop a Network Security system tailored to comply with Malaysian IT Security standards for Small-Medium Enterprises. The system will be built using open-source resources, facilitating unrestricted access and reducing the need for extensive specialized training. This approach enables businesses to safeguard their network infrastructure efficiently, avoiding the substantial costs often associated with proprietary security solutions.

2. To implement a variety of open-source security tools such as IDS (Intruder Detection Systems), IPS (Intruder Prevention Systems), and Telegram and custom python3 scripts on-to a unanimous platform.

3. To implement a notification mechanism for security operations through a phone number.



### FEATURES

1. The SENSI project involves significant customizations to the Raspberry Pi and its operating system to optimize it for hosting Suricata, a network security application. Key modifications include altering the boot process from an SD card to a 240GB SSD, greatly improving storage capacity and system speed. Additionally, the swap space in the Raspberry Pi OS has been expanded from 256MB to 12GB, effectively augmenting the total memory to 18GB. These enhancements collectively boost the Raspberry Pi's performance, making it more suitable for the demands of high-performance applications like Suricata.

2. Suricata serves as the core of the SENSI system's network threat detection capabilities. It is integrated into the customized Raspberry Pi system, initially set up in Network Intrusion Detection System (NIDS) mode to monitor and analyze network traffic. For full functionality as a Network Intrusion Detection & Prevention System (NIDPS), Suricata's configuration requires specific adjustments. In NIDPS mode, Suricata not only detects threats but also actively intervenes by sending alerts for potential threats and, if necessary, blocking harmful network traffic. This integration is crucial for effective detection and prevention of network threats, significantly enhancing the SENSI system's security effectiveness.

3. The SENSI system incorporates the Telegram API to swiftly alert system administrators of potential threats detected by Suricata. This integration is achieved through a custom Telegram Bot, named PeachPatrolbot, which is set up to interact automatically with a dedicated Telegram group, acting as the main channel for security alerts. By using the bot's token and the group's chat ID, the SENSI system automates the dispatch of real-time notifications to administrators' mobile devices. This feature significantly enhances the system's responsiveness and allows administrators to take prompt action against security threats.

4. In the SENSI system, Python3 scripts play a crucial role in automating essential functions, significantly improving the system's efficiency and reducing the need for manual operations. These scripts are primarily responsible for two functions: sending Suricata alerts to the Telegram platform and simplifying the process of updating system configurations. By automating these tasks, the SENSI system becomes more accessible and user-friendly, especially for those without advanced technical expertise. This automation is key to maintaining the system's effectiveness in network threat detection and enhances its overall functionality.

5. The SENSI system emphasizes user-friendliness in system configuration by incorporating Bash scripts, making the setup process accessible to users regardless of their technical background. Bash, known for its efficiency in automating and sequencing tasks, is used within SENSI to simplify and streamline the configuration process. This approach allows even users with limited technical knowledge to easily configure and update the system, facilitating efficient deployment and ongoing management. The use of Bash scripts ensures that the system remains adaptable and user-friendly, broadening its accessibility to a wider range of users and making network threat detection and management more manageable.


### HIGH LEVEL ARCHITECTURE

#### KEY COMPONENETS

- **Raspberry Pi 4 Model B (8GB)**: Act as the brains of the system, running Raspberry Pi OS (Raspbian) and offer I/O needed for IDPS functionality.

* Suricata for network IDS & IPS.

- Telegram-based threat notification system.

- Python 3 scripts for automation.

- BASH script for management menu.


##### Hardware Specifications:

![image](https://github.com/syst3m5bul1y/SENSI/assets/100330775/36f21047-0c7e-4e0d-a0d4-e0e0937a71ff)


- Raspberry Pi 4 Model B (8GB)

- ALFA AWUS036NHA wireless network adapter.

- Kingston A400 240GB 2.5 SATA III SSD.

- UGreen High Speed USB-SATA III converter.


#### OPERATING SYSTEM AND SERVICES

![SENSI System Architecture](https://github.com/syst3m5bul1y/SENSI/assets/100330775/158e47e8-7920-4cd7-bc4a-d55c5c771722)



- **Raspbian OS:** Chosen for its ease of use, compatibility and strong community support. It will contain all processes within the SENSI system.

- **Suricata**: NIDPS; was the second choice. Snort (primary option) had logging issues (failed to log in unified2). Suricata was configured to log in fast.log.

- **Telegram API**: Home-made API for Telegram instant messaging - made using a dedicated Telegram-Bot, python 3 script. Offers real-time threat notifications. 

- **configurator.py:** A python script that automates some configurations at `suricata.yaml` to personalize Suricata to the host network.

- **SENSI_mgmt:** A bash script that could be used to manage the entire system, from updating the OS to turning the notification system ON. 
	- This exists to allow the user to be technologically-naive and still operate and conduct basic maintenance of the system.

- **peachpatrol.py:** Contains the home-grown Telegram API, log reading mechanism and log forwarding mechanism for the Telegram instant messages. 
	- The Telegram API to function properly, the following needs to be replaced with the user's specific Telegram details:
		- `self.chat_id = "CHAT-ID-HERE"`
		- `self.bot_token = "BOT-TOKEN-HERE"`
    
		![Screenshot 2023-12-03 184833](https://github.com/syst3m5bul1y/SENSI/assets/100330775/c83c08df-c65d-4af8-b757-3ebd2d5f016c)

	


### NETWORK INTEGRATION

#### Recommended Network Architecture for SENSI Deployment

![Screenshot 2023-12-03 192102](https://github.com/syst3m5bul1y/SENSI/assets/100330775/3e1a01cc-a3c8-4b01-ac17-2827d54ca053)


  
The network architecture featuring SENSI provides comprehensive monitoring of all inbound and outbound traffic, enhancing threat detection. The architecture starts with a router, which manages data flow between the local network and the internet. Next, a firewall acts as the initial defense, filtering traffic based on security rules. If a firewall isn't present, SENSI is positioned between the router and the switch, although including a firewall is highly recommended for enhanced security.

SENSI, placed behind the firewall (or router if no firewall exists), inspects all network traffic using Suricata IPS to identify any anomalies or threats. This adds a sophisticated layer of security to the network. Finally, traffic passes through a switch, distributing it within the internal network. This layout ensures SENSI scrutinizes all network traffic, providing a robust security solution.


#### Alternative Architecture via Managed Switch

![Screenshot 2023-12-03 210201](https://github.com/syst3m5bul1y/SENSI/assets/100330775/6f5c53e9-8811-4ef2-b39f-c7d2371369b5)



#### Alternative Architecture via Network Tap

![Screenshot 2023-12-03 210324](https://github.com/syst3m5bul1y/SENSI/assets/100330775/f9f32884-6e76-47cb-b4d6-df30f111529c)


