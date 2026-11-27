# off

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## off('BLEDeviceFind')

```TypeScript
function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void
```

Unsubscribe BLE scan result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** BLEDeviceFind

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-BLE-function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void--><!--Device-BLE-function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'BLEDeviceFind' | Yes | Type of the scan result event to listen for. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ScanResult&gt;&gt; | No | Callback used to listen for the scan result event. |

**Examples**

```TypeScript
function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.BLE.on('BLEDeviceFind', onReceiveEvent);
bluetooth.BLE.off('BLEDeviceFind', onReceiveEvent);
```
