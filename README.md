
# EVE-NG Network Automation with Ansible

This repository contains **network automation playbooks** for EVE-NG lab environments using **Ansible**. It is designed to help network engineers, students, and automation enthusiasts configure, backup, and verify network devices safely and efficiently.  

---

## **Project Purpose**

Modern networks are complex, and manual configuration is error-prone and time-consuming. This project demonstrates how to automate routine network tasks using Ansible, including:

- Device configuration (hostnames, users, interfaces)
- Backup of running configurations
- Applying static routes
- Verifying device state (interfaces, routes, NTP, SSH)
- Safe “check mode” testing before making changes

The playbooks are designed to be **idempotent**, meaning they can be run multiple times without causing unexpected changes.

---

## **Why This Project Exists**

- To provide a **learning lab** for network automation using Ansible and EVE-NG.
- To demonstrate **real-world practices** in network automation, similar to what companies use today.
- To create **repeatable, safe, and verifiable** network changes in virtual lab environments.

---

## **Repository Structure**

network-automation/
├── inventory/
│   └── hosts.ini
│
├── playbooks/
│   ├── backup.yml
│   ├── hostname_user.yml
│   ├── interfaces.yml
│   ├── static_routes.yml
│   ├── verify.yml
│   └── full_safe.yml
│
├── scripts/
│   └── precheck.py
│
├── .gitignore
└── README.md


---

## **Supported Devices**

- Cisco routers (IOS)
- Cisco switches (if needed)
- EVE-NG virtual lab environment  

--Switches can be configured with additional playbooks if required. Currently, the main focus is on routers. Unconfigured interfaces on Router1 and Router2 can be safely added using the interface playbooks.

---

## **Usage Instructions**

### 1. Check Mode (Safe Testing)

Run a playbook in **check mode** to preview changes **without applying them**:

```bash
ansible-playbook -i inventory/hosts.ini playbooks/<playbook_name>.yml --check
```




Why Use This Repository

Demonstrates practical network automation in a lab setting

Prepares you for real-world automation tasks in companies

Safe, repeatable, and easy to modify for different lab topologies


Contact

Created by Rhayem Saidi
GitHub: https://github.com/RhayemSaidi
