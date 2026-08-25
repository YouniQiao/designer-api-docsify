# getState

## Modules to Import

```TypeScript
import { access } from 'kits/@kit.ConnectivityKit';
```

## getState

```TypeScript
function getState(): BluetoothState
```

Obtains the Bluetooth status of a device.

**Since:** 10

**Required permissions:** 
- API version 10 - 12: ohos.permission.ACCESS_BLUETOOTH

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BluetoothState](arkts-connectivity-bluetoothmanager-bluetoothstate-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900001 |
| 2900099 |
