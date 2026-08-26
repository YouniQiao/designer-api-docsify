# getLocalName

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

## getLocalName

```TypeScript
function getLocalName(): string
```

Obtains the Bluetooth local name of a device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getLocalName](arkts-connectivity-bluetoothmanager-getlocalname-f.md)

**Required permissions:** ohos.permission.USE_BLUETOOTH

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the name the device. |

**Examples**

```TypeScript
let localName : string = bluetooth.getLocalName();
```
