# on_bondStateChange

## Modules to Import

```TypeScript
import { bluetoothManager } from 'bluetoothManager';
```

## on_bondStateChange

```TypeScript
function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void
```

Subscribe the event reported when a remote Bluetooth device is bonded. On API 10 and above, the permission required by this interface is changed from USE_BLUETOOTH to ACCESS_BLUETOOTH.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** bondStateChange

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH
- API version 9: ohos.permission.USE_BLUETOOTH

<!--Device-bluetoothManager-function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void--><!--Device-bluetoothManager-function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bondStateChange' | Yes | Type of the bond state event to listen for. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BondStateParam&gt; | Yes | Callback used to listen for the bond state event, [BondStateParam](arkts-connectivity-bluetoothmanager-bondstateparam-i.md#BondStateParam). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BondStateParam) { // data, as the input parameter of the callback, indicates the pairing state.
    console.info('pair state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

