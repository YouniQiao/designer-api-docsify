# ScanFilter

Describes the criteria for filtering scanning results can be set.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [ScanFilter](arkts-connectivity-bluetoothmanager-scanfilter-i.md)

<!--Device-bluetooth-interface ScanFilter--><!--Device-bluetooth-interface ScanFilter-End-->

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
deviceId?: string
```

The address of a BLE peripheral device

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [deviceId](arkts-connectivity-bluetoothmanager-scanfilter-i.md#deviceid)

<!--Device-ScanFilter-deviceId?: string--><!--Device-ScanFilter-deviceId?: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## name

```TypeScript
name?: string
```

The name of a BLE peripheral device

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [name](arkts-connectivity-bluetoothmanager-scanfilter-i.md#name)

<!--Device-ScanFilter-name?: string--><!--Device-ScanFilter-name?: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid?: string
```

The service UUID of a BLE peripheral device

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [serviceUuid](arkts-connectivity-bluetoothmanager-scanfilter-i.md#serviceuuid)

<!--Device-ScanFilter-serviceUuid?: string--><!--Device-ScanFilter-serviceUuid?: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

