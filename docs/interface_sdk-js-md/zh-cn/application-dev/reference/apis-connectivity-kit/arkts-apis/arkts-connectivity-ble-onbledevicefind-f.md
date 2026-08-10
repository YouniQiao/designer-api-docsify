# onBLEDeviceFind

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## onBLEDeviceFind

```TypeScript
function onBLEDeviceFind(callback: Callback<Array<ScanResult>>): void
```

Subscribe BLE scan result.If the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real.Otherwise, the type of the peer device address is virtual.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ble-function onBLEDeviceFind(callback: Callback<Array<ScanResult>>): void--><!--Device-ble-function onBLEDeviceFind(callback: Callback<Array<ScanResult>>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ScanResult&gt;&gt; | 是 | Callback used to listen for the scan result event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2900099 | Operation failed. |

