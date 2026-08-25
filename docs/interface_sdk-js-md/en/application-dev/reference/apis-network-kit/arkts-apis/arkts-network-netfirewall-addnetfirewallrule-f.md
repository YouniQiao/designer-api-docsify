# addNetFirewallRule

## Modules to Import

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## addNetFirewallRule

```TypeScript
function addNetFirewallRule(rule: NetFirewallRule): Promise<number>
```

Adds a firewall rule for the system user ID. The supported rule types are IP, Domain, and DNS. This API uses a promise to return the result.

> **Description**&gt;
> 1. The priority of firewall rules is described as follows (there is no requirement on the call sequence of
> [setNetFirePolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md) and
> [addNetFirewallRule](#addnetfirewallrule)):&gt;
> - Call [setNetFirePolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md) to set the default policy to **DENY** and call
> [addNetFirewallRule](#addnetfirewallrule) to add an explicit rule. The priorities of the rules
> are as follows:&gt;
> - Explicit denying rule&gt;
> - Explicit allowing rule&gt;
> - Default denying policy&gt;
> - Call [setNetFirePolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md) to set the default policy to **ALLOW** and call
> [addNetFirewallRule](#addnetfirewallrule) to add an explicit rule. The priorities of the rules
> are as follows:&gt;
> - Explicit allowing rule&gt;
> - Explicit denying rule&gt;
> - Default allowing policy&gt;
> - When the IP address rule and domain name rule of the firewall conflict (the IP of the domain name resolution is
> the same as that in the IP address rule, and the rule behavior conflicts):&gt;
> - If the access is performed using a domain name, the domain name rule has a higher priority than the IP address
> rule and is not affected by the rule of the IP parsed from the domain name.&gt;
> - If the access is performed using an IP address, the following rules are followed:&gt;
> - If the domain name rule allows the access and the domain name resolution has been performed, the IP address
> denying rule or the default denying policy will not take effect, and the access using the IP address will be
> allowed.&gt;
> - If the domain name rule allows the access and the domain name resolution has not been performed, the IP address
> denying rule or the default denying policy will take effect, and the access using the IP address will be denied.&gt;
> - If the domain name rule denies the access, the IP address allowing rule or the default policy will take effect,
> and the access using the IP address will be allowed.&gt;
> 2. Supplementary description of rule types:&gt;
> - When the input parameter **rule.type** of **addNetFirewallRule** is set to **RULE_IP**:&gt;
> - If **rule.action** is set to **RULE_ALLOW** and **rule.localIps** and **rule.remoteIps** are not configured,
> the rule takes effect as full IP range access is allowed.&gt;
> - If **rule.action** is set to **RULE_DENY** and **rule.localIps** and **rule.remoteIps** are not configured, the
> rule takes effect as full IP range access is denied.&gt;
> - If **rule.type** of **addNetFirewallRule** is set to **RULE_DOMAIN** and **rule.domains** is not configured,
> the rule does not take effect.&gt;
> 3. Description of the upper limit for adding firewall rules:&gt;
> - A maximum of 1000 firewall rules can be added for a single system user ID. If this limit is exceeded, error
> code **29400001** is reported.&gt;
> - A maximum of 2000 firewall rules can be added for all system user IDs. If this limit is exceeded, error code
> **29400001** is reported.&gt;
> - A maximum of 100 fuzzy domain name rules can be added for all system user IDs. If this limit is exceeded, error
> code **29400005** is reported.
> **Required permission**: ohos.permission.MANAGE_NET_FIREWALL

**Since:** 15

**Required permissions:** ohos.permission.MANAGE_NET_FIREWALL

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rule | [NetFirewallRule](arkts-network-netfirewall-netfirewallrule-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [29400000](../errorcode-net-netfirewall.md#29400000-specified-user-does-not-exist) |
| [29400001](../errorcode-net-netfirewall.md#29400001-number-of-firewall-rules-exceeds-the-maximum) |
| [29400002](../errorcode-net-netfirewall.md#29400002-number-of-ip-address-rules-in-the-firewall-rule-exceeds-the-maximum) |
| [29400003](../errorcode-net-netfirewall.md#29400003-number-of-port-rules-in-the-firewall-rule-exceeds-the-maximum) |
| [29400004](../errorcode-net-netfirewall.md#29400004-number-of-domain-name-rules-in-the-firewall-rule-exceeds-the-maximum) |
| [29400005](../errorcode-net-netfirewall.md#29400005-number-of-fuzzy-domain-name-rules-exceeds-the-maximum) |
| [29400007](../errorcode-net-netfirewall.md#29400007-dns-rule-duplication) |
