# getBtConnectionState

## Modules to Import

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## getBtConnectionState

```TypeScript
function getBtConnectionState(): ProfileConnectionState
```

Get the local device connection state to any profile of any remote device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.bluetoothManager/bluetoothManager.getBtConnectionState

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getBtConnectionState(): ProfileConnectionState--><!--Device-bluetooth-function getBtConnectionState(): ProfileConnectionState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ProfileConnectionState](arkts-connectivity-bluetooth-profileconnectionstate-e.md) |

## Examples

```TypeScript
let connectionState : bluetooth.ProfileConnectionState = bluetooth.getBtConnectionState();
```
