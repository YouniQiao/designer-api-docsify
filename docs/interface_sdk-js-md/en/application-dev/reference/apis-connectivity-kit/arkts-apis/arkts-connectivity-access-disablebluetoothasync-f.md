# disableBluetoothAsync

## Modules to Import

```TypeScript
import { access } from 'kits/@kit.ConnectivityKit';
```

## disableBluetoothAsync

```TypeScript
function disableBluetoothAsync(): Promise<void>
```

Asynchronous interface for disables Bluetooth on a device.

**Since:** 20

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900001 |
| 2900013 |
| 2900014 |
| 2900099 |
