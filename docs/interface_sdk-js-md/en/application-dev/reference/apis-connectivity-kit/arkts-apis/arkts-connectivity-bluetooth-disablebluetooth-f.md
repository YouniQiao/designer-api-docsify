# disableBluetooth

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

## disableBluetooth

```TypeScript
function disableBluetooth(): boolean
```

Disables Bluetooth on a device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [disableBluetooth](arkts-connectivity-bluetoothmanager-disablebluetooth-f.md)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
let disable : boolean = bluetooth.disableBluetooth();
```
