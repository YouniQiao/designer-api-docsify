# ScanOptions

Describes the parameters for scan.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [ScanOptions](arkts-connectivity-bluetoothmanager-scanoptions-i.md#scanoptions)

<!--Device-bluetooth-interface ScanOptions--><!--Device-bluetooth-interface ScanOptions-End-->

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

## dutyMode

```TypeScript
dutyMode?: ScanDuty
```

Bluetooth LE scan mode

**Type:** ScanDuty

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [dutyMode](arkts-connectivity-bluetoothmanager-scanoptions-i.md#dutymode)

<!--Device-ScanOptions-dutyMode?: ScanDuty--><!--Device-ScanOptions-dutyMode?: ScanDuty-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## interval

```TypeScript
interval?: number
```

Time of delay for reporting the scan result

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [interval](arkts-connectivity-bluetoothmanager-scanoptions-i.md#interval)

<!--Device-ScanOptions-interval?: number--><!--Device-ScanOptions-interval?: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## matchMode

```TypeScript
matchMode?: MatchMode
```

Match mode for Bluetooth LE scan filters hardware match

**Type:** MatchMode

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [matchMode](arkts-connectivity-bluetoothmanager-scanoptions-i.md#matchmode)

<!--Device-ScanOptions-matchMode?: MatchMode--><!--Device-ScanOptions-matchMode?: MatchMode-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

