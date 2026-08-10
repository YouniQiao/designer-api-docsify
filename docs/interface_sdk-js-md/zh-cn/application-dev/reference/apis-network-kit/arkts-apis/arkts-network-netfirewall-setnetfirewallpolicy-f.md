# setNetFirewallPolicy

## 导入模块

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## setNetFirewallPolicy

```TypeScript
function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>
```

Set firewall policy by userId.&lt;p&gt;Enables or disables the firewall function, and specifies the default actions for inbound connections and outbound connections.&lt;/p&gt;

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

**需要权限：** ohos.permission.MANAGE_NET_FIREWALL

<!--Device-netFirewall-function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>--><!--Device-netFirewall-function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | Indicates the user ID. It cannot be the ID of a user that does not exist. |
| policy | [NetFirewallPolicy](arkts-network-netfirewall-netfirewallpolicy-i.md) | 是 | The firewall policy to be set. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Returns void. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 29400000 | The specified user does not exist. |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Operation failed. Cannot connect to service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |

## 示例

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

