# @ohos.enterprise.networkManager

This module provides device network management capabilities, including querying IP addresses and MAC addresses, managing network interface states, configuring global network proxies, managing firewall rules and domain name filtering rules, controlling mobile data networks, managing APN configurations, and configuring Ethernet networks. It is suitable for enterprise IT administrators to centrally manage and secure device networks, helping enterprises achieve unified network access policy management, prevent network attacks and data leaks, and reduce network management costs. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace networkManager--><!--Device-unnamed-declare namespace networkManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { networkManager } from 'networkManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addApn](arkts-mdm-networkmanager-addapn-f.md#addapn) | Adds an access point name (APN). |
| [addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#adddomainfilterrule) | Adds domain name filtering rules for the device. In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22. [LogType](arkts-mdm-networkmanager-logtype-e.md#logtype) is supported since API version 23. > **NOTE：**> > - After a rule with [Action](arkts-mdm-networkmanager-action-e.md#action) set to **ALLOW** is added, a default **DENY** rule is > added automatically to discard or intercept domain name resolution packets that are not covered by the **ALLOW** > rule. > > - The added rules will be cleared after the device restarts. > > - To prevent interception rules from becoming ineffective due to DNS caching, it is recommended that you > configure domain name filtering rules immediately after the system starts up. If interception fails because of > DNS caching, restart the system to clear the cache and restore the interception function. > > - Rule matching order: Domain name filtering rules added by this API are matched first, followed by IP firewall > rules (added via [addFirewallRule](arkts-mdm-networkmanager-addfirewallrule-f.md#addfirewallrule)). Within both domain name rules and IP > rules, matching is performed in the order of ALLOW, DENY, and REJECT [actions](arkts-mdm-networkmanager-action-e.md#action). |
| [addFirewallRule](arkts-mdm-networkmanager-addfirewallrule-f.md#addfirewallrule) | Adds firewall rules for the device. This API is suitable for enterprise network security management and control scenarios. For example, it can be used to restrict network access from specific IP addresses, prevent malicious network attacks, control network communication of applications, and manage the trustlist or blocklist for network access. This helps enterprises implement refined control over network access and prevent network attacks and data leaks. In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22. [LogType](arkts-mdm-networkmanager-logtype-e.md#logtype) is supported since API version 23. > **NOTE：**> > - After a rule with [Action](arkts-mdm-networkmanager-action-e.md#action) set to **ALLOW** is added, a rule with **Action** set > to **DENY** is added by default to discard or intercept all network data packets that do not meet the **ALLOW** > rule. > > - After the device is restarted, the firewall rules are cleared. > > - Rule matching order: Domain name filtering rules (added via > [addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#adddomainfilterrule)) are matched first, followed by IP firewall rules > added by this API. Within both domain name rules and IP rules, matching is performed in the order of ALLOW, DENY, > and REJECT [actions](arkts-mdm-networkmanager-action-e.md#action). |
| [deleteApn](arkts-mdm-networkmanager-deleteapn-f.md#deleteapn) | Deletes the APN. This API is suitable for enterprise mobile network configuration management scenarios, such as removing invalid APN configurations, adjusting mobile network access point settings, and preventing the use of incorrect APN configurations. It helps enterprises maintain correct mobile network configurations and ensure that devices connect to mobile networks through the appropriate access points. |
| [getAllNetworkInterfacesSync](arkts-mdm-networkmanager-getallnetworkinterfacessync-f.md#getallnetworkinterfacessync) | Obtains all activated wired network interfaces. This API is suitable for enterprise network management scenarios, such as viewing available network connections on the current device, auditing network interface status, and preparing for subsequent network configuration operations. It helps enterprises understand device network connection status, facilitating centralized management of network resources and troubleshooting of network issues. |
| [getDomainFilterRules](arkts-mdm-networkmanager-getdomainfilterrules-f.md#getdomainfilterrules) | Obtains domain name filtering rules. This API is suitable for enterprise network security audit scenarios, such as checking current domain name filtering policy configurations, auditing domain name access control rules, verifying whether domain name filtering rules are correctly executed, and troubleshooting domain name access issues. It helps enterprises review and validate domain name access control policies to ensure network access control complies with security requirements. In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22. [LogType](arkts-mdm-networkmanager-logtype-e.md#logtype) is supported since API version 23. |
| [getFirewallRules](arkts-mdm-networkmanager-getfirewallrules-f.md#getfirewallrules) | Queries firewall rules of a device. This API is suitable for enterprise network security audit scenarios, such as checking the current firewall policy configuration, auditing network access control rules, verifying whether firewall rules are correctly executed, and troubleshooting network access issues. It helps enterprises audit and verify network security policies and ensure that network access control meets security requirements. In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22. [LogType](arkts-mdm-networkmanager-logtype-e.md#logtype) is supported since API version 23. |
| [getGlobalProxyForAccount](arkts-mdm-networkmanager-getglobalproxyforaccount-f.md#getglobalproxyforaccount) | Obtains the network proxy for a specified user. This API is suitable for network management scenarios in enterprise environments with multiple users, such as auditing user-level network proxy configurations, verifying user network access policies, and troubleshooting user network access issues. It helps enterprises check and verify user-level network management policies. > **NOTE：**> > This API is used to obtain the proxy configuration of a specified user set by the **setGlobalProxyForAccount** > API. To obtain the global proxy configuration that applies to all users, you are advised to use the > [getGlobalProxySync](arkts-mdm-networkmanager-getglobalproxysync-f.md#getglobalproxysync) API. |
| [getGlobalProxySync](arkts-mdm-networkmanager-getglobalproxysync-f.md#getglobalproxysync) | Obtains the global network proxy. This API is suitable for enterprise network management scenarios, such as auditing the current network proxy configuration, verifying whether the proxy policy takes effect, and troubleshooting network access issues. It helps enterprises check the network proxy settings and ensure that the network access policy is correctly executed. |
| [getIpAddressSync](arkts-mdm-networkmanager-getipaddresssync-f.md#getipaddresssync) | Obtains the device IP address based on the network interface. This API is suitable for enterprise network management scenarios, such as network audit, device positioning, network connection troubleshooting, and IP address allocation management. It helps enterprise IT administrators understand device network configurations, facilitating network management and fault diagnosis. |
| [getMacSync](arkts-mdm-networkmanager-getmacsync-f.md#getmacsync) | Obtains the MAC address of a device based on the network interface. This API is suitable for enterprise network management scenarios, such as device identification, network access control, MAC address audit, and device asset management. It helps enterprises identify and track devices, implementing refined network access control. |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isnetworkinterfacedisabledsync) | Queries whether a specified network interface is disabled. |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isnetworkinterfacedisabledsync) | Queries whether a specified network interface is disabled. This API is suitable for enterprise network management scenarios, such as checking network interface status, auditing network interface usage, and verifying the execution effect of network policies. It helps enterprises determine whether their network interface management policies have taken effect, facilitating policy adjustment and troubleshooting. |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryapn) | Queries the APN ID. This API is suitable for enterprise mobile network configuration audit scenarios, such as finding APNs with specific configurations, verifying whether an APN configuration exists, and providing APN ID parameters for APN management operations. It helps enterprises locate and manage APN configurations, and supplies the necessary parameter information for updating and deleting APNs. |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryapn) | Queries the APN parameter information. This API is suitable for enterprise mobile network configuration audit scenarios, such as checking the configuration parameters of a specific APN, verifying whether the APN configuration is correct, and auditing mobile network access point settings. It helps enterprises review and validate APN configurations to ensure that mobile network settings meet requirements. |
| [removeDomainFilterRule](arkts-mdm-networkmanager-removedomainfilterrule-f.md#removedomainfilterrule) | Removes the domain name filtering rules. This API is suitable for enterprise network security policy adjustment scenarios, such as canceling access restrictions on certain domain names, adjusting domain name filtering policies, removing outdated or invalid rules, and resolving false positive blocking issues. It helps enterprises flexibly adjust domain name access policies to ensure that network access control policies meet actual business requirements. In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22. [LogType](arkts-mdm-networkmanager-logtype-e.md#logtype) is supported since API version 23. If there is no rule with [Action](arkts-mdm-networkmanager-action-e.md#action) being **ALLOW** after the rule is removed, the **DENY** rules that are added by default with [addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#adddomainfilterrule) will be removed. |
| [removeFirewallRule](arkts-mdm-networkmanager-removefirewallrule-f.md#removefirewallrule) | Removes a firewall rule. This API is suitable for enterprise network security policy adjustment scenarios, such as canceling certain network access restrictions, adjusting firewall policies, and clearing outdated or invalid rules. It helps enterprises flexibly adjust network security policies and ensure that network access control policies meet actual requirements. In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22. [LogType](arkts-mdm-networkmanager-logtype-e.md#logtype) is supported since API version 23. If there is no rule with [Action](arkts-mdm-networkmanager-action-e.md#action) being **ALLOW** after the rule is removed, the **DENY** rules that are added by default with [addFirewallRule](arkts-mdm-networkmanager-addfirewallrule-f.md#addfirewallrule) will be removed. |
| [setEthernetConfig](arkts-mdm-networkmanager-setethernetconfig-f.md#setethernetconfig) | Sets the IP address of a specific Ethernet interface. This API is suitable for enterprise network management scenarios, such as configuring static IP addresses for devices, centrally managing IP address allocation for enterprise network devices, and setting network parameters. It helps enterprises centrally manage network configurations and ensures that device network parameters comply with enterprise network management policies. |
| [setGlobalProxyForAccount](arkts-mdm-networkmanager-setglobalproxyforaccount-f.md#setglobalproxyforaccount) | Sets the network proxy for a specified user. This API is suitable for network management scenarios in enterprise environments with multiple users. For example, you can set different network proxy policies for different users, implement user-level network access control, and meet the network access requirements of different users, helping enterprises implement refined user-level network management. |
| [setGlobalProxySync](arkts-mdm-networkmanager-setglobalproxysync-f.md#setglobalproxysync) | Sets the global network proxy. This API is suitable for enterprise network management scenarios, such as setting a unified network proxy for an enterprise, implementing network access audit, controlling network access paths, and optimizing network performance. It helps enterprises centrally manage network access, making network access auditable and controllable. |
| [setNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-setnetworkinterfacedisabledsync-f.md#setnetworkinterfacedisabledsync) | Disables the device from using the specified network interface. This API is suitable for enterprise network security management and control scenarios. It can be used to disable high-risk network interfaces, restrict devices from using specific network connections, and prevent data leaks through network interfaces. This helps enterprises reduce network security risks and prevent attacks or data leaks through specific network interfaces. |
| [setPreferredApn](arkts-mdm-networkmanager-setpreferredapn-f.md#setpreferredapn) | Sets the preferred APN. |
| [turnOffMobileData](arkts-mdm-networkmanager-turnoffmobiledata-f.md#turnoffmobiledata) | Turns off mobile data. |
| [turnOnMobileData](arkts-mdm-networkmanager-turnonmobiledata-f.md#turnonmobiledata) | Turns on mobile data. |
| [updateApn](arkts-mdm-networkmanager-updateapn-f.md#updateapn) | Updates the APN. This API is suitable for enterprise mobile network configuration management scenarios, such as modifying APN configuration parameters, adjusting carrier settings, and optimizing mobile network connection performance. It helps enterprises flexibly adjust mobile network configurations and ensure that the mobile network connection parameters of devices meet actual requirements. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md#addiptablesfilterrule) | Adds a network packet filtering rule for the device. Only IPv4 is supported. This API uses an asynchronous callback to return the result. |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md#addiptablesfilterrule-system-api) | Adds a network packet filtering rule for the device. Only IPv4 is supported. This API uses a promise to return the result. |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md#getallnetworkinterfaces) | Obtains all activated wired network interfaces. This API uses an asynchronous callback to return the result. |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md#getallnetworkinterfaces-system-api) | Obtains all activated wired network interfaces. This API uses a promise to return the result. |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f-sys.md#getglobalproxy) | Obtains the global network proxy. This API uses an asynchronous callback to return the result. |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f-sys.md#getglobalproxy-system-api) | Obtains the global network proxy. This API uses a promise to return the result. |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f-sys.md#getipaddress) | Obtains the device IP address based on the network interface. This API uses an asynchronous callback to return the result. |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f-sys.md#getipaddress-system-api) | Obtains the device IP address based on the network interface. This API uses a promise to return the result. |
| [getMac](arkts-mdm-networkmanager-getmac-f-sys.md#getmac) | Obtains the MAC address of a device based on the network interface. This API uses an asynchronous callback to return the result. |
| [getMac](arkts-mdm-networkmanager-getmac-f-sys.md#getmac-system-api) | Obtains the MAC address of a device based on the network interface. This API uses a promise to return the result. |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md#isnetworkinterfacedisabled) | Queries whether a specified network interface is disabled. This API uses an asynchronous callback to return the result. |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md#isnetworkinterfacedisabled-system-api) | Queries whether a specified network interface is disabled. This API uses a promise to return the result. |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md#listiptablesfilterrules) | Obtains the network packet filtering rule. Only IPv4 is supported. This API uses an asynchronous callback to return the result. |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md#listiptablesfilterrules-system-api) | Obtains the network packet filtering rule. Only IPv4 is supported. This API uses a promise to return the result. |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md#removeiptablesfilterrule) | Removes the network packet filtering rule. Only IPv4 is supported. This API uses an asynchronous callback to return the result. |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md#removeiptablesfilterrule-system-api) | Removes the network packet filtering rule. Only IPv4 is supported. This API uses a promise to return the result. |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f-sys.md#setglobalproxy) | Sets the global network proxy. This API uses an asynchronous callback to return the result. |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f-sys.md#setglobalproxy-system-api) | Sets the global network proxy. This API uses a promise to return the result. |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md#setnetworkinterfacedisabled) | Disables a network interface. This API uses an asynchronous callback to return the result. |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md#setnetworkinterfacedisabled-system-api) | Disables a network interface. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [DomainFilterRule](arkts-mdm-networkmanager-domainfilterrule-i.md) | Represents a domain name filtering rule. In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22. [LogType](arkts-mdm-networkmanager-logtype-e.md#logtype) is supported since API version 23. |
| [FirewallRule](arkts-mdm-networkmanager-firewallrule-i.md) | Represents a firewall rule. In API version 21 and earlier versions, only IPv4 is supported. IPv4 and IPv6 are supported since API version 22. [LogType](arkts-mdm-networkmanager-logtype-e.md#logtype) is supported since API version 23. |
| [InterfaceConfig](arkts-mdm-networkmanager-interfaceconfig-i.md) | Enumerates Ethernet network interface configurations. Only IPv4 is supported. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [AddFilterRule](arkts-mdm-networkmanager-addfilterrule-i-sys.md) | Defines the network packet filtering rule to add. |
| [RemoveFilterRule](arkts-mdm-networkmanager-removefilterrule-i-sys.md) | Defines the network packet filtering rule to remove. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [Action](arkts-mdm-networkmanager-action-e.md) | Enumerates the actions that can be taken for data packets. |
| [Direction](arkts-mdm-networkmanager-direction-e.md) | Enumerates the direction chains to which the rule applies. |
| [IpSetMode](arkts-mdm-networkmanager-ipsetmode-e.md) | Enumerates Ethernet connection configuration modes. |
| [LogType](arkts-mdm-networkmanager-logtype-e.md) | Enumerates the log types. |
| [Protocol](arkts-mdm-networkmanager-protocol-e.md) | Enumerates network protocols. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [AddMethod](arkts-mdm-networkmanager-addmethod-e-sys.md) | Enumerates the methods used to add the network packets. |
<!--DelEnd-->

