# @ohos.net.netFirewall(Network Firewall)

The **netFirewall** module implements the network firewall functionality for applications. It allows applications to query the firewall interception records of the device.

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
| [addNetFirewallRule(Network Firewall)](arkts-network-netfirewall-addnetfirewallrule-f.md) | Adds a firewall rule for the system user ID. The supported rule types are IP, Domain, and DNS. This API uses a promise to return the result. > **Description** > > 1. The priority of firewall rules is described as follows (there is no requirement on the call sequence of > [setNetFirePolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md) and > [addNetFirewallRule](arkts-network-netfirewall-addnetfirewallrule-f.md)): > > - Call [setNetFirePolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md) to set the default policy to **DENY** and call > [addNetFirewallRule](arkts-network-netfirewall-addnetfirewallrule-f.md) to add an explicit rule. The priorities of the rules > are as follows: > > - Explicit denying rule > > - Explicit allowing rule > > - Default denying policy > > - Call [setNetFirePolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md) to set the default policy to **ALLOW** and call > [addNetFirewallRule](arkts-network-netfirewall-addnetfirewallrule-f.md) to add an explicit rule. The priorities of the rules > are as follows: > > - Explicit allowing rule > > - Explicit denying rule > > - Default allowing policy > > - When the IP address rule and domain name rule of the firewall conflict (the IP of the domain name resolution is > the same as that in the IP address rule, and the rule behavior conflicts): > > - If the access is performed using a domain name, the domain name rule has a higher priority than the IP address > rule and is not affected by the rule of the IP parsed from the domain name. > > - If the access is performed using an IP address, the following rules are followed: > > - If the domain name rule allows the access and the domain name resolution has been performed, the IP address > denying rule or the default denying policy will not take effect, and the access using the IP address will be > allowed. > > - If the domain name rule allows the access and the domain name resolution has not been performed, the IP address > denying rule or the default denying policy will take effect, and the access using the IP address will be denied. > > - If the domain name rule denies the access, the IP address allowing rule or the default policy will take effect, > and the access using the IP address will be allowed. > > 2. Supplementary description of rule types: > > - When the input parameter **rule.type** of **addNetFirewallRule** is set to **RULE_IP**: > > - If **rule.action** is set to **RULE_ALLOW** and **rule.localIps** and **rule.remoteIps** are not configured, > the rule takes effect as full IP range access is allowed. > > - If **rule.action** is set to **RULE_DENY** and **rule.localIps** and **rule.remoteIps** are not configured, the > rule takes effect as full IP range access is denied. > > - If **rule.type** of **addNetFirewallRule** is set to **RULE_DOMAIN** and **rule.domains** is not configured, > the rule does not take effect. > > 3. Description of the upper limit for adding firewall rules: > > - A maximum of 1000 firewall rules can be added for a single system user ID. If this limit is exceeded, error > code **29400001** is reported. > > - A maximum of 2000 firewall rules can be added for all system user IDs. If this limit is exceeded, error code > **29400001** is reported. > > - A maximum of 100 fuzzy domain name rules can be added for all system user IDs. If this limit is exceeded, error > code **29400005** is reported. > **Required permission**: ohos.permission.MANAGE_NET_FIREWALL |
| [getNetFirewallPolicy(Network Firewall)](arkts-network-netfirewall-getnetfirewallpolicy-f.md) | Queries the firewall policy for a system user ID, including the firewall switch status and default inbound or outbound behavior (allow or deny). This API uses a promise to return the result. **Required permission**: ohos.permission.GET_NET_FIREWALL |
| [getNetFirewallRule(Network Firewall)](arkts-network-netfirewall-getnetfirewallrule-f.md) | Obtains a firewall rule based on the specified user ID and rule ID. This API uses a promise to return the result. **Required permission**: ohos.permission.GET_NET_FIREWALL |
| [getNetFirewallRules(Network Firewall)](arkts-network-netfirewall-getnetfirewallrules-f.md) | Obtains firewall rules by user ID. You need to specify the pagination query parameter when calling this API. Currently, firewall rules can be sorted by name. This API uses a promise to return the result. **Required permission**: ohos.permission.GET_NET_FIREWALL |
| [removeNetFirewallRule(Network Firewall)](arkts-network-netfirewall-removenetfirewallrule-f.md) | Deletes a specified firewall rule of a system user ID. This API uses a promise to return the result. **Required permission**: ohos.permission.MANAGE_NET_FIREWALL |
| [setNetFirewallPolicy(Network Firewall)](arkts-network-netfirewall-setnetfirewallpolicy-f.md) | Sets the firewall policy for a system user ID, including the firewall switch status and default inbound or outbound behavior (allow or deny). Different firewall policies can be configured for different system user IDs. This API uses a promise to return the result. > **NOTE：**> > If this API is called by multiple applications under the same system user, the latest delivered policy prevails. > **Required permission**: ohos.permission.MANAGE_NET_FIREWALL |
| [updateNetFirewallRule(Network Firewall)](arkts-network-netfirewall-updatenetfirewallrule-f.md) | Updates a firewall rule. This API uses a promise to return the result. **Required permission**: ohos.permission.MANAGE_NET_FIREWALL |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getInterceptedRecords(Network Firewall)](arkts-network-netfirewall-getinterceptedrecords-f-sys.md) | Get intercepted records by userId, and it is necessary to specify the pagination query parameters. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [FirewallRulePage(Network Firewall)](arkts-network-netfirewall-firewallrulepage-i.md) | Defines the pagination structure for firewall rules. |
| [NetFirewallDnsParams(Network Firewall)](arkts-network-netfirewall-netfirewalldnsparams-i.md) | Defines the DNS information of a firewall rule. > **Description** > > This parameter cannot be empty when **rule.type** of [addNetFirewallRule](arkts-network-netfirewall-addnetfirewallrule-f.md) > is set to RULE_DNS. |
| [NetFirewallDomainParams(Network Firewall)](arkts-network-netfirewall-netfirewalldomainparams-i.md) | Defines domain name parameters of a firewall rule. Currently, Chinese domain names are not supported. |
| [NetFirewallIpParams(Network Firewall)](arkts-network-netfirewall-netfirewallipparams-i.md) | Defines the IP parameters of the firewall rule. The IP address type can be IPv4 or IPv6. A single IP address or IP address segment is supported. |
| [NetFirewallPolicy(Network Firewall)](arkts-network-netfirewall-netfirewallpolicy-i.md) | Defines the firewall policy, including the firewall switch status and default inbound or outbound action (allow or deny). |
| [NetFirewallPortParams(Network Firewall)](arkts-network-netfirewall-netfirewallportparams-i.md) | Defines the port parameters of a firewall rule. |
| [NetFirewallRule(Network Firewall)](arkts-network-netfirewall-netfirewallrule-i.md) | Defines a firewall rule. |
| [RequestParam(Network Firewall)](arkts-network-netfirewall-requestparam-i.md) | Defines query parameters. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [InterceptedRecord(Network Firewall)](arkts-network-netfirewall-interceptedrecord-i-sys.md) | Intercepted record. |
| [InterceptedRecordPage(Network Firewall)](arkts-network-netfirewall-interceptedrecordpage-i-sys.md) | Intercepted record page information. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [FirewallRuleAction(Network Firewall)](arkts-network-netfirewall-firewallruleaction-e.md) | Enumerates the firewall rule actions, including allowing or denying network connections. |
| [NetFirewallOrderField(Network Firewall)](arkts-network-netfirewall-netfirewallorderfield-e.md) | Enumerates the sorting methods of firewall rules. > **Description** > > [getNetFirewallRules](arkts-network-netfirewall-getnetfirewallrules-f.md) supports only the **ORDER_BY_RULE_NAME** field. |
| [NetFirewallOrderType(Network Firewall)](arkts-network-netfirewall-netfirewallordertype-e.md) | Enumerates the sorting order of firewall rules, which can be ascending or descending. |
| [NetFirewallRuleDirection(Network Firewall)](arkts-network-netfirewall-netfirewallruledirection-e.md) | Enumerates the firewall rule directions, including inbound and outbound. |
| [NetFirewallRuleType(Network Firewall)](arkts-network-netfirewall-netfirewallruletype-e.md) | Enumerates the firewall rule types, including IP, Domain, and DNS. |

