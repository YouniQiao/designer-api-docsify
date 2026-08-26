# BLECharacteristic

Describes the Gatt characteristic.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [BLECharacteristic](arkts-connectivity-bluetoothmanager-blecharacteristic-i.md)

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

The UUID of a BLECharacteristic instance

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [characteristicUuid](arkts-connectivity-bluetoothmanager-blecharacteristic-i.md#characteristicuuid)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## characteristicValue

```TypeScript
characteristicValue: ArrayBuffer
```

The value of a BLECharacteristic instance

**Type:** ArrayBuffer

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [characteristicValue](arkts-connectivity-bluetoothmanager-blecharacteristic-i.md#characteristicvalue)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## descriptors

```TypeScript
descriptors: Array<BLEDescriptor>
```

The list of [BLEDescriptor](arkts-connectivity-bluetooth-bledescriptor-i.md) contained in the characteristic

**Type:** Array&lt;BLEDescriptor&gt;

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [descriptors](arkts-connectivity-bluetoothmanager-blecharacteristic-i.md#descriptors)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the [GattService](arkts-connectivity-bluetooth-gattservice-i.md) instance to which the characteristic belongs

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [serviceUuid](arkts-connectivity-bluetoothmanager-blecharacteristic-i.md#serviceuuid)

**System capability:** SystemCapability.Communication.Bluetooth.Core
