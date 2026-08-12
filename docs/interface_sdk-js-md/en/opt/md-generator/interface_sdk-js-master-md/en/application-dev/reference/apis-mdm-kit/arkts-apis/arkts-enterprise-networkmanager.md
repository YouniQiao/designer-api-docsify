# @ohos.enterprise.networkManager(Network Management)

This module provides device network management capabilities, including querying IP addresses and MAC addresses,managing network interface states, configuring global network proxies, managing firewall rules and domain name filtering rules, controlling mobile data networks, managing APN configurations, and configuring Ethernet networks. It is suitable for enterprise IT administrators to centrally manage and secure device networks, helping enterprises achieve unified network access policy management, prevent network attacks and data leaks, and reduce network management costs.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace networkManager--><!--Device-unnamed-declare namespace networkManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { networkManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addApn](arkts-mdm-networkmanager-addapn-f.md#addapn) |
| [addDomainFilterRule](arkts-mdm-networkmanager-adddomainfilterrule-f.md#adddomainfilterrule) |
| [addFirewallRule](arkts-mdm-networkmanager-addfirewallrule-f.md#addfirewallrule) |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f.md#addiptablesfilterrule) |
| [addIptablesFilterRule](arkts-mdm-networkmanager-addiptablesfilterrule-f.md#addiptablesfilterrule-1) |
| [deleteApn](arkts-mdm-networkmanager-deleteapn-f.md#deleteapn) |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f.md#getallnetworkinterfaces) |
| [getAllNetworkInterfaces](arkts-mdm-networkmanager-getallnetworkinterfaces-f.md#getallnetworkinterfaces-1) |
| [getAllNetworkInterfacesSync](arkts-mdm-networkmanager-getallnetworkinterfacessync-f.md#getallnetworkinterfacessync) |
| [getDomainFilterRules](arkts-mdm-networkmanager-getdomainfilterrules-f.md#getdomainfilterrules) |
| [getFirewallRules](arkts-mdm-networkmanager-getfirewallrules-f.md#getfirewallrules) |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f.md#getglobalproxy) |
| [getGlobalProxy](arkts-mdm-networkmanager-getglobalproxy-f.md#getglobalproxy-1) |
| [getGlobalProxyForAccount](arkts-mdm-networkmanager-getglobalproxyforaccount-f.md#getglobalproxyforaccount) |
| [getGlobalProxySync](arkts-mdm-networkmanager-getglobalproxysync-f.md#getglobalproxysync) |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f.md#getipaddress) |
| [getIpAddress](arkts-mdm-networkmanager-getipaddress-f.md#getipaddress-1) |
| [getIpAddressSync](arkts-mdm-networkmanager-getipaddresssync-f.md#getipaddresssync) |
| [getMac](arkts-mdm-networkmanager-getmac-f.md#getmac) |
| [getMac](arkts-mdm-networkmanager-getmac-f.md#getmac-1) |
| [getMacSync](arkts-mdm-networkmanager-getmacsync-f.md#getmacsync) |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f.md#isnetworkinterfacedisabled) |
| [isNetworkInterfaceDisabled](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f.md#isnetworkinterfacedisabled-1) |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isnetworkinterfacedisabledsync) |
| [isNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md#isnetworkinterfacedisabledsync-1) |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f.md#listiptablesfilterrules) |
| [listIptablesFilterRules](arkts-mdm-networkmanager-listiptablesfilterrules-f.md#listiptablesfilterrules-1) |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryapn) |
| [queryApn](arkts-mdm-networkmanager-queryapn-f.md#queryapn-1) |
| [removeDomainFilterRule](arkts-mdm-networkmanager-removedomainfilterrule-f.md#removedomainfilterrule) |
| [removeFirewallRule](arkts-mdm-networkmanager-removefirewallrule-f.md#removefirewallrule) |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f.md#removeiptablesfilterrule) |
| [removeIptablesFilterRule](arkts-mdm-networkmanager-removeiptablesfilterrule-f.md#removeiptablesfilterrule-1) |
| [setEthernetConfig](arkts-mdm-networkmanager-setethernetconfig-f.md#setethernetconfig) |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f.md#setglobalproxy) |
| [setGlobalProxy](arkts-mdm-networkmanager-setglobalproxy-f.md#setglobalproxy-1) |
| [setGlobalProxyForAccount](arkts-mdm-networkmanager-setglobalproxyforaccount-f.md#setglobalproxyforaccount) |
| [setGlobalProxySync](arkts-mdm-networkmanager-setglobalproxysync-f.md#setglobalproxysync) |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f.md#setnetworkinterfacedisabled) |
| [setNetworkInterfaceDisabled](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f.md#setnetworkinterfacedisabled-1) |
| [setNetworkInterfaceDisabledSync](arkts-mdm-networkmanager-setnetworkinterfacedisabledsync-f.md#setnetworkinterfacedisabledsync) |
| [setPreferredApn](arkts-mdm-networkmanager-setpreferredapn-f.md#setpreferredapn) |
| [turnOffMobileData](arkts-mdm-networkmanager-turnoffmobiledata-f.md#turnoffmobiledata) |
| [turnOnMobileData](arkts-mdm-networkmanager-turnonmobiledata-f.md#turnonmobiledata) |
| [updateApn](arkts-mdm-networkmanager-updateapn-f.md#updateapn) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AddFilterRule](arkts-mdm-networkmanager-addfilterrule-i.md) |
| [DomainFilterRule](arkts-mdm-networkmanager-domainfilterrule-i.md) |
| [FirewallRule](arkts-mdm-networkmanager-firewallrule-i.md) |
| [InterfaceConfig](arkts-mdm-networkmanager-interfaceconfig-i.md) |
| [RemoveFilterRule](arkts-mdm-networkmanager-removefilterrule-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Action](arkts-mdm-networkmanager-action-e.md) |
| [AddMethod](arkts-mdm-networkmanager-addmethod-e.md) |
| [Direction](arkts-mdm-networkmanager-direction-e.md) |
| [IpSetMode](arkts-mdm-networkmanager-ipsetmode-e.md) |
| [LogType](arkts-mdm-networkmanager-logtype-e.md) |
| [Protocol](arkts-mdm-networkmanager-protocol-e.md) |
