# @ohos.enterprise.networkManager(Network Management)

This module provides device network management capabilities, including querying IP addresses and MAC addresses, managing network interface states, configuring global network proxies, managing firewall rules and domain name filtering rules, controlling mobile data networks, managing APN configurations, and configuring Ethernet networks. It is suitable for enterprise IT administrators to centrally manage and secure device networks, helping enterprises achieve unified network access policy management, prevent network attacks and data leaks, and reduce network management costs.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { networkManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addApn(Network Management)](arkts-mdm-networkmanager-addapn-f.md) |
| [addDomainFilterRule(Network Management)](arkts-mdm-networkmanager-adddomainfilterrule-f.md) |
| [addFirewallRule(Network Management)](arkts-mdm-networkmanager-addfirewallrule-f.md) |
| [deleteApn(Network Management)](arkts-mdm-networkmanager-deleteapn-f.md) |
| [getAllNetworkInterfacesSync(Network Management)](arkts-mdm-networkmanager-getallnetworkinterfacessync-f.md) |
| [getDomainFilterRules(Network Management)](arkts-mdm-networkmanager-getdomainfilterrules-f.md) |
| [getFirewallRules(Network Management)](arkts-mdm-networkmanager-getfirewallrules-f.md) |
| [getGlobalProxyForAccount(Network Management)](arkts-mdm-networkmanager-getglobalproxyforaccount-f.md) |
| [getGlobalProxySync(Network Management)](arkts-mdm-networkmanager-getglobalproxysync-f.md) |
| [getIpAddressSync(Network Management)](arkts-mdm-networkmanager-getipaddresssync-f.md) |
| [getMacSync(Network Management)](arkts-mdm-networkmanager-getmacsync-f.md) |
| [isNetworkInterfaceDisabledSync(Network Management)](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md) |
| [isNetworkInterfaceDisabledSync(Network Management)](arkts-mdm-networkmanager-isnetworkinterfacedisabledsync-f.md) |
| [queryApn(Network Management)](arkts-mdm-networkmanager-queryapn-f.md) |
| [queryApn(Network Management)](arkts-mdm-networkmanager-queryapn-f.md) |
| [removeDomainFilterRule(Network Management)](arkts-mdm-networkmanager-removedomainfilterrule-f.md) |
| [removeFirewallRule(Network Management)](arkts-mdm-networkmanager-removefirewallrule-f.md) |
| [setEthernetConfig(Network Management)](arkts-mdm-networkmanager-setethernetconfig-f.md) |
| [setGlobalProxyForAccount(Network Management)](arkts-mdm-networkmanager-setglobalproxyforaccount-f.md) |
| [setGlobalProxySync(Network Management)](arkts-mdm-networkmanager-setglobalproxysync-f.md) |
| [setNetworkInterfaceDisabledSync(Network Management)](arkts-mdm-networkmanager-setnetworkinterfacedisabledsync-f.md) |
| [setPreferredApn(Network Management)](arkts-mdm-networkmanager-setpreferredapn-f.md) |
| [turnOffMobileData(Network Management)](arkts-mdm-networkmanager-turnoffmobiledata-f.md) |
| [turnOnMobileData(Network Management)](arkts-mdm-networkmanager-turnonmobiledata-f.md) |
| [updateApn(Network Management)](arkts-mdm-networkmanager-updateapn-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addIptablesFilterRule(Network Management)](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md) |
| [addIptablesFilterRule(Network Management)](arkts-mdm-networkmanager-addiptablesfilterrule-f-sys.md) |
| [getAllNetworkInterfaces(Network Management)](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md) |
| [getAllNetworkInterfaces(Network Management)](arkts-mdm-networkmanager-getallnetworkinterfaces-f-sys.md) |
| [getGlobalProxy(Network Management)](arkts-mdm-networkmanager-getglobalproxy-f-sys.md) |
| [getGlobalProxy(Network Management)](arkts-mdm-networkmanager-getglobalproxy-f-sys.md) |
| [getIpAddress(Network Management)](arkts-mdm-networkmanager-getipaddress-f-sys.md) |
| [getIpAddress(Network Management)](arkts-mdm-networkmanager-getipaddress-f-sys.md) |
| [getMac(Network Management)](arkts-mdm-networkmanager-getmac-f-sys.md) |
| [getMac(Network Management)](arkts-mdm-networkmanager-getmac-f-sys.md) |
| [isNetworkInterfaceDisabled(Network Management)](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md) |
| [isNetworkInterfaceDisabled(Network Management)](arkts-mdm-networkmanager-isnetworkinterfacedisabled-f-sys.md) |
| [listIptablesFilterRules(Network Management)](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md) |
| [listIptablesFilterRules(Network Management)](arkts-mdm-networkmanager-listiptablesfilterrules-f-sys.md) |
| [removeIptablesFilterRule(Network Management)](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md) |
| [removeIptablesFilterRule(Network Management)](arkts-mdm-networkmanager-removeiptablesfilterrule-f-sys.md) |
| [setGlobalProxy(Network Management)](arkts-mdm-networkmanager-setglobalproxy-f-sys.md) |
| [setGlobalProxy(Network Management)](arkts-mdm-networkmanager-setglobalproxy-f-sys.md) |
| [setNetworkInterfaceDisabled(Network Management)](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md) |
| [setNetworkInterfaceDisabled(Network Management)](arkts-mdm-networkmanager-setnetworkinterfacedisabled-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DomainFilterRule(Network Management)](arkts-mdm-networkmanager-domainfilterrule-i.md) |
| [FirewallRule(Network Management)](arkts-mdm-networkmanager-firewallrule-i.md) |
| [InterfaceConfig(Network Management)](arkts-mdm-networkmanager-interfaceconfig-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AddFilterRule(Network Management)](arkts-mdm-networkmanager-addfilterrule-i-sys.md) |
| [RemoveFilterRule(Network Management)](arkts-mdm-networkmanager-removefilterrule-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Action(Network Management)](arkts-mdm-networkmanager-action-e.md) |
| [Direction(Network Management)](arkts-mdm-networkmanager-direction-e.md) |
| [IpSetMode(Network Management)](arkts-mdm-networkmanager-ipsetmode-e.md) |
| [LogType(Network Management)](arkts-mdm-networkmanager-logtype-e.md) |
| [Protocol(Network Management)](arkts-mdm-networkmanager-protocol-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AddMethod(Network Management)](arkts-mdm-networkmanager-addmethod-e-sys.md) |
<!--DelEnd-->
