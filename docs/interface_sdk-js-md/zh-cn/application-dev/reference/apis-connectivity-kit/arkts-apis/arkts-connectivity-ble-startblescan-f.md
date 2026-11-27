# startBLEScan

## 导入模块

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## startBLEScan

```TypeScript
function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void
```

发起BLE扫描流程。

扫描结果会通过[ble.on('BLEDeviceFind')](arkts-connectivity-ble-on-f.md#onbledevicefind)的回调函数获取到。只能扫描BLE设备，调用[ble.stopBLEScan](arkts-connectivity-ble-stopblescan-f.md)可以停止该方法开启的扫描流程。该接口只支持单路扫描，即应用同时只能调用一次，下一次调用前，需要先调用[ble.stopBLEScan](arkts-connectivity-ble-stopblescan-f.md)停止上一次的扫描流程。若需要使用多路扫描，可使用[BleScanner](arkts-connectivity-ble-blescanner-i.md)。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ble-function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void--><!--Device-ble-function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filters | Array&lt;[ScanFilter](arkts-connectivity-ble-scanfilter-i.md)&gt; | 是 | 表示扫描结果过滤策略集合，符合过滤条件的设备会被保留。若该参数设置为null，将扫描所有可发现的周边BLE设备，但是不建议使用此方式，可能扫描到非预期设备，并增加功耗。 |
| options | [ScanOptions](arkts-connectivity-ble-scanoptions-i.md) | 否 | 表示扫描的参数配置。不填写时使用默认配置。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../errorcode-universal.md#401-函数参数数量或参数类型不匹配) | [Sync] Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| [2900001](../errorcode-bluetoothManager.md#2900001-蓝牙服务停止) | Service stopped. |
| [2900003](../errorcode-bluetoothManager.md#2900003-蓝牙开关关闭) | Bluetooth disabled. |
| [2900099](../errorcode-bluetoothManager.md#2900099-操作失败) | Operation failed. |

**示例**

```TypeScript
import { common } from '@kit.ConnectivityKit';
function onReceiveEvent(data: Array<ble.ScanResult>) {
    console.info('BLE scan device find result = '+ JSON.stringify(data));
}
try {
    ble.on("BLEDeviceFind", onReceiveEvent);
    let addressInfo : common.BluetoothAddress = {
        address:"XX:XX:XX:XX:XX:XX",
        addressType:common.BluetoothAddressType.REAL,
        rawAddressType:common.BluetoothRawAddressType.PUBLIC
    }
    let scanFilter: ble.ScanFilter = {
        deviceId:"XX:XX:XX:XX:XX:XX",
        address:addressInfo, // 使用address时不需要重复设置deviceId
        name:"test",
        serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
    };
    let scanOptions: ble.ScanOptions = {
    interval: 500,
    dutyMode: ble.ScanDuty.SCAN_MODE_LOW_POWER,
    matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE
    }
    ble.startBLEScan([scanFilter],scanOptions);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
