# BLEConnectChangedState

Describes the Gatt profile connection state.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** BLEConnectionChangeState

<!--Device-bluetoothManager-interface BLEConnectChangedState--><!--Device-bluetoothManager-interface BLEConnectChangedState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## deviceId

```TypeScript
deviceId: string
```

Indicates the peer device address

**Type:** string

**Since:** 9

**Deprecated since:** 10

**Substitutes:** deviceId

<!--Device-BLEConnectChangedState-deviceId: string--><!--Device-BLEConnectChangedState-deviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: ProfileConnectionState
```

Connection state of the Gatt profile

**Type:** ProfileConnectionState

**Since:** 9

**Deprecated since:** 10

**Substitutes:** state

<!--Device-BLEConnectChangedState-state: ProfileConnectionState--><!--Device-BLEConnectChangedState-state: ProfileConnectionState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

