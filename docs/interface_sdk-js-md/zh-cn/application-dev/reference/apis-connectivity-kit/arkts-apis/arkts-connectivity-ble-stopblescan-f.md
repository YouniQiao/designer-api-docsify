# stopBLEScan

## 导入模块

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## stopBLEScan

```TypeScript
function stopBLEScan(): void
```

停止BLE扫描流程。

停止的BLE扫描由[ble.startBLEScan](arkts-connectivity-ble-startblescan-f.md)触发。当应用不再需要扫描BLE设备时，需主动调用该方法停止扫描。调用此接口后将不再收到扫描结果上报，重新开启BLE扫描即可再次扫到BLE设备。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ble-function stopBLEScan(): void--><!--Device-ble-function stopBLEScan(): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| [2900001](../errorcode-bluetoothManager.md#2900001-蓝牙服务停止) | Service stopped. |
| [2900003](../errorcode-bluetoothManager.md#2900003-蓝牙开关关闭) | Bluetooth disabled. |
| [2900099](../errorcode-bluetoothManager.md#2900099-操作失败) | Operation failed. |

**示例**

```TypeScript
try {
    ble.stopBLEScan();
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
