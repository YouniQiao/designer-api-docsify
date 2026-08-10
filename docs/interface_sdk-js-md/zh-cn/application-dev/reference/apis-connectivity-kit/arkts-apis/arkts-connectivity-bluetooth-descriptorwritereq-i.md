# DescriptorWriteReq

Describes the parameters of the Gatt client's characteristic write request.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorWriteRequest

<!--Device-bluetooth-interface DescriptorWriteReq--><!--Device-bluetooth-interface DescriptorWriteReq-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of the characteristic to which the descriptor belongs

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorWriteRequest.characteristicUuid

<!--Device-DescriptorWriteReq-characteristicUuid: string--><!--Device-DescriptorWriteReq-characteristicUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## descriptorUuid

```TypeScript
descriptorUuid: string
```

The UUID of a DescriptorWriteReq instance

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorWriteRequest.descriptorUuid

<!--Device-DescriptorWriteReq-descriptorUuid: string--><!--Device-DescriptorWriteReq-descriptorUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

Indicates the address of the client that initiates the write request

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorWriteRequest.deviceId

<!--Device-DescriptorWriteReq-deviceId: string--><!--Device-DescriptorWriteReq-deviceId: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## isPrep

```TypeScript
isPrep: boolean
```

Whether this request should be pending for later operation

**类型：** boolean

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorWriteRequest.isPrep

<!--Device-DescriptorWriteReq-isPrep: boolean--><!--Device-DescriptorWriteReq-isPrep: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## needRsp

```TypeScript
needRsp: boolean
```

Whether the remote client need a response

**类型：** boolean

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorWriteRequest.needRsp

<!--Device-DescriptorWriteReq-needRsp: boolean--><!--Device-DescriptorWriteReq-needRsp: boolean-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## offset

```TypeScript
offset: number
```

Indicates the byte offset of the start position for writing characteristic value

**类型：** number

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorWriteRequest.offset

<!--Device-DescriptorWriteReq-offset: number--><!--Device-DescriptorWriteReq-offset: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service to which the descriptor belongs

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorWriteRequest.serviceUuid

<!--Device-DescriptorWriteReq-serviceUuid: string--><!--Device-DescriptorWriteReq-serviceUuid: string-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## transId

```TypeScript
transId: number
```

The Id of the write request

**类型：** number

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorWriteRequest.transId

<!--Device-DescriptorWriteReq-transId: number--><!--Device-DescriptorWriteReq-transId: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## value

```TypeScript
value: ArrayBuffer
```

Indicates the value to be written

**类型：** ArrayBuffer

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.DescriptorWriteRequest.value

<!--Device-DescriptorWriteReq-value: ArrayBuffer--><!--Device-DescriptorWriteReq-value: ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

