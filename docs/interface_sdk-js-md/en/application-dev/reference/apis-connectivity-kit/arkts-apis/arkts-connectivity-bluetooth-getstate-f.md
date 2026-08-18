# getState

## Modules to Import

```TypeScript
import { a2dp } from '@kit.ConnectivityKit';
import { access } from '@kit.ConnectivityKit';
import { baseProfile } from '@kit.ConnectivityKit';
import { ble } from '@kit.ConnectivityKit';
import { connection } from '@kit.ConnectivityKit';
import { constant } from '@kit.ConnectivityKit';
import { hfp } from '@kit.ConnectivityKit';
import { hid } from '@kit.ConnectivityKit';
import { bas } from '@kit.ConnectivityKit';
import { common } from '@kit.ConnectivityKit';
import { bluetooth } from '@kit.ConnectivityKit';
import { map } from '@kit.ConnectivityKit';
import { pan } from '@kit.ConnectivityKit';
import { pbap } from '@kit.ConnectivityKit';
import { opp } from '@kit.ConnectivityKit';
import { socket } from '@kit.ConnectivityKit';
import { wearDetection } from '@kit.ConnectivityKit';
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## getState

```TypeScript
function getState(): BluetoothState
```

Obtains the Bluetooth status of a device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getState](arkts-connectivity-bluetoothmanager-getstate-f.md)

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function getState(): BluetoothState--><!--Device-bluetooth-function getState(): BluetoothState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| BluetoothState | Returns the Bluetooth status, which can be { |

**Examples**

```TypeScript
let state : bluetooth.BluetoothState = bluetooth.getState();
```

