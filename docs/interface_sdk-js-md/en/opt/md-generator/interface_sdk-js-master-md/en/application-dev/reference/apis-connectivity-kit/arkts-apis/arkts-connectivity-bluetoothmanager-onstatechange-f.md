# on_stateChange

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## on_stateChange

```TypeScript
function on(type: 'stateChange', callback: Callback<BluetoothState>): void
```

Subscribe the event reported when the Bluetooth state changes. On API 10 and above, the permission required by this interface is changed from USE_BLUETOOTH to ACCESS_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** stateChange

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH
- API version 9: ohos.permission.USE_BLUETOOTH

<!--Device-bluetoothManager-function on(type: 'stateChange', callback: Callback<BluetoothState>): void--><!--Device-bluetoothManager-function on(type: 'stateChange', callback: Callback<BluetoothState>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BluetoothState&gt; | Yes |

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
function onReceiveEvent(data: bluetoothManager.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('stateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```
