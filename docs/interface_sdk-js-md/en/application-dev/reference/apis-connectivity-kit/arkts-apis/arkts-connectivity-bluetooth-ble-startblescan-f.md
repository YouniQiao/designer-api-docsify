# startBLEScan

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## startBLEScan

```TypeScript
function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void
```

Starts scanning for specified BLE devices with filters.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [startBLEScan](arkts-connectivity-bluetoothmanager-ble-startblescan-f.md)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH and ohos.permission.LOCATION

<!--Device-BLE-function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void--><!--Device-BLE-function startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filters | Array&lt;ScanFilter&gt; | Yes | Indicates the list of filters used to filter out specified devices. If you do not want to use filter, set this parameter to `null`. |
| options | ScanOptions | No | Indicates the parameters for scanning and if the user does not assign a value, the default value will be used. [interval](arkts-connectivity-bluetooth-scanoptions-i.md#interval) set to 0, [dutyMode](arkts-connectivity-bluetooth-scanoptions-i.md#dutymode) set to [SCAN_MODE_LOW_POWER](arkts-connectivity-bluetooth-scanduty-e.md#scan_mode_low_power) and [matchMode](arkts-connectivity-bluetooth-scanoptions-i.md#matchmode) set to [MATCH_MODE_AGGRESSIVE](arkts-connectivity-bluetooth-matchmode-e.md#match_mode_aggressive). |

**Examples**

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
