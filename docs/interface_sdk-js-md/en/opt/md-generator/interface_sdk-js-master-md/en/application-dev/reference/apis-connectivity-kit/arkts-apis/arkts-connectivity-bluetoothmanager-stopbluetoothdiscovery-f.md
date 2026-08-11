# stopBluetoothDiscovery

## Modules to Import

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## stopBluetoothDiscovery

```TypeScript
function stopBluetoothDiscovery(): void
```

Stops Bluetooth device scanning.On API 10 and above, the permission required by this interface is changed from DISCOVER_BLUETOOTH to ACCESS_BLUETOOTH.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** ohos.bluetooth.connection/connection#stopBluetoothDiscovery

**Required permissions:** 
- API version 10+: ohos.permission.ACCESS_BLUETOOTH
- API version 9: ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetoothManager-function stopBluetoothDiscovery(): void--><!--Device-bluetoothManager-function stopBluetoothDiscovery(): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.stopBluetoothDiscovery();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```
