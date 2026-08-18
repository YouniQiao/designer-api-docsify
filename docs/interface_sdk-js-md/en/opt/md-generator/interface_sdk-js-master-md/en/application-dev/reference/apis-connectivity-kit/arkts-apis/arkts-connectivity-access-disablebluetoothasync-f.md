# disableBluetoothAsync

## Modules to Import

```TypeScript
```

## disableBluetoothAsync

```TypeScript
function disableBluetoothAsync(): Promise<void>
```

Asynchronous interface for disables Bluetooth on a device.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-access-function disableBluetoothAsync(): Promise<void>--><!--Device-access-function disableBluetoothAsync(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900013 |
| 2900014 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900099 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.disableBluetoothAsync().then(() => {
        console.info('disableBluetoothAsync');
    }, (error: BusinessError) => {
        console.error('disableBluetoothAsync: errCode:' + error.code + ',errMessage' + error.message);
    })
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
