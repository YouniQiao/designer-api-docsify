# enableBluetoothAsync

## Modules to Import

```TypeScript
import { access } from 'kits/@kit.ConnectivityKit';
```

## enableBluetoothAsync

```TypeScript
function enableBluetoothAsync(): Promise<void>
```

Asynchronous interface for enables Bluetooth on a device.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-access-function enableBluetoothAsync(): Promise<void>--><!--Device-access-function enableBluetoothAsync(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns the promise object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
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

