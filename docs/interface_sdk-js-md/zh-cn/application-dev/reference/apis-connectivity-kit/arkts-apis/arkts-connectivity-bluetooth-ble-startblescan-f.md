# startBLEScan

## 导入模块

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## startBLEScan

```TypeScript
function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void
```

发起BLE扫描流程。

从API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [startBLEScan](arkts-connectivity-bluetoothmanager-ble-startblescan-f.md)

**需要权限：** ohos.permission.DISCOVER_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH and ohos.permission.LOCATION

<!--Device-BLE-function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void--><!--Device-BLE-function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filters | Array&lt;ScanFilter&gt; | 是 | 表示扫描结果过滤策略集合，如果不使用过滤的方式，该参数设置为null。 |
| options | ScanOptions | 否 | 表示扫描的参数配置，可选参数。 |

**示例**

```TypeScript
function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('BLE scan device find result = '+ JSON.stringify(data));
}
bluetooth.BLE.on("BLEDeviceFind", onReceiveEvent);
let scanOptions : bluetooth.ScanOptions = {
    interval: 500,
    dutyMode: bluetooth.ScanDuty.SCAN_MODE_LOW_POWER,
    matchMode: bluetooth.MatchMode.MATCH_MODE_AGGRESSIVE,
}

let scanFilter : bluetooth.ScanFilter = {
    deviceId:"XX:XX:XX:XX:XX:XX",
    name:"test",
    serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
}
bluetooth.BLE.startBLEScan(
    [scanFilter], scanOptions
);
```
