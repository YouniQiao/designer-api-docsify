# isBluetoothDiscovering

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## isBluetoothDiscovering

```TypeScript
function isBluetoothDiscovering(): boolean
```

Check if bluetooth is discovering.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function isBluetoothDiscovering(): boolean--><!--Device-connection-function isBluetoothDiscovering(): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let res: boolean = connection.isBluetoothDiscovering();
    console.info('isBluetoothDiscovering: ' + res);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

