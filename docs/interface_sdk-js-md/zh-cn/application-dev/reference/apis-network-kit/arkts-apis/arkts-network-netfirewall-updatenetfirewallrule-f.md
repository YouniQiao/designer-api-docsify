# updateNetFirewallRule

## 导入模块

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## updateNetFirewallRule

```TypeScript
function updateNetFirewallRule(rule: NetFirewallRule): Promise<void>
```

更新防火墙规则。使用Promise异步回调。

**起始版本：** 15

**需要权限：** ohos.permission.MANAGE_NET_FIREWALL

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rule | [NetFirewallRule](arkts-network-netfirewall-netfirewallrule-i.md) | 是 |

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
| [29400002](../errorcode-net-netfirewall.md#29400002-防火墙规则中的ip地址规则数量超过最大值) |
| [29400003](../errorcode-net-netfirewall.md#29400003-防火墙规则中的port规则数量超过最大值) |
| [29400004](../errorcode-net-netfirewall.md#29400004-防火墙规则中的域名规则数量超过最大值) |
| [29400005](../errorcode-net-netfirewall.md#29400005-模糊域名规则数量超过最大值) |
| [29400006](../errorcode-net-netfirewall.md#29400006-指定的规则不存在) |
| [29400007](../errorcode-net-netfirewall.md#29400007-dns规则重复) |
