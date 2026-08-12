# getBtConnectionState

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## getBtConnectionState

```TypeScript
function getBtConnectionState(): ProfileConnectionState
```

Get the local device connection state to any profile of any remote device.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [getBtConnectionState](ohos.bluetoothManager/bluetoothManager.getBtConnectionState)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getBtConnectionState(): ProfileConnectionState--><!--Device-bluetooth-function getBtConnectionState(): ProfileConnectionState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| ProfileConnectionState | One of { |

## Examples

```TypeScript
let connectionState : bluetooth.ProfileConnectionState = bluetooth.getBtConnectionState();
```

