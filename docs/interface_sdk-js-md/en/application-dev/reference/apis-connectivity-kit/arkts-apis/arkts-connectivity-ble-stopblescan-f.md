# stopBLEScan

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## stopBLEScan

```TypeScript
function stopBLEScan(): void
```

Stops BLE scanning.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ble-function stopBLEScan(): void--><!--Device-ble-function stopBLEScan(): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
try {
    ble.stopBLEScan();
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
