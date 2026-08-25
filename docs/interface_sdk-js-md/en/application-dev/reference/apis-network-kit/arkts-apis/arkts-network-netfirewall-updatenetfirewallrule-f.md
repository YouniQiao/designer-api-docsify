# updateNetFirewallRule

## Modules to Import

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## updateNetFirewallRule

```TypeScript
function updateNetFirewallRule(rule: NetFirewallRule): Promise<void>
```

Updates a firewall rule. This API uses a promise to return the result.  
**Required permission**: ohos.permission.MANAGE_NET_FIREWALL

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
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [29400000](../errorcode-net-netfirewall.md#29400000-specified-user-does-not-exist) |
| [29400002](../errorcode-net-netfirewall.md#29400002-number-of-ip-address-rules-in-the-firewall-rule-exceeds-the-maximum) |
| [29400003](../errorcode-net-netfirewall.md#29400003-number-of-port-rules-in-the-firewall-rule-exceeds-the-maximum) |
| [29400004](../errorcode-net-netfirewall.md#29400004-number-of-domain-name-rules-in-the-firewall-rule-exceeds-the-maximum) |
| [29400005](../errorcode-net-netfirewall.md#29400005-number-of-fuzzy-domain-name-rules-exceeds-the-maximum) |
| [29400006](../errorcode-net-netfirewall.md#29400006-specified-rule-does-not-exist) |
| [29400007](../errorcode-net-netfirewall.md#29400007-dns-rule-duplication) |
