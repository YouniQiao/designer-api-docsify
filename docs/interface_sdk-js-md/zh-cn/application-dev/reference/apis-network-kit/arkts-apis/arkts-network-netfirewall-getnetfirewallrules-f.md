# getNetFirewallRules

## 导入模块

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## getNetFirewallRules

```TypeScript
function getNetFirewallRules(userId: number, requestParam: RequestParam): Promise<FirewallRulePage>
```

按用户ID获取防火墙规则，需要指定分页查询参数。目前支持根据防火墙规则名排序。使用Promise异步回调。

**起始版本：** 15

**需要权限：** ohos.permission.GET_NET_FIREWALL

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| requestParam | [RequestParam](arkts-network-netfirewall-requestparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FirewallRulePage](arkts-network-netfirewall-firewallrulepage-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [29400000](../errorcode-net-netfirewall.md#29400000-指定用户不存在) |
