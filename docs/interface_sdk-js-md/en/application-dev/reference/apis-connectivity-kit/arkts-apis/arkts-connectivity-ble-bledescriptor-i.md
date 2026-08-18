# BLEDescriptor

Describes the Gatt descriptor.

**Since:** 23

<!--Device-ble-interface BLEDescriptor--><!--Device-ble-interface BLEDescriptor-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of the [BLECharacteristic](arkts-connectivity-ble-blecharacteristic-i.md) instance to which the descriptor belongs

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BLEDescriptor-characteristicUuid: string--><!--Device-BLEDescriptor-characteristicUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## descriptorHandle

```TypeScript
descriptorHandle?: int
```

The descriptor handle of the BLEDescriptor instance

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BLEDescriptor-descriptorHandle?: int--><!--Device-BLEDescriptor-descriptorHandle?: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## descriptorUuid

```TypeScript
descriptorUuid: string
```

The UUID of the BLEDescriptor instance

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BLEDescriptor-descriptorUuid: string--><!--Device-BLEDescriptor-descriptorUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## descriptorValue

```TypeScript
descriptorValue: ArrayBuffer
```

The value of the BLEDescriptor instance

**Type:** ArrayBuffer

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BLEDescriptor-descriptorValue: ArrayBuffer--><!--Device-BLEDescriptor-descriptorValue: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## permissions

```TypeScript
permissions?: GattPermissions
```

The permissions of a BLEDescriptor instance. The default value is Readable and Writable.

**Type:** [GattPermissions](arkts-connectivity-ble-gattpermissions-i.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BLEDescriptor-permissions?: GattPermissions--><!--Device-BLEDescriptor-permissions?: GattPermissions-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the [GattService](arkts-connectivity-ble-gattservice-i.md) instance to which the descriptor belongs

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BLEDescriptor-serviceUuid: string--><!--Device-BLEDescriptor-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

