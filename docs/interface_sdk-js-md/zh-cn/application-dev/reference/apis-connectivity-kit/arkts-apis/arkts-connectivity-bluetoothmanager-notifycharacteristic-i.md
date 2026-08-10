# NotifyCharacteristic

Describes the value of the indication or notification sent by the Gatt server.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.NotifyCharacteristic

<!--Device-bluetoothManager-interface NotifyCharacteristic--><!--Device-bluetoothManager-interface NotifyCharacteristic-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of a NotifyCharacteristic instance

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.NotifyCharacteristic#characteristicUuid

<!--Device-NotifyCharacteristic-characteristicUuid: string--><!--Device-NotifyCharacteristic-characteristicUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## characteristicValue

```TypeScript
characteristicValue: ArrayBuffer
```

The value of a NotifyCharacteristic instance

**类型：** ArrayBuffer

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.NotifyCharacteristic#characteristicValue

<!--Device-NotifyCharacteristic-characteristicValue: ArrayBuffer--><!--Device-NotifyCharacteristic-characteristicValue: ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## confirm

```TypeScript
confirm: boolean
```

Specifies whether to request confirmation from the BLE peripheral device (indication) or send a notification. Value {@code true} indicates the former and {@code false} indicates the latter.

**类型：** boolean

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.NotifyCharacteristic#confirm

<!--Device-NotifyCharacteristic-confirm: boolean--><!--Device-NotifyCharacteristic-confirm: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the {@link GattService} instance to which the characteristic belongs

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.NotifyCharacteristic#serviceUuid

<!--Device-NotifyCharacteristic-serviceUuid: string--><!--Device-NotifyCharacteristic-serviceUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

