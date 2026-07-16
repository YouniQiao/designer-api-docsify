# NotifyCharacteristic

Describes the value of the indication or notification sent by the Gatt server.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** NotifyCharacteristic

<!--Device-bluetooth-interface NotifyCharacteristic--><!--Device-bluetooth-interface NotifyCharacteristic-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of a NotifyCharacteristic instance

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicUuid

<!--Device-NotifyCharacteristic-characteristicUuid: string--><!--Device-NotifyCharacteristic-characteristicUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## characteristicValue

```TypeScript
characteristicValue: ArrayBuffer
```

The value of a NotifyCharacteristic instance

**Type:** ArrayBuffer

**Since:** 7

**Deprecated since:** 9

**Substitutes:** characteristicValue

<!--Device-NotifyCharacteristic-characteristicValue: ArrayBuffer--><!--Device-NotifyCharacteristic-characteristicValue: ArrayBuffer-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## confirm

```TypeScript
confirm: boolean
```

Specifies whether to request confirmation from the BLE peripheral device (indication) or send a notification. Value {@code true} indicates the former and {@code false} indicates the latter.

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** confirm

<!--Device-NotifyCharacteristic-confirm: boolean--><!--Device-NotifyCharacteristic-confirm: boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the {@link GattService} instance to which the characteristic belongs

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** serviceUuid

<!--Device-NotifyCharacteristic-serviceUuid: string--><!--Device-NotifyCharacteristic-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

