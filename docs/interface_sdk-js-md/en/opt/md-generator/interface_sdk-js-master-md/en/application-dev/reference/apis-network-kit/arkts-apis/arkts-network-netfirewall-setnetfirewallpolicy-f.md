# setNetFirewallPolicy

## Modules to Import

```TypeScript
```

## setNetFirewallPolicy

```TypeScript
function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>
```

Set firewall policy by userId. &lt;p&gt;Enables or disables the firewall function, and specifies the default actions for inbound connections and outbound connections.&lt;/p&gt;

**Since:** 15

**Required permissions:** ohos.permission.MANAGE_NET_FIREWALL

<!--Device-netFirewall-function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>--><!--Device-netFirewall-function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| policy | [NetFirewallPolicy](arkts-network-netfirewall-netfirewallpolicy-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [29400000](../errorcode-net-netfirewall.md#29400000-specified-user-does-not-exist) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let policy: netFirewall.NetFirewallPolicy = {
  isOpen: true,
  inAction: netFirewall.FirewallRuleAction.RULE_DENY,
  outAction: netFirewall.FirewallRuleAction.RULE_ALLOW
};
netFirewall.setNetFirewallPolicy(100, policy).then(() => {
  console.info("set firewall policy success.");
}).catch((error : BusinessError) => {
  console.error("set firewall policy failed: " + JSON.stringify(error));
});
```
