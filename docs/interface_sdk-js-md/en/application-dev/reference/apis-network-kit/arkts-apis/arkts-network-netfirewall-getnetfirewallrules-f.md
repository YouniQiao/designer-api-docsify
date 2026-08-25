# getNetFirewallRules

## Modules to Import

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## getNetFirewallRules

```TypeScript
function getNetFirewallRules(userId: number, requestParam: RequestParam): Promise<FirewallRulePage>
```

Obtains firewall rules by user ID. You need to specify the pagination query parameter when calling this API. Currently, firewall rules can be sorted by name. This API uses a promise to return the result.  
**Required permission**: ohos.permission.GET_NET_FIREWALL

**Since:** 15

**Required permissions:** ohos.permission.GET_NET_FIREWALL

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| requestParam | [RequestParam](arkts-network-netfirewall-requestparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FirewallRulePage](arkts-network-netfirewall-firewallrulepage-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [29400000](../errorcode-net-netfirewall.md#29400000-specified-user-does-not-exist) |
