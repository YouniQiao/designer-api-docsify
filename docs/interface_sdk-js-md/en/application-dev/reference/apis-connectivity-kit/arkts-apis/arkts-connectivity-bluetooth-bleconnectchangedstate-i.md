# BLEConnectChangedState

Describes the Gatt profile connection state.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BLEConnectChangedState](arkts-connectivity-bluetoothmanager-bleconnectchangedstate-i.md#bleconnectchangedstate)

<!--Device-bluetooth-interface BLEConnectChangedState--><!--Device-bluetooth-interface BLEConnectChangedState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

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

## deviceId

```TypeScript
deviceId: string
```

Indicates the peer device address

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [deviceId](arkts-connectivity-bluetoothmanager-bleconnectchangedstate-i.md#deviceid)

<!--Device-BLEConnectChangedState-deviceId: string--><!--Device-BLEConnectChangedState-deviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: ProfileConnectionState
```

Connection state of the Gatt profile

**Type:** ProfileConnectionState

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [state](arkts-connectivity-bluetoothmanager-bleconnectchangedstate-i.md#state)

<!--Device-BLEConnectChangedState-state: ProfileConnectionState--><!--Device-BLEConnectChangedState-state: ProfileConnectionState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

