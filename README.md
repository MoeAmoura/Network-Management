# SNMP MIB Module Assignment

## Objectives

The primary goal of this assignment is to gain hands-on experience with the SNMP SMIv2 data modeling language, specifically to write a MIB module. The focus is on creating a module that enables the management (querying and manipulation) of a firewall table on a machine using SNMP.

## Problem Statement

In this assignment, your task is to utilize the SNMP SMIv2 modeling language to develop an SNMP MIB module. This module should provide the capability to manage the firewall table, including querying and manipulating its entries.

### Module Requirements:

- The module should be named ID-xxxxxx, where 'xxxxxx' represents your student ID.
- All managed objects should descend (directly or indirectly) from the node nes470(9000) under the enterprises node.
- Each entry in the firewall table should define a firewall rule with the following information:
  - Source MAC address
  - Destination MAC address
  - Source IP address
  - Destination IP address
  - Source TCP/UDP port number
  - Destination TCP/UDP port number
  - Protocol type: TCP, UDP, or ICMP
  - Action: accept, drop, or reject
  - Number of packets that have matched this rule/entry.
- The SNMP manager should be able to retrieve all the data in the firewall table.
- The SNMP manager can modify all the data in the firewall table except the number of packets that have matched a given rule.
- Each managed object must have the appropriate access permissions and data type.
- The module must conform to the SMIv2 RFC (RFC 2578).
- When validated by the smilint tool with severity level 4 (via the options `smilint -l 4 -i group`), the module should produce no errors and no warnings.

## Hints

- Start with and build upon the skeletal MIB module presented in Section 5.7 in the [RFC 2578 document](https://tools.ietf.org/html/rfc2578).
- Look into, investigate, and mimic the IETF’s interfaces MIB module or other actual standard MIB modules.
