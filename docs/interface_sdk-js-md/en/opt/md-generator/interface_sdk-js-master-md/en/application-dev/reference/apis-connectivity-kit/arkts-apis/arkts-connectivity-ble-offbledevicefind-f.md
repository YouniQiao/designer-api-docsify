# off_BLEDeviceFind

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## off_BLEDeviceFind

```TypeScript
function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void
```

Unsubscribe BLE scan result. On API 10 and above, the permission required by this interface is changed from USE_BLUETOOTH to ACCESS_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** BLEDeviceFind

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH
- API version 9: ohos.permission.USE_BLUETOOTH

<!--Device-BLE-function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void--><!--Device-BLE-function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'BLEDeviceFind' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ScanResult&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.BLE.on('BLEDeviceFind', onReceiveEvent);
    bluetoothManager.BLE.off('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```
