# createVpnConnection（系统接口）

## 导入模块

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## createVpnConnection

```TypeScript
function createVpnConnection(context: AbilityContext): VpnConnection
```

创建一个 VPN 连接对象。

**起始版本：** 10

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [AbilityContext](arkts-network-vpn-abilitycontext-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [VpnConnection](arkts-network-vpnextension-vpnconnection-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
