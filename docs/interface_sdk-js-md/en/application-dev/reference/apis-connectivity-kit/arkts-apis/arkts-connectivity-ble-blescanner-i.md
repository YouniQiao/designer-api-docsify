# BleScanner

Manages the ble scanner.Before calling a ble scanner method, you must use [createBleScanner](arkts-connectivity-ble-createblescanner-f.md#createBleScanner) to create an BleScanner instance.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-ble-interface BleScanner--><!--Device-ble-interface BleScanner-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## off('BLEDeviceFind')

```TypeScript
off(type: 'BLEDeviceFind', callback?: Callback<ScanReport>): void
```

Unsubscribe BLE scan result.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-BleScanner-off(type: 'BLEDeviceFind', callback?: Callback<ScanReport>): void--><!--Device-BleScanner-off(type: 'BLEDeviceFind', callback?: Callback<ScanReport>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'BLEDeviceFind' | Yes | Type of the scan result event to listen for. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ScanReport](arkts-connectivity-ble-scanreport-i.md)&gt; | No | Callback used to listen for the scan result event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { ble } from '@kit.ConnectivityKit';
function onReceiveEvent(scanReport: ble.ScanReport) {
    console.info('bluetooth device find = '+ JSON.stringify(scanReport));
}
let bleScanner: ble.BleScanner = ble.createBleScanner();
try {
    bleScanner.on('BLEDeviceFind', onReceiveEvent);
    bleScanner.off('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## on('BLEDeviceFind')

```TypeScript
on(type: 'BLEDeviceFind', callback: Callback<ScanReport>): void
```

Subscribe BLE scan result.On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC,the type of the peer device address is real. Otherwise, the type of the peer device address is virtual.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 26.0.0.

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)
- API version 15 - 24: ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-BleScanner-on(type: 'BLEDeviceFind', callback: Callback<ScanReport>): void--><!--Device-BleScanner-on(type: 'BLEDeviceFind', callback: Callback<ScanReport>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'BLEDeviceFind' | Yes | Type of the scan result event to listen for. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ScanReport](arkts-connectivity-ble-scanreport-i.md)&gt; | Yes | Callback used to listen for the scan result event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.<br>**Applicable version:** 15 - 24 |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { ble } from '@kit.ConnectivityKit';
function onReceiveEvent(scanReport: ble.ScanReport) {
    console.info('bluetooth device find = '+ JSON.stringify(scanReport));
}
let bleScanner: ble.BleScanner = ble.createBleScanner();
try {
    bleScanner.on('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## startScan

```TypeScript
startScan(filters: Array<ScanFilter>, options?: ScanOptions): Promise<void>
```

Starts scanning for specified BLE devices with filters.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-BleScanner-startScan(filters: Array<ScanFilter>, options?: ScanOptions): Promise<void>--><!--Device-BleScanner-startScan(filters: Array<ScanFilter>, options?: ScanOptions): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filters | Array&lt;ScanFilter&gt; | Yes | Indicates the list of filters used to filter out specified devices. If you do not want to use filter, set this parameter to {@code null}. |
| options | ScanOptions | No | Indicates the parameters for scanning and if the user does not assign a value, the default value will be used. [interval](arkts-connectivity-ble-scanoptions-i.md#interval) set to 0, and [dutyMode](arkts-connectivity-ble-scanoptions-i.md#dutyMode) set to [SCAN_MODE_LOW_POWER](arkts-connectivity-ble-scanduty-e.md#SCAN_MODE_LOW_POWER) and [matchMode](arkts-connectivity-ble-scanoptions-i.md#matchMode) set to [MATCH_MODE_AGGRESSIVE](arkts-connectivity-ble-matchmode-e.md#MATCH_MODE_AGGRESSIVE). and [phyType](arkts-connectivity-ble-scanoptions-i.md#phyType) set to [PHY_LE_ALL_SUPPORTED](arkts-connectivity-ble-phytype-e.md#PHY_LE_ALL_SUPPORTED). and [reportMode](arkts-connectivity-ble-scanoptions-i.md#reportMode) set to [NORMAL](arkts-connectivity-ble-scanreportmode-e.md#NORMAL). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| 2900009 | Fails to start scan as it is out of hardware resources. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900001 | Service stopped. |
| 2902050 | Failed to start scan as Ble scan is already started by the app. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { ble } from '@kit.ConnectivityKit';
let bleScanner: ble.BleScanner = ble.createBleScanner();
function onReceiveEvent(scanReport: ble.ScanReport) {
    console.info('BLE scan device find result = '+ JSON.stringify(scanReport));
}
async function startscan() {
    try {
        bleScanner.on("BLEDeviceFind", onReceiveEvent);
        let scanFilter: ble.ScanFilter = {
            deviceId:"XX:XX:XX:XX:XX:XX",
            name:"test",
            serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
        };
        let scanOptions: ble.ScanOptions = {
            interval: 500,
            dutyMode: ble.ScanDuty.SCAN_MODE_LOW_POWER,
            matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE,
            reportMode: ble.ScanReportMode.FENCE_SENSITIVITY_LOW
        }
        await bleScanner.startScan([scanFilter],scanOptions);
        console.info('startScan success');
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
}
startscan();
```

## startScan

```TypeScript
startScan(filters: Array<ScanFilter> | null, options?: ScanOptions): Promise<void>
```

Starts scanning for specified BLE devices with filters.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-BleScanner-startScan(filters: Array<ScanFilter> | null, options?: ScanOptions): Promise<void>--><!--Device-BleScanner-startScan(filters: Array<ScanFilter> | null, options?: ScanOptions): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filters | Array&lt;ScanFilter&gt; \| null | Yes | Indicates the list of filters used to filter out specified devices. If you do not want to use filter, set this parameter to {@code null}. |
| options | ScanOptions | No | Indicates the parameters for scanning and if the user does not assign a value, the default value will be used. [interval](arkts-connectivity-ble-scanoptions-i.md#interval) set to 0, and [dutyMode](arkts-connectivity-ble-scanoptions-i.md#dutyMode) set to [SCAN_MODE_LOW_POWER](arkts-connectivity-ble-scanduty-e.md#SCAN_MODE_LOW_POWER) and [matchMode](arkts-connectivity-ble-scanoptions-i.md#matchMode) set to [MATCH_MODE_AGGRESSIVE](arkts-connectivity-ble-matchmode-e.md#MATCH_MODE_AGGRESSIVE). and [phyType](arkts-connectivity-ble-scanoptions-i.md#phyType) set to [PHY_LE_ALL_SUPPORTED](arkts-connectivity-ble-phytype-e.md#PHY_LE_ALL_SUPPORTED). and [reportMode](arkts-connectivity-ble-scanoptions-i.md#reportMode) set to [NORMAL](arkts-connectivity-ble-scanreportmode-e.md#NORMAL). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| 2900009 | Fails to start scan as it is out of hardware resources. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900001 | Service stopped. |
| 2902050 | Failed to start scan as Ble scan is already started by the app. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## stopScan

```TypeScript
stopScan(): Promise<void>
```

Stops BLE scanning.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-BleScanner-stopScan(): Promise<void>--><!--Device-BleScanner-stopScan(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { ble } from '@kit.ConnectivityKit';
let bleScanner: ble.BleScanner = ble.createBleScanner();
async function stopScan() {
    try {
        await bleScanner.stopScan();
        console.info('stopScan success');
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
}
stopScan();
```

