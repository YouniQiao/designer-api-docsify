# pairDevice

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

## pairDevice

```TypeScript
function pairDevice(deviceId: string): boolean
```

Starts pairing with a remote Bluetooth device.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [pairDevice](arkts-connectivity-bluetoothmanager-pairdevice-f.md)

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | The address of the remote device to pair. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Examples**

```TypeScript
// The address can be scanned.
let result : boolean = bluetooth.pairDevice("XX:XX:XX:XX:XX:XX");
```
