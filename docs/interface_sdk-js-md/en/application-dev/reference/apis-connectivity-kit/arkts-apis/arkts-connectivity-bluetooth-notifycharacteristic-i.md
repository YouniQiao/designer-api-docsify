# NotifyCharacteristic

Describes the value of the indication or notification sent by the Gatt server.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [NotifyCharacteristic](arkts-connectivity-bluetoothmanager-notifycharacteristic-i.md#notifycharacteristic)

<!--Device-bluetooth-interface NotifyCharacteristic--><!--Device-bluetooth-interface NotifyCharacteristic-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { a2dp } from '@kit.ConnectivityKit';
import { access } from '@kit.ConnectivityKit';
import { baseProfile } from '@kit.ConnectivityKit';
import { ble } from '@kit.ConnectivityKit';
import { connection } from '@kit.ConnectivityKit';
import { constant } from '@kit.ConnectivityKit';
import { hfp } from '@kit.ConnectivityKit';
import { hid } from '@kit.ConnectivityKit';
import { bas } from '@kit.ConnectivityKit';
import { common } from '@kit.ConnectivityKit';
import { bluetooth } from '@kit.ConnectivityKit';
import { map } from '@kit.ConnectivityKit';
import { pan } from '@kit.ConnectivityKit';
import { pbap } from '@kit.ConnectivityKit';
import { opp } from '@kit.ConnectivityKit';
import { socket } from '@kit.ConnectivityKit';
import { wearDetection } from '@kit.ConnectivityKit';
import { bluetoothManager } from '@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of a NotifyCharacteristic instance

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [characteristicUuid](arkts-connectivity-bluetoothmanager-notifycharacteristic-i.md#characteristicuuid)

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

**Substitutes:** [characteristicValue](arkts-connectivity-bluetoothmanager-notifycharacteristic-i.md#characteristicvalue)

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

**Substitutes:** [confirm](arkts-connectivity-bluetoothmanager-notifycharacteristic-i.md#confirm)

<!--Device-NotifyCharacteristic-confirm: boolean--><!--Device-NotifyCharacteristic-confirm: boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the [GattService](arkts-connectivity-bluetooth-gattservice-i.md#gattservice) instance to which the characteristic belongs

**Type:** string

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [serviceUuid](arkts-connectivity-bluetoothmanager-notifycharacteristic-i.md#serviceuuid)

<!--Device-NotifyCharacteristic-serviceUuid: string--><!--Device-NotifyCharacteristic-serviceUuid: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

