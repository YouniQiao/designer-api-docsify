# getPersistentDeviceIds

## Modules to Import

```TypeScript
import { access } from 'kits/@kit.ConnectivityKit';
```

## getPersistentDeviceIds

```TypeScript
function getPersistentDeviceIds(): string[]
```

Obtains the persistent randomized device address of the application.

**Since:** 16

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.PERSISTENT_BLUETOOTH_PEERS_MAC

**Atomic service API:** This API can be used in atomic services since API version 16.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900003 |
| 2900099 |
