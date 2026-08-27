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

**Deprecated since:** 9

**Substitutes:** [getBtConnectionState](arkts-connectivity-bluetoothmanager-getbtconnectionstate-f.md)

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| ProfileConnectionState | One of { |

**Examples**

```TypeScript
let connectionState : bluetooth.ProfileConnectionState = bluetooth.getBtConnectionState();
```
