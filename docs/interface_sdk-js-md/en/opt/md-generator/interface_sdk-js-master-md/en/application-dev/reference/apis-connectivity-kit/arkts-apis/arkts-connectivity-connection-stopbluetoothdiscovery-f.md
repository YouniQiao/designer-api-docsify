# stopBluetoothDiscovery

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## stopBluetoothDiscovery

```TypeScript
function stopBluetoothDiscovery(): void
```

Stops Bluetooth device scanning.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-connection-function stopBluetoothDiscovery(): void--><!--Device-connection-function stopBluetoothDiscovery(): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.stopBluetoothDiscovery();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
