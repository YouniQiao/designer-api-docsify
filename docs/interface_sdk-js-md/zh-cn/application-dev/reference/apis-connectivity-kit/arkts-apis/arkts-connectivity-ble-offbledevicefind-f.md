# offBLEDeviceFind

## 导入模块

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## offBLEDeviceFind

```TypeScript
function offBLEDeviceFind(callback?: Callback<Array<ScanResult>>): void
```

Unsubscribe BLE scan result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ble-function offBLEDeviceFind(callback?: Callback<Array<ScanResult>>): void--><!--Device-ble-function offBLEDeviceFind(callback?: Callback<Array<ScanResult>>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ScanResult&gt;&gt; | 否 | Callback used to listen for the scan result event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2900099 | Operation failed. |

