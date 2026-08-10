# CharacteristicReadRequest

Describes the parameters of the Gatt client's characteristic read request.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.CharacteristicReadRequest

<!--Device-bluetoothManager-interface CharacteristicReadRequest--><!--Device-bluetoothManager-interface CharacteristicReadRequest-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of a CharacteristicReadRequest instance

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.CharacteristicReadRequest#characteristicUuid

<!--Device-CharacteristicReadRequest-characteristicUuid: string--><!--Device-CharacteristicReadRequest-characteristicUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Indicates the address of the client that initiates the read request

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.CharacteristicReadRequest#deviceId

<!--Device-CharacteristicReadRequest-deviceId: string--><!--Device-CharacteristicReadRequest-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## offset

```TypeScript
offset: number
```

Indicates the byte offset of the start position for reading characteristic value

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.CharacteristicReadRequest#offset

<!--Device-CharacteristicReadRequest-offset: number--><!--Device-CharacteristicReadRequest-offset: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service to which the characteristic belongs

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.CharacteristicReadRequest#serviceUuid

<!--Device-CharacteristicReadRequest-serviceUuid: string--><!--Device-CharacteristicReadRequest-serviceUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## transId

```TypeScript
transId: number
```

The Id of the read request

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.CharacteristicReadRequest#transId

<!--Device-CharacteristicReadRequest-transId: number--><!--Device-CharacteristicReadRequest-transId: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

