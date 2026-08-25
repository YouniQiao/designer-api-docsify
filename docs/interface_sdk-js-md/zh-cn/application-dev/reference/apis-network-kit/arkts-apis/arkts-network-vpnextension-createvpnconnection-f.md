# createVpnConnection

## 导入模块

```TypeScript
import { vpnExtension } from '@kit.NetworkKit';
```

## createVpnConnection

```TypeScript
function createVpnConnection(context: VpnExtensionContext): VpnConnection
```

创建一个三方VPN连接对象。

> **说明：**&gt;
> 调用createVpnConnection接口前，需要先调用startVpnExtensionAbility接口启用VPN功能。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [VpnExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-common-vpnextensioncontext-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [VpnConnection](arkts-network-vpnextension-vpnconnection-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
