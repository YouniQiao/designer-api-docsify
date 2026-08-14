# enableBluetoothAsync

## Modules to Import

```TypeScript
import { access } from 'access';
```

## enableBluetoothAsync

```TypeScript
function enableBluetoothAsync(): Promise<void>
```

Asynchronous interface for enables Bluetooth on a device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-access-function enableBluetoothAsync(): Promise<void>--><!--Device-access-function enableBluetoothAsync(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns the promise object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900013 | The user does not respond. |
| 2900014 | User refuse the action. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.enableBluetoothAsync().then(() => {
        console.info('enableBluetoothAsync');
    }, (error: BusinessError) => {
        console.error('enableBluetoothAsync: errCode:' + error.code + ',errMessage' + error.message);
    })
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

