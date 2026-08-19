# off_bluetoothDeviceFind

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## off_bluetoothDeviceFind('bluetoothDeviceFind')

```TypeScript
function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void
```

Unsubscribe the event reported when a remote Bluetooth device is discovered. On API 10 and above, the permission required by this interface is changed from USE_BLUETOOTH to ACCESS_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** bluetoothDeviceFind

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH
- API version 9: ohos.permission.USE_BLUETOOTH

<!--Device-bluetoothManager-function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void--><!--Device-bluetoothManager-function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bluetoothDeviceFind' | Yes | Type of the discovering event to listen for. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | No | Callback used to listen for the discovering event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<string>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
    bluetoothManager.off('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

