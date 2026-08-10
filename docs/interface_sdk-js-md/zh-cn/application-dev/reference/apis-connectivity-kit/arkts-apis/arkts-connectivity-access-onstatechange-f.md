# onStateChange

## 导入模块

```TypeScript
import { access } from 'kits/@kit.ConnectivityKit';
```

## onStateChange

```TypeScript
function onStateChange(callback: Callback<BluetoothState>): void
```

Subscribe the event reported when the Bluetooth state changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-access-function onStateChange(callback: Callback<BluetoothState>): void--><!--Device-access-function onStateChange(callback: Callback<BluetoothState>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BluetoothState&gt; | 是 | Callback used to listen for the Bluetooth state event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

