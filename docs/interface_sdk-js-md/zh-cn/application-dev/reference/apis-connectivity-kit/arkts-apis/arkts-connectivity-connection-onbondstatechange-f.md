# onBondStateChange

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## onBondStateChange

```TypeScript
function onBondStateChange(callback: Callback<BondStateParam>): void
```

Subscribe the event reported when a remote Bluetooth device is bonded.On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC,the type of the peer device address is real.Otherwise, the type of the peer device address is virtual.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** 
- API版本26.0.0+：ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)
- API版本23 - 24：ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function onBondStateChange(callback: Callback<BondStateParam>): void--><!--Device-connection-function onBondStateChange(callback: Callback<BondStateParam>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BondStateParam&gt; | 是 | Callback used to listen for the bond state event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2900099 | Operation failed. |

