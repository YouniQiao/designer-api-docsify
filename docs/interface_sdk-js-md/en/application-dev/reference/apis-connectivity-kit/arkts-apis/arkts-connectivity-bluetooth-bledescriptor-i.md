# BLEDescriptor

Describes the Gatt descriptor.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BLEDescriptor](arkts-connectivity-bluetoothmanager-bledescriptor-i.md)

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

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of the [BLECharacteristic](arkts-connectivity-bluetooth-blecharacteristic-i.md) instance to which the descriptor belongs

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [characteristicUuid](arkts-connectivity-bluetoothmanager-bledescriptor-i.md#characteristicuuid)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## descriptorUuid

```TypeScript
descriptorUuid: string
```

The UUID of the BLEDescriptor instance

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [descriptorUuid](arkts-connectivity-bluetoothmanager-bledescriptor-i.md#descriptoruuid)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## descriptorValue

```TypeScript
descriptorValue: ArrayBuffer
```

The value of the BLEDescriptor instance

**Type:** ArrayBuffer

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [descriptorValue](arkts-connectivity-bluetoothmanager-bledescriptor-i.md#descriptorvalue)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the [GattService](arkts-connectivity-bluetooth-gattservice-i.md) instance to which the descriptor belongs

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [serviceUuid](arkts-connectivity-bluetoothmanager-bledescriptor-i.md#serviceuuid)

**System capability:** SystemCapability.Communication.Bluetooth.Core
