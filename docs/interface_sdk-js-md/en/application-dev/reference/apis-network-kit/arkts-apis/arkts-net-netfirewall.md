# @ohos.net.netFirewall

Provides interfaces to manage net firewall.

**Since:** 14

<!--Device-unnamed-declare namespace netFirewall--><!--Device-unnamed-declare namespace netFirewall-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

## Modules to Import

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addNetFirewallRule](arkts-network-netfirewall-addnetfirewallrule-f.md#addnetfirewallrule) | Add a firewall rule. |
| [getNetFirewallPolicy](arkts-network-netfirewall-getnetfirewallpolicy-f.md#getnetfirewallpolicy) | Get firewall policy by userId. |
| [getNetFirewallRule](arkts-network-netfirewall-getnetfirewallrule-f.md#getnetfirewallrule) | Get a specified firewall rule by userId and ruleId. |
| [getNetFirewallRules](arkts-network-netfirewall-getnetfirewallrules-f.md#getnetfirewallrules) | Get firewall rules by userId, and it is necessary to specify the pagination query parameters. |
| [removeNetFirewallRule](arkts-network-netfirewall-removenetfirewallrule-f.md#removenetfirewallrule) | Delete a firewall rule by userId and ruleId. |
| [setNetFirewallPolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md#setnetfirewallpolicy) | Set firewall policy by userId.<p>Enables or disables the firewall function, and specifies the default actions for inbound connections and outbound connections.</p> |
| [updateNetFirewallRule](arkts-network-netfirewall-updatenetfirewallrule-f.md#updatenetfirewallrule) | Update a firewall rule. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getInterceptedRecords](arkts-network-netfirewall-getinterceptedrecords-f-sys.md#getinterceptedrecords) | Get intercepted records by userId, and it is necessary to specify the pagination query parameters. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [FirewallRulePage](arkts-network-netfirewall-firewallrulepage-i.md) | Rule page information. |
| [NetFirewallDnsParams](arkts-network-netfirewall-netfirewalldnsparams-i.md) | Firewall DNS parameters. |
| [NetFirewallDomainParams](arkts-network-netfirewall-netfirewalldomainparams-i.md) | Firewall domain name parameters. |
| [NetFirewallIpParams](arkts-network-netfirewall-netfirewallipparams-i.md) | Firewall IP parameters. |
| [NetFirewallPolicy](arkts-network-netfirewall-netfirewallpolicy-i.md) | Firewall policy. |
| [NetFirewallPortParams](arkts-network-netfirewall-netfirewallportparams-i.md) | Firewall port parameters. |
| [NetFirewallRule](arkts-network-netfirewall-netfirewallrule-i.md) | Firewall rules. |
| [RequestParam](arkts-network-netfirewall-requestparam-i.md) | Pagination query input parameters. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [InterceptedRecord](arkts-network-netfirewall-interceptedrecord-i-sys.md) | Intercepted record. |
| [InterceptedRecordPage](arkts-network-netfirewall-interceptedrecordpage-i-sys.md) | Intercepted record page information. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [FirewallRuleAction](arkts-network-netfirewall-firewallruleaction-e.md) | Firewall rule behavior enumeration. |
| [NetFirewallOrderField](arkts-network-netfirewall-netfirewallorderfield-e.md) | Pagination query sorting field. |
| [NetFirewallOrderType](arkts-network-netfirewall-netfirewallordertype-e.md) | Pagination query sorting type. |
| [NetFirewallRuleDirection](arkts-network-netfirewall-netfirewallruledirection-e.md) | Firewall rule direction enumeration. |
| [NetFirewallRuleType](arkts-network-netfirewall-netfirewallruletype-e.md) | Indicates the firewall rule type. |

