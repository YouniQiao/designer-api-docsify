# CharacteristicWriteReq

Describes the parameters of the of the Gatt client's characteristic write request.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.CharacteristicWriteRequest

<!--Device-bluetooth-interface CharacteristicWriteReq--><!--Device-bluetooth-interface CharacteristicWriteReq-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetooth } from 'kits/@kit.ConnectivityKit';
```

## characteristicUuid

```TypeScript
characteristicUuid: string
```

The UUID of a CharacteristicWriteReq instance

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.CharacteristicWriteRequest.characteristicUuid

<!--Device-CharacteristicWriteReq-characteristicUuid: string--><!--Device-CharacteristicWriteReq-characteristicUuid: string-End-->

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

**替代接口：** ohos.bluetoothManager/bluetoothManager.CharacteristicWriteRequest.deviceId

<!--Device-CharacteristicWriteReq-deviceId: string--><!--Device-CharacteristicWriteReq-deviceId: string-End-->

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

**替代接口：** ohos.bluetoothManager/bluetoothManager.CharacteristicWriteRequest.isPrep

<!--Device-CharacteristicWriteReq-isPrep: boolean--><!--Device-CharacteristicWriteReq-isPrep: boolean-End-->

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

**替代接口：** ohos.bluetoothManager/bluetoothManager.CharacteristicWriteRequest.needRsp

<!--Device-CharacteristicWriteReq-needRsp: boolean--><!--Device-CharacteristicWriteReq-needRsp: boolean-End-->

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

**替代接口：** ohos.bluetoothManager/bluetoothManager.CharacteristicWriteRequest.offset

<!--Device-CharacteristicWriteReq-offset: number--><!--Device-CharacteristicWriteReq-offset: number-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## serviceUuid

```TypeScript
serviceUuid: string
```

The UUID of the service to which the characteristic belongs

**类型：** string

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.bluetoothManager/bluetoothManager.CharacteristicWriteRequest.serviceUuid

<!--Device-CharacteristicWriteReq-serviceUuid: string--><!--Device-CharacteristicWriteReq-serviceUuid: string-End-->

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

**替代接口：** ohos.bluetoothManager/bluetoothManager.CharacteristicWriteRequest.transId

<!--Device-CharacteristicWriteReq-transId: number--><!--Device-CharacteristicWriteReq-transId: number-End-->

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

**替代接口：** ohos.bluetoothManager/bluetoothManager.CharacteristicWriteRequest.value

<!--Device-CharacteristicWriteReq-value: ArrayBuffer--><!--Device-CharacteristicWriteReq-value: ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

