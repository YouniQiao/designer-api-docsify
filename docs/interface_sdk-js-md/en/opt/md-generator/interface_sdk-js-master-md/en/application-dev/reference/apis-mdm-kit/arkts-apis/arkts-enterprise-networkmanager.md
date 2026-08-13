# @ohos.enterprise.networkManager

This module provides device network management capabilities, including querying IP addresses and MAC addresses, managing network interface states, configuring global network proxies, managing firewall rules and domain name filtering rules, controlling mobile data networks, managing APN configurations, and configuring Ethernet networks. It is suitable for enterprise IT administrators to centrally manage and secure device networks, helping enterprises achieve unified network access policy management, prevent network attacks and data leaks, and reduce network management costs. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace networkManager--><!--Device-unnamed-declare namespace networkManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { networkManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addApn](arkts-mdm-networkmanager-addapn-f.md#addApn) |
| [addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#addDomainFilterRule) |
| [addFirewallRule](arkts-mdm-networkmanager-addfirewallrule-f.md#addFirewallRule) |
| [deleteApn](arkts-mdm-networkmanager-deleteapn-f.md#deleteApn) |
| [getAllNetworkInterfacesSync](arkts-mdm-networkmanager-getallnetworkinterfacessync-f.md#getAllNetworkInterfacesSync) |
| [getDomainFilterRules](arkts-mdm-networkmanager-getdomainfilterrules-f.md#getDomainFilterRules) |
| [getFirewallRules](arkts-mdm-networkmanager-getfirewallrules-f.md#getFirewallRules) |
| [getGlobalProxyForAccount](arkts-mdm-networkmanager-getglobalproxyforaccount-f.md#getGlobalProxyForAccount) |
| [getGlobalProxySync](arkts-mdm-networkmanager-getglobalproxysync-f.md#getGlobalProxySync) |
| [getIpAddressSync](arkts-mdm-networkmanager-getipaddresssync-f.md#getIpAddressSync) |
| [getMacSync](arkts-mdm-networkmanager-getmacsync-f.md#getMacSync) |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isNetworkInterfaceDisabledSync) |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isNetworkInterfaceDisabledSync) |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryApn) |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryApn) |
| [removeDomainFilterRule](arkts-mdm-networkmanager-removedomainfilterrule-f.md#removeDomainFilterRule) |
| [removeFirewallRule](arkts-mdm-networkmanager-removefirewallrule-f.md#removeFirewallRule) |
| [setEthernetConfig](arkts-mdm-networkmanager-setethernetconfig-f.md#setEthernetConfig) |
| [setGlobalProxyForAccount](arkts-mdm-networkmanager-setglobalproxyforaccount-f.md#setGlobalProxyForAccount) |
| [setGlobalProxySync](arkts-mdm-networkmanager-setglobalproxysync-f.md#setGlobalProxySync) |
| [setNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-setnetworkinterfacedisabledsync-f.md#setNetworkInterfaceDisabledSync) |
| [setPreferredApn](arkts-mdm-networkmanager-setpreferredapn-f.md#setPreferredApn) |
| [turnOffMobileData](arkts-mdm-networkmanager-turnoffmobiledata-f.md#turnOffMobileData) |
| [turnOnMobileData](arkts-mdm-networkmanager-turnonmobiledata-f.md#turnOnMobileData) |
| [updateApn](arkts-mdm-networkmanager-updateapn-f.md#updateApn) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md#addIptablesFilterRule-(System-API)) |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md#addIptablesFilterRule-(System-API)) |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md#getAllNetworkInterfaces-(System-API)) |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md#getAllNetworkInterfaces-(System-API)) |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f-sys.md#getGlobalProxy-(System-API)) |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f-sys.md#getGlobalProxy-(System-API)) |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f-sys.md#getIpAddress-(System-API)) |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f-sys.md#getIpAddress-(System-API)) |
| [getMac](arkts-mdm-networkmanager-getmac-f-sys.md#getMac-(System-API)) |
| [getMac](arkts-mdm-networkmanager-getmac-f-sys.md#getMac-(System-API)) |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md#isNetworkInterfaceDisabled-(System-API)) |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md#isNetworkInterfaceDisabled-(System-API)) |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md#listIptablesFilterRules-(System-API)) |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md#listIptablesFilterRules-(System-API)) |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md#removeIptablesFilterRule-(System-API)) |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md#removeIptablesFilterRule-(System-API)) |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f-sys.md#setGlobalProxy-(System-API)) |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f-sys.md#setGlobalProxy-(System-API)) |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md#setNetworkInterfaceDisabled-(System-API)) |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md#setNetworkInterfaceDisabled-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DomainFilterRule](arkts-mdm-networkmanager-domainfilterrule-i.md) |
| [FirewallRule](arkts-mdm-networkmanager-firewallrule-i.md) |
| [InterfaceConfig](arkts-mdm-networkmanager-interfaceconfig-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AddFilterRule](arkts-mdm-networkmanager-addfilterrule-i-sys.md) |
| [RemoveFilterRule](arkts-mdm-networkmanager-removefilterrule-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Action](arkts-mdm-networkmanager-action-e.md) |
| [Direction](arkts-mdm-networkmanager-direction-e.md) |
| [IpSetMode](arkts-mdm-networkmanager-ipsetmode-e.md) |
| [LogType](arkts-mdm-networkmanager-logtype-e.md) |
| [Protocol](arkts-mdm-networkmanager-protocol-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AddMethod](arkts-mdm-networkmanager-addmethod-e-sys.md) |
<!--DelEnd-->
