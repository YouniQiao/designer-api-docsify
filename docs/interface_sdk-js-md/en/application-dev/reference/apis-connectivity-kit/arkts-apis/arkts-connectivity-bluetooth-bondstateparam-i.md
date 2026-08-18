# BondStateParam

Describes the class of a bluetooth device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [BondStateParam](arkts-connectivity-bluetoothmanager-bondstateparam-i.md)

<!--Device-bluetooth-interface BondStateParam--><!--Device-bluetooth-interface BondStateParam-End-->

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

Address of a Bluetooth device.

**Type:** string

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [deviceId](arkts-connectivity-bluetoothmanager-bondstateparam-i.md#deviceid)

<!--Device-BondStateParam-deviceId: string--><!--Device-BondStateParam-deviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: BondState
```

Profile connection state of the device.

**Type:** BondState

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [state](arkts-connectivity-bluetoothmanager-bondstateparam-i.md#state)

<!--Device-BondStateParam-state: BondState--><!--Device-BondStateParam-state: BondState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

