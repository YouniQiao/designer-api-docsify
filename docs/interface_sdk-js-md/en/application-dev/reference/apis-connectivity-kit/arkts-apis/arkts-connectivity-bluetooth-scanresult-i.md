# ScanResult

Describes the contents of the scan results.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [ScanResult](arkts-connectivity-bluetoothmanager-scanresult-i.md)

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

## data

```TypeScript
data: ArrayBuffer
```

The raw data of broadcast packet

**Type:** ArrayBuffer

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [data](arkts-connectivity-bluetoothmanager-scanresult-i.md#data)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Address of the scanned device

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [deviceId](arkts-connectivity-bluetoothmanager-scanresult-i.md#deviceid)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## rssi

```TypeScript
rssi: number
```

RSSI of the remote device

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [rssi](arkts-connectivity-bluetoothmanager-scanresult-i.md#rssi)

**System capability:** SystemCapability.Communication.Bluetooth.Core
