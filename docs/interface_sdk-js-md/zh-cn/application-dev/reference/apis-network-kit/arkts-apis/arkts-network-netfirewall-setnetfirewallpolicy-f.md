# setNetFirewallPolicy

## 导入模块

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## setNetFirewallPolicy

```TypeScript
function setNetFirewallPolicy(userId: number, policy: NetFirewallPolicy): Promise<void>
```

设置系统用户ID的防火墙策略，包含防火墙开关状态，默认的出站/入站行为（允许/阻止）。支持不同的系统用户ID配置不同的防火墙策略。使用Promise异步回调。

> **说明：**&gt;
> 同一系统用户下，多应用调用该接口下发策略，会以最新下发的策略为准。

**起始版本：** 15

**需要权限：** ohos.permission.MANAGE_NET_FIREWALL

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| policy | [NetFirewallPolicy](arkts-network-netfirewall-netfirewallpolicy-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [29400000](../errorcode-net-netfirewall.md#29400000-指定用户不存在) |
