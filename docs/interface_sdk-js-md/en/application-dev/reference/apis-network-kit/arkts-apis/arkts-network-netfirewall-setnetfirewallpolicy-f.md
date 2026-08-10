# setNetFirewallPolicy

## Modules to Import

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## setNetFirewallPolicy

```TypeScript
function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>
```

Set firewall policy by userId.&lt;p&gt;Enables or disables the firewall function, and specifies the default actions for inbound connections and outbound connections.&lt;/p&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Required permissions:** ohos.permission.MANAGE_NET_FIREWALL

<!--Device-netFirewall-function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>--><!--Device-netFirewall-function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | Indicates the user ID. It cannot be the ID of a user that does not exist. |
| policy | [NetFirewallPolicy](arkts-network-netfirewall-netfirewallpolicy-i.md) | Yes | The firewall policy to be set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns void. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 29400000 | The specified user does not exist. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Operation failed. Cannot connect to service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |

## Examples

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

