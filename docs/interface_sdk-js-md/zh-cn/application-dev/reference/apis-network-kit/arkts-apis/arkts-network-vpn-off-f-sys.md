# off（系统接口）

## 导入模块

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## off('connect')

```TypeScript
function off(type: 'connect', callback?: Callback<VpnConnectState>): void
```

Unsubscribes from vpn connect state changes.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**需要权限：** ohos.permission.MANAGE_VPN

<!--Device-vpn-function off(type: 'connect', callback?: Callback<VpnConnectState>): void--><!--Device-vpn-function off(type: 'connect', callback?: Callback<VpnConnectState>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'connect' | 是 | Indicates vpn connect state changes. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VpnConnectState&gt; | 否 | The callback of the vpn connect state. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Operation failed. Cannot connect to service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |


## off('connectMulti')

```TypeScript
function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void
```

Unsubscribes from vpn connect state changes.

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

**需要权限：** ohos.permission.MANAGE_VPN

<!--Device-vpn-function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void--><!--Device-vpn-function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'connectMulti' | 是 | Indicates multi vpn connect state changes. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MultiVpnConnectState&gt; | 否 | The callback of the multi vpn connect state. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 19900002 | System internal error. |
| 19900001 | Invalid parameter value. |

