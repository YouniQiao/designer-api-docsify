# getNetFirewallRule

## Modules to Import

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## getNetFirewallRule

```TypeScript
function getNetFirewallRule(userId: number, ruleId: number): Promise<NetFirewallRule>
```

Get a specified firewall rule by userId and ruleId.

**Since:** 15

**Required permissions:** ohos.permission.GET_NET_FIREWALL

<!--Device-netFirewall-function getNetFirewallRule(userId: number, ruleId: number): Promise<NetFirewallRule>--><!--Device-netFirewall-function getNetFirewallRule(userId: number, ruleId: number): Promise<NetFirewallRule>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| ruleId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;NetFirewallRule&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [29400000](../errorcode-net-netfirewall.md#29400000-specified-user-does-not-exist) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [29400006](../errorcode-net-netfirewall.md#29400006-specified-rule-does-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

netFirewall.getNetFirewallRule(100, 1).then((rule: netFirewall.NetFirewallRule) => {
  console.info("result:", JSON.stringify(rule));
}).catch((error : BusinessError) => {
  console.error(" get firewall rules failed: " + JSON.stringify(error));
});
```
