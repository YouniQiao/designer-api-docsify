# disableBluetooth

## Modules to Import

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## disableBluetooth

```TypeScript
function disableBluetooth(): void
```

Disables Bluetooth on a device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-access-function disableBluetooth(): void--><!--Device-access-function disableBluetooth(): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.disableBluetooth();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
