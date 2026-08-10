# createVpnConnection

## 导入模块

```TypeScript
import { vpnExtension } from 'kits/@kit.NetworkKit';
```

## createVpnConnection

```TypeScript
function createVpnConnection(context: VpnExtensionContext): VpnConnection
```

Create a VPN connection using the VpnExtensionContext.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-vpnExtension-function createVpnConnection(context: VpnExtensionContext): VpnConnection--><!--Device-vpnExtension-function createVpnConnection(context: VpnExtensionContext): VpnConnection-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VpnExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-common-vpnextensioncontext-t.md) | 是 | Indicates the context of application or capability. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VpnConnection](arkts-network-vpnextension-vpnconnection-i.md) | the VpnConnection of the construct VpnConnection instance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

