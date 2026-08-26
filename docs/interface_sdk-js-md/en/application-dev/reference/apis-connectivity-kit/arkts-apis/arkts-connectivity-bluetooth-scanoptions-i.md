# ScanOptions

Describes the parameters for scan.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [ScanOptions](arkts-connectivity-bluetoothmanager-scanoptions-i.md)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import bas from '@kit.ConnectivityKit.bas';
import common from '@kit.ConnectivityKit.common';
import bluetooth from '@kit.ConnectivityKit';
import map from '@kit.ConnectivityKit.map';
import pan from '@kit.ConnectivityKit.pan';
import pbap from '@kit.ConnectivityKit.pbap';
import opp from '@kit.ConnectivityKit.opp';
import socket from '@kit.ConnectivityKit.socket';
import wearDetection from '@kit.ConnectivityKit.wearDetection';
import bluetoothManager from '@kit.ConnectivityKitManager';
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

**System capability:** SystemCapability.Communication.Bluetooth.Core
