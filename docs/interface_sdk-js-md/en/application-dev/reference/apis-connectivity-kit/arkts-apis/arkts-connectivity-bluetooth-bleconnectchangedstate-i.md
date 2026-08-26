# BLEConnectChangedState

Describes the Gatt profile connection state.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BLEConnectChangedState](arkts-connectivity-bluetoothmanager-bleconnectchangedstate-i.md)

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

## deviceId

```TypeScript
deviceId: string
```

Indicates the peer device address

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [deviceId](arkts-connectivity-bluetoothmanager-bleconnectchangedstate-i.md#deviceid)

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

**System capability:** SystemCapability.Communication.Bluetooth.Core
