# PinRequiredParam

Describes the bond key param.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [PinRequiredParam](arkts-connectivity-bluetoothmanager-pinrequiredparam-i.md#pinrequiredparam)

<!--Device-bluetooth-interface PinRequiredParam--><!--Device-bluetooth-interface PinRequiredParam-End-->

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

ID of the device to pair.

**Type:** string

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [deviceId](arkts-connectivity-bluetoothmanager-pinrequiredparam-i.md#deviceid)

<!--Device-PinRequiredParam-deviceId: string--><!--Device-PinRequiredParam-deviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## pinCode

```TypeScript
pinCode: string
```

Key for the device pairing.

**Type:** string

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [pinCode](arkts-connectivity-bluetoothmanager-pinrequiredparam-i.md#pincode)

<!--Device-PinRequiredParam-pinCode: string--><!--Device-PinRequiredParam-pinCode: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

