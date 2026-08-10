# DescriptorWriteRequest

Describes the parameters of the Gatt client's characteristic write request.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorWriteRequest

<!--Device-bluetoothManager-interface DescriptorWriteRequest--><!--Device-bluetoothManager-interface DescriptorWriteRequest-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of the characteristic to which the descriptor belongs

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorWriteRequest#characteristicUuid

<!--Device-DescriptorWriteRequest-characteristicUuid: string--><!--Device-DescriptorWriteRequest-characteristicUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## descriptorUuid

```TypeScript
descriptorUuid: string
```

The UUID of a DescriptorWriteRequest instance

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorWriteRequest#descriptorUuid

<!--Device-DescriptorWriteRequest-descriptorUuid: string--><!--Device-DescriptorWriteRequest-descriptorUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Indicates the address of the client that initiates the write request

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorWriteRequest#deviceId

<!--Device-DescriptorWriteRequest-deviceId: string--><!--Device-DescriptorWriteRequest-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## isPrep

```TypeScript
isPrep: boolean
```

Whether this request should be pending for later operation

**类型：** boolean

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorWriteRequest#isPrepared

<!--Device-DescriptorWriteRequest-isPrep: boolean--><!--Device-DescriptorWriteRequest-isPrep: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## needRsp

```TypeScript
needRsp: boolean
```

Whether the remote client need a response

**类型：** boolean

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorWriteRequest#needRsp

<!--Device-DescriptorWriteRequest-needRsp: boolean--><!--Device-DescriptorWriteRequest-needRsp: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## offset

```TypeScript
offset: number
```

Indicates the byte offset of the start position for writing characteristic value

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorWriteRequest#offset

<!--Device-DescriptorWriteRequest-offset: number--><!--Device-DescriptorWriteRequest-offset: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service to which the descriptor belongs

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorWriteRequest#serviceUuid

<!--Device-DescriptorWriteRequest-serviceUuid: string--><!--Device-DescriptorWriteRequest-serviceUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## transId

```TypeScript
transId: number
```

The Id of the write request

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorWriteRequest#transId

<!--Device-DescriptorWriteRequest-transId: number--><!--Device-DescriptorWriteRequest-transId: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## value

```TypeScript
value: ArrayBuffer
```

Indicates the value to be written

**类型：** ArrayBuffer

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.ble/ble.DescriptorWriteRequest#value

<!--Device-DescriptorWriteRequest-value: ArrayBuffer--><!--Device-DescriptorWriteRequest-value: ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

